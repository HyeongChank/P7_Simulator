import pandas as pd
# import xgboost as xgb
import numpy as np
# import datetime
# import numpy as np
# import matplotlib.pyplot as plt
from tensorflow import keras
from scipy.interpolate import interp1d
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras import backend as K
# import pickle
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# import matplotlib.pyplot as plt
# import seaborn as sns
# from datetime import datetime
import openpyxl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def operate():
    count = 1
    p_count = 15
    prediction_list = []
    # data load
    def load():
        data = pd.read_excel("data/test_data.xlsx", sheet_name='Sheet1')
        print(data.head())
        print(data['value'])
        data_list = data['value'].tolist()
        return data_list


    def make_model(data_list):
        data = data_list
        nonlocal prediction_list
        nonlocal count
        nonlocal p_count
        lookback = 200
        X, y = [], []
        for i in range(len(data) - lookback):
            X.append(data[i:i+lookback])
            y.append(data[i+lookback])
        X = np.array(X)
        y = np.array(y)
        previous_data = data[-200:]

        # LSTM 모델 구성
        model = keras.Sequential()
        model.add(keras.layers.LSTM(units=64, input_shape=(lookback, 1)))
        model.add(keras.layers.Dense(units=1))

        # 모델 컴파일
        model.compile(loss='mean_squared_error', optimizer='adam')

        # 모델 학습
        model.fit(X, y, epochs=20, batch_size=32)

        # 이후 30개의 대기시간 예측
        last_sequence = data[-lookback:]  # 최근 30개의 대기시간 데이터를 가져옵니다.
        predicted_data = []
        for _ in range(1):
            sequence = np.array(last_sequence)
            sequence = np.reshape(sequence, (1, lookback, 1))
            prediction = model.predict(sequence)[0][0]
            predicted_data.append(prediction)
            last_sequence.append(prediction)
            last_sequence = last_sequence[1:]
        print(predicted_data)
        prediction_list.append(predicted_data)


        # 그래프로 예측 결과와 실제 데이터를 표현합니다.
        x_axis_previous = range(len(data)-200, len(data))  # 기존 데이터 중 마지막 30개의 인덱스
        x_axis_predicted = range(len(data), len(data)+1)  # 이후 2개의 예측 데이터
        # 개수 오류 계속 났었음. ( x_axis_previous = previous_data 맞춰줘야 하고, x_axis_predicted = predicted_data 맞춰줘야 함)
        plt.plot(x_axis_previous, previous_data, label='Previous Data')
        plt.scatter(x_axis_predicted, predicted_data, label='Predicted Data', color='red')
        plt.xlabel('Time')
        plt.ylabel('Waiting Time')
        plt.ylim(0, 200)  # y축 범위 설정
        plt.legend()
        graph_image_filename = "test_graph.png"
        plt.savefig(graph_image_filename)
        print(f"그래프를 '{graph_image_filename}' 파일로 저장했습니다.")
        # plt.show()


        # 예측값을 data에 추가
        for predict_value in predicted_data:
            data.append(predict_value)
        print('count', count)
        
        # 입력 횟수만큼 예측값 학습한 값 출력(새로운 값 추가하여 재학습)
        if count < p_count:
            count+=1
            make_model(data)
        print(prediction_list)

    data_list = load()
    make_model(data_list)

if __name__=='__main__':

    data_list = operate()
    # combined_data = add_data(data, new_data)

    # # 대기시간을 list로 만듦
    # column_list = preprocessing(combined_data)
    