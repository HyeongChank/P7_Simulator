import pandas as pd
import xgboost as xgb
import numpy as np
import datetime
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from scipy.interpolate import interp1d
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras import backend as K
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def postdata():
    def load_data():
        data = pd.read_csv("D:/김형찬/Congest_project/data/sorted_truck_simulation_results.csv", encoding='cp949')
        print(data.head())
        return data

    def preprocessing_data(data):
        data['unload_block'] = data['unload_block'].replace({'<simpy.resources.resource.Resource object at 0x0000019BF88723B0>':1, '<simpy.resources.resource.Resource object at 0x0000019BF88723E0>':2,
                                                              '<simpy.resources.resource.Resource object at 0x0000019BF94954B0>':3,'<simpy.resources.resource.Resource object at 0x0000019BF94955A0>':4,
                                                                '<simpy.resources.resource.Resource object at 0x0000019BF94962C0>':5})

        data['load_block'] = data['unload_block'].replace({'<simpy.resources.resource.Resource object at 0x0000019BF94963E0>':1, '<simpy.resources.resource.Resource object at 0x0000019BF94963E0>':2,
                                                              '<simpy.resources.resource.Resource object at 0x0000019BF9496350>':3,'<simpy.resources.resource.Resource object at 0x0000019BF9496380>':4,
                                                                '<simpy.resources.resource.Resource object at 0x0000019BF94963E0>':5})
        print(data[['unload_block', 'load_block']])        
        data['wait_time_unload_spot'] = data['start_unload_work'] - data['arrive_unload_spot']
        data['wait_time_load_spot'] = data['start_load_work'] - data['arrive_load_spot']
        n_data = data.copy()
        n_data['code'] = n_data['code'].replace({'in': 1, 'out': 2, 'in_out': 3})        
        # print(n_data[['number','code','entryTime','unload_count','wait_time_unload_spot','load_count','wait_time_load_spot','unload_block', 'load_block']])
        df = pd.DataFrame(n_data)
        df_unload = df[df['code'].isin([1,3])]
        #print(df_unload)
        df_load = df[df['code'].isin([2,3])]
        df_unload_pre = df_unload[['unload_block','entryTime','wait_time_unload_spot', 'unload_count']]
        df_load_pre = df_load[['load_block','entryTime','wait_time_load_spot', 'load_count']]
        #print(df_unload_pre)

        for col in ['unload_block','entryTime', 'wait_time_unload_spot', 'unload_count']:
            df_unload_pre[col] = pd.to_numeric(df_unload_pre[col], errors='coerce')
        for col in ['load_block','entryTime', 'wait_time_load_spot', 'load_count']:    
            df_load_pre[col] = pd.to_numeric(df_load_pre[col], errors='coerce')
        # 'entryTime'을 5 단위로 그룹화
        data_unload = df_unload_pre.copy()
        data_load = df_load_pre.copy()
        print(data_unload)

        unload_wait_list = data_unload['wait_time_unload_spot'].tolist()
        load_wait_list = data_load['wait_time_load_spot'].tolist()
        return n_data, unload_wait_list, load_wait_list


    def preprocess_model(unload_wait_list, lookback):
        X, y = [], []
        for i in range(len(unload_wait_list) - lookback):
            X.append(unload_wait_list[i:i+lookback])
            y.append(unload_wait_list[i+lookback])
        X = np.array(X)
        y = np.array(y)
        return X, y

    def make_model(n_data, unload_wait_list, load_wait_list, lookback):

        X, y = preprocess_model(unload_wait_list, lookback)
        previous_data = unload_wait_list[-30:]
        # LSTM 모델 구성
        model = keras.Sequential()
        model.add(keras.layers.LSTM(units=64, input_shape=(lookback, 1)))
        model.add(keras.layers.Dense(units=1))
        # 모델 컴파일
        model.compile(loss='mean_squared_error', optimizer='adam')
        # 모델 학습
        history = model.fit(X, y, epochs=200, batch_size=32)

        X_load, y_load = preprocess_model(load_wait_list, lookback)
        previous_data_load = load_wait_list[-30:]
        model_load = keras.Sequential()
        model_load.add(keras.layers.LSTM(units=64, input_shape=(lookback, 1)))
        model_load.add(keras.layers.Dense(units=1))
        model_load.compile(loss='mean_squared_error', optimizer='adam')
        model_load.fit(X_load, y_load, epochs=200, batch_size=32)

        # 이후 30개의 대기시간 예측
        last_sequence = unload_wait_list[-lookback:]  # 최근 30개의 대기시간 데이터를 가져옵니다.
        predicted_data_unload = []
        for _ in range(1):
            sequence = np.array(last_sequence)
            sequence = np.reshape(sequence, (1, lookback, 1))
            prediction = model.predict(sequence)[0][0]
            predicted_data_unload.append(prediction)
            last_sequence.append(prediction)
            last_sequence = last_sequence[1:]
        #print(predicted_data_unload)

        last_sequence_load = load_wait_list[-lookback:]
        predicted_data_load = []
        for _ in range(1):
            sequence = np.array(last_sequence_load)
            sequence = np.reshape(sequence, (1, lookback, 1))
            prediction = model_load.predict(sequence)[0][0]
            predicted_data_load.append(prediction)
            last_sequence_load.append(prediction)
            last_sequence_load = last_sequence_load[1:]

            # 학습 오차 출력
            print('Train Loss:', history.history['loss'][-1])

            # 모델 평가 (여기서는 학습 데이터를 다시 사용했지만, 실제로는 검증 데이터를 사용해야 합니다.)
            eval_loss = model.evaluate(X, y, verbose=0)
            print('Eval Loss:', eval_loss)
        #print(predicted_data_load)     

        # 데이터
        y_true_unload = y
        y_pred_unload = predicted_data_unload

        y_true_load = y_load
        y_pred_load = predicted_data_load

        # unload 데이터에 대한 그래프
        plt.figure(figsize=(12, 6))
        plt.plot(y_true_unload, label='Actual Unload Wait Time')
        plt.plot(y_pred_unload, label='Predicted Unload Wait Time')
        plt.title('Unload Wait Time: Actual vs Predicted')
        plt.xlabel('Time')
        plt.ylabel('Wait Time')
        plt.legend()
        plt.show()

        # 그래프로 예측 결과와 실제 데이터를 표현합니다.
        x_axis_previous = range(len(n_data)-30, len(n_data))  # 기존 데이터 중 마지막 30개의 인덱스
        x_axis_predicted = range(len(n_data), len(n_data) + 1)  # 이후 2개의 예측 데이터
        # 개수 오류 계속 났었음. ( x_axis_previous = previous_data 맞춰줘야 하고, x_axis_predicted = predicted_data 맞춰줘야 함)
        # plt.plot(x_axis_previous, previous_data, label='Previous_unload_spot')
        # plt.scatter(x_axis_predicted, predicted_data_unload, label='Predicted_unload', color='red')
        # plt.plot(x_axis_previous, previous_data_load, label='Previous_load_spot')
        # plt.scatter(x_axis_predicted, predicted_data_load, label='Predicted_load', color='green')    
        # plt.xlabel('Time')
        # plt.ylabel('Wait_Time')   
        # plt.ylim(0, 300)  # y축 범위 설정
        # plt.legend()
        # graph_image_filename = "test_graph.png"
        # plt.savefig(graph_image_filename)
        # print(f"그래프를 '{graph_image_filename}' 파일로 저장했습니다.")
        # plt.show()
        return predicted_data_unload, predicted_data_load

    data = load_data()
    n_data, unload_wait_list, load_wait_list = preprocessing_data(data)
    lookback = 70
    predicted_data_unload, predicted_data_load = make_model(n_data, unload_wait_list, load_wait_list, lookback)
    predicted_data_unload = [float(x) for x in predicted_data_unload]
    predicted_data_load = [float(x) for x in predicted_data_load]
    
    return predicted_data_unload, predicted_data_load


if __name__=='__main__':
    postdata()

  