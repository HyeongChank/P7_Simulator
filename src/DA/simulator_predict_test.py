import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from tensorflow import keras
from scipy.interpolate import interp1d
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras import backend as K
import pickle
from sklearn.model_selection import train_test_split
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# data load
def operate():

    def load():
        # new_data 들어오면 기존 df 에 합치면 됨
        data = pd.read_csv("./data/sorted_truck_simulation_results.csv", encoding='cp949')
        print(data)
        print(data['in_yard_count'])
        return data
        
    def preprocessing(data): 
        print(data[['entryTime', 'work_time', 'spot_wait_time', 'entry_count', 'exit_count', 'op', 'in_yard_count']])
        data['op'] = data['op'].replace({'unload':1, 'load':2, 'both':3})
        return data


 
    def make_model(df_in_model):
        # 데이터 전처리
        X_data = df_in_model[['entryTime', 'work_time', 'spot_wait_time', 'in_yard_count', 'op']]
        y_data = df_in_model['in_yard_count'].values
        print(df_in_model.shape[0])
        print(len(X_data['entryTime']))
        print(len(y_data))
        # lookback 없이 모든 데이터를 학습하기 위해 reshape
        X = np.reshape(X_data.values, (X_data.shape[0], 1, X_data.shape[1]))
        y = np.reshape(y_data, (y_data.shape[0], 1))

        # 시계열이라 데이터를 랜덤하게 분할하지 않고 시간대에 따라 분할
        train_size = int(len(X_data) * 0.8)
        print(train_size)
        # 시간 순서를 유지하면서 데이터 분할(분할할 때, X_train, y_train 값 같게 분할 해야하고 차원
        # 신경 써야 함)
        X_train, X_test = X[:train_size, :, :], X[train_size:, :, :]
        y_train, y_test = y[:train_size, :], y[train_size:, :]

        print(X_train.shape)  # 값 (320, 1, 6)
        print(y_train.shape)  # 값 (320, 1)
        # 데이터 정규화
        scaler = MinMaxScaler()
        # 같은 형태의 배열을 만들되, 모든 값을 비움
        X_train_scaled = np.zeros_like(X_train)
        X_test_scaled = np.zeros_like(X_test)
        # 특성(열) 개수만큼 for문 돌면서 scale 값 대입
        for i in range(X_train.shape[2]):
            X_train_scaled[:, :, i] = scaler.fit_transform(X_train[:, :, i])
            X_test_scaled[:, :, i] = scaler.transform(X_test[:, :, i])
        print("pass", X_train_scaled.shape)
        
        # y_train, y_test 스케일링
        scaler_y = MinMaxScaler()
        y_train_scaled = scaler_y.fit_transform(y_train)
        y_test_scaled = scaler_y.transform(y_test)
        print("pass", y_train_scaled.shape)
        # LSTM 모델 구성
        model = keras.Sequential()
        ## input_shape 는 (시퀀스의 길이(시간 스텝의 수), 특성의 수)가 들어가야 함
        model.add(keras.layers.LSTM(units=64, input_shape=(X_train.shape[1], X_train.shape[2])))
    
        model.add(keras.layers.Dense(units=1))

        # 모델 컴파일
        model.compile(loss='mean_squared_error', optimizer='adam')
        # 모델 학습
        model.fit(X_train_scaled, y_train_scaled, epochs=10, batch_size=32)
        # 모델 예측
        y_train_pred_scaled = model.predict(X_train_scaled)
        y_test_pred_scaled = model.predict(X_test_scaled)
        # 예측값을 원래의 스케일로 되돌리기
        y_train_pred = scaler_y.inverse_transform(y_train_pred_scaled)
        y_test_pred = scaler_y.inverse_transform(y_test_pred_scaled)
        # 원래의 스케일로 되돌린 실제값
        y_train_real = scaler_y.inverse_transform(y_train_scaled)
        y_test_real = scaler_y.inverse_transform(y_test_scaled)
        time_index = 0
        # '입차시간' 데이터 추출
        X_train_time = X_train[:, -1:, time_index].reshape(-1)
        X_test_time = X_test[:, -1:, time_index].reshape(-1)
    

        combined_time = np.concatenate((X_train_time, X_test_time), axis=0)
        print(combined_time)
        print(len(combined_time))
        combined_pred = np.concatenate((y_train_pred, y_test_pred), axis=0)
        print(combined_pred)
        print(len(combined_pred))
        combined_real = np.concatenate((y_train_real, y_test_real), axis=0)
        print(combined_real)
        print(len(combined_real))
        df_in_model['pred_count'] = combined_pred
        print(df_in_model)
    #     # datetime 형식을 리스트로 바꾸면 유닉스타임 스탬프로 변경돼서 다른 방법 써야 함
    # #     # time = combined_time.tolist()
    #     datetime_list = combined_time.tolist()
    #     actual_values = combined_real.tolist()
    #     predict_values = combined_pred.tolist()
    # #     print('time', datetime_list)
    # #     print(len(datetime_list))
    # #     print('actual_values',actual_values)
    # #     print(len(actual_values))
    # #     print('predict_values',predict_values)

    #     # Mean Absolute Error (MAE)
    #     mae_train = mean_absolute_error(y_train_real, y_train_pred)
    #     mae_test = mean_absolute_error(y_test_real, y_test_pred)

    #     print(f'Train MAE: {mae_train}, Test MAE: {mae_test}')

    #     # Mean Squared Error (MSE)
    #     mse_train = mean_squared_error(y_train_real, y_train_pred)
    #     mse_test = mean_squared_error(y_test_real, y_test_pred)

    #     print(f'Train MSE: {mse_train}, Test MSE: {mse_test}')

    #     # Root Mean Squared Error (RMSE)
    #     rmse_train = np.sqrt(mse_train)
    #     rmse_test = np.sqrt(mse_test)

    #     print(f'Train RMSE: {rmse_train}, Test RMSE: {rmse_test}')

    #     # R^2 Score
    #     r2_train = r2_score(y_train_real, y_train_pred)
    #     r2_test = r2_score(y_test_real, y_test_pred)

    #     print(f'Train R^2: {r2_train}, Test R^2: {r2_test}')

    #     # 그래프의 크기 설정
    #     plt.figure(figsize=(14, 7))
    #     plt.scatter(datetime_list, actual_values, color='blue', label='Actual values')
    #     plt.scatter(datetime_list, predict_values, color='red', label='Predicted values')
    #     plt.xlabel('Time')
    #     plt.ylabel('Values')
    #     plt.title('Scatter plot of actual and predicted values over time')
    #     plt.legend()
    #     graph_image_filename = "simul_graph.png"
    #     plt.savefig(graph_image_filename)
    #     print(f"그래프를 '{graph_image_filename}' 파일로 저장했습니다.")
    #     # plt.show()
  
    #     # 모델 저장
    #     with open('./models/simul_model.pkl', 'wb') as f:
    #         pickle.dump(model, f)
    #     # return X_test_time_original, y_train_pred, y_test_pred
        
       
    
    data = load()
    df_in_model = preprocessing(data)
    make_model(df_in_model)    


    # return X_test_time_original, y_train_pred, y_test_pred

if __name__=='__main__':
    operate()
