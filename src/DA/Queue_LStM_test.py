
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
        # 반입 작업 구분
        df_unload = df[df['code'].isin([1,3])]
        #print(df_unload)
        # 반출 작업 구분
        df_load = df[df['code'].isin([2,3])]
        df_unload_pre = df_unload[['unload_block','entryTime','wait_time_unload_spot', 'unload_count']]
        df_load_pre = df_load[['load_block','entryTime','wait_time_load_spot', 'load_count']]
        print(df_unload_pre)
        n_data = df_unload_pre.drop(['unload_block', 'unload_count'], axis=1, inplace=False)

        # 블록별 구분 작업
        block_data_df = df_unload_pre.drop(['unload_count'], axis=1, inplace=False)
        print(block_data_df)
        
        block1 = block_data_df[block_data_df['unload_block']==1]
        block2 = block_data_df[block_data_df['unload_block']==2]
        block3 = block_data_df[block_data_df['unload_block']==3]
        block4 = block_data_df[block_data_df['unload_block']==4]
        block5 = block_data_df[block_data_df['unload_block']==5]
        block1 = block1.reset_index(drop=True)
        block2 = block2.reset_index(drop=True)
        block3 = block3.reset_index(drop=True)
        block4 = block4.reset_index(drop=True)
        block5 = block5.reset_index(drop=True)
        print(block1)
        # print(block2)
        block_list_dic = []
        block_list_preprocessing = [n_data, block1, block2, block3, block4, block5]
        for ent in block_list_preprocessing:
            # index 새로 설정(0~)
            
            ent = ent.reset_index(drop=True)
            print(ent)

            # entryTime을 5분 단위로 그룹화
            bins = range(0, ent["entryTime"].max() + 5, 5)
            labels = range(5, ent["entryTime"].max() + 5, 5)
            ent['entryTime_group'] = pd.cut(ent["entryTime"], bins=bins, labels=labels, right=False)

            # 각 그룹의 wait_time_unload_spot 최대값 계산(평균은 mean으로 바꾸면 됨)
            ent = ent.groupby("entryTime_group")["wait_time_unload_spot"].max().reset_index()

            # na값 평균으로 채우기
            ent['wait_time_unload_spot'] = ent['wait_time_unload_spot'].fillna(ent['wait_time_unload_spot'].mean())
            na_count = ent.isna().sum()

            print(ent)
            block_list_dic.append(ent)
        n_data, block1, block2, block3, block4, block5 = block_list_dic














        # index 새로 설정(0~)
        n_data = n_data.reset_index(drop=True)
        print(n_data)

        # entryTime을 5분 단위로 그룹화
        bins = range(0, n_data["entryTime"].max() + 5, 5)
        labels = range(5, n_data["entryTime"].max() + 5, 5)
        n_data['entryTime_group'] = pd.cut(n_data["entryTime"], bins=bins, labels=labels, right=False)

        # 각 그룹의 wait_time_unload_spot 최대값 계산(평균은 mean으로 바꾸면 됨)
        n_data = n_data.groupby("entryTime_group")["wait_time_unload_spot"].max().reset_index()
        # na 값 0으로 채우기
        # grouped['wait_time_unload_spot'] = grouped['wait_time_unload_spot'].fillna(0)
        na_count = n_data.isna().sum()
        print(na_count)
        # na값 평균으로 채우기
        n_data['wait_time_unload_spot'] = n_data['wait_time_unload_spot'].fillna(n_data['wait_time_unload_spot'].mean())
        na_count = n_data.isna().sum()
        print(na_count)
        print(n_data)
        # for col in ['unload_block','entryTime', 'wait_time_unload_spot', 'unload_count']:
        #     df_unload_pre[col] = pd.to_numeric(df_unload_pre[col], errors='coerce')
        # for col in ['load_block','entryTime', 'wait_time_load_spot', 'load_count']:    
        #     df_load_pre[col] = pd.to_numeric(df_load_pre[col], errors='coerce')
        
        # data_unload = df_unload_pre.copy()
        # data_load = df_load_pre.copy()
        # data_unload_new = data_unload[['entryTime', 'wait_time_load_spot']]
        # print('data_unload_new', data_unload_new)

        return n_data, block1, block2, block3, block4, block5


    def make_model(df_list):
        n_data = df_list[0]

        data = n_data['wait_time_unload_spot'].values.reshape(-1, 1)
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(data)

        # 시계열 데이터 준비
        window_size = 10  # 입력 시퀀스의 길이
        X = []
        y = []
        for i in range(len(scaled_data) - window_size):
            X.append(scaled_data[i:i+window_size])
            y.append(scaled_data[i+window_size])
        X = np.array(X)
        y = np.array(y)

        # 데이터셋 분할
        train_size = int(len(X) * 0.8)
        X_train, X_test = X[:train_size], X[train_size:]
        y_train, y_test = y[:train_size], y[train_size:]

        # LSTM 모델 구성
        model = Sequential()
        model.add(LSTM(units=64, activation='relu', input_shape=(window_size, 1)))
        model.add(Dense(units=1))
        model.compile(optimizer='adam', loss='mean_squared_error')

        # 모델 학습
        model.fit(X_train, y_train, epochs=100, batch_size=32)

        # 예측 수행
        y_pred = model.predict(X_test)

        # 예측 결과 역스케일링
        y_test = scaler.inverse_transform(y_test)
        y_pred = scaler.inverse_transform(y_pred)
        # 오차 계산

        print("NaN in y_test: ", np.isnan(y_test).any())
        print("NaN in y_pred: ", np.isnan(y_pred).any())
        print("y_test dtype: ", y_test.dtype)
        print("y_pred dtype: ", y_pred.dtype)


        error = y_test - y_pred
        mae = np.mean(np.abs(error))

        print("Error: \n", error)
        print("Mean Absolute Error: ", mae)
    
        
        # 그래프 출력
        plt.figure(figsize=(14,5))
        plt.scatter(n_data['entryTime_group'], n_data['wait_time_unload_spot'], color='blue', label='Actual')
        plt.scatter(n_data['entryTime_group'][train_size+window_size:], y_pred.flatten(), color='red', label='Predicted')  
        plt.title('Wait Time Prediction')
        plt.xlabel('Entry Time')
        plt.ylabel('Wait Time')
        plt.legend()
        graph_image_filename = "images/queue_graph.png"
        plt.savefig(graph_image_filename)
        print(f"그래프를 '{graph_image_filename}' 파일로 저장했습니다.")
        # plt.show()


    data = load_data()
    data_unload, block1, block2, block3, block4, block5 = preprocessing_data(data)
    df_list = [data_unload, block1, block2, block3, block4, block5]
    make_model(df_list)

if __name__=='__main__':
    postdata()