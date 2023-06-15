import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from tensorflow import keras
import csv
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
        data = pd.read_csv("data/sorted_truck_simulation_results.csv", encoding='cp949')
        return data
        
    def preprocessing(data): 
        #print(data[['entryTime', 'work_time', 'spot_wait_time', 'entry_count', 'exit_count', 'op']])
        data['op'] = data['op'].replace({'unload':1, 'load':2, 'both':3})
        return data


    # 데이터 전처리
    def make_model(df_in_model):
        lookback = 10
        # 데이터 전처리
        X_data = df_in_model[['work_time', 'spot_wait_time', 'op']]
        y_data = df_in_model['in_yard_count'].values
        #print(y_data)

        X, y = [], []
        for i in range(df_in_model.shape[0] - lookback):
            X.append(X_data[i:i+lookback].values)
            y.append(y_data[i+lookback])
        X = np.array(X)
        y = np.array(y)

        # 시계열이라 데이터를 랜덤하게 분할하지 않고 시간대에 따라 분할
        train_size = int(len(X) * 0.8)

        # 시간 순서를 유지하면서 데이터 분할
        X_train, X_test = X[:train_size, :], X[train_size:, :]
        y_train, y_test = y[:train_size], y[train_size:]

        # print(X_train.shape)
        # print(y_train.shape)
        # 데이터 정규화
        scaler = MinMaxScaler()
        X_train_scaled = np.zeros_like(X_train)
        X_test_scaled = np.zeros_like(X_test)

        for i in range(X_train.shape[2]):
            X_train_scaled[:, :, i] = scaler.fit_transform(X_train[:, :, i])
            X_test_scaled[:, :, i] = scaler.transform(X_test[:, :, i])

        # # y_train, y_test 스케일링
        # scaler_y = MinMaxScaler()
        # y_train_scaled = scaler_y.fit_transform(y_train)
        # y_test_scaled = scaler_y.transform(y_test)

        # LSTM 모델 구성
        model = keras.Sequential()
        model.add(keras.layers.LSTM(units=64, input_shape=(lookback, X_train.shape[-1])))
        model.add(keras.layers.Dense(units=64, activation='relu'))
        model.add(keras.layers.Dense(units=32, activation='relu'))
        model.add(keras.layers.Dense(units=1))

        # 모델 컴파일
        model.compile(loss='mean_squared_error', optimizer='adam')
        # 모델 학습
        model.fit(X_train, y_train, epochs=100, batch_size=32)
        # 모델 예측
        y_train_pred_scaled = model.predict(X_train)
        y_test_pred_scaled = model.predict(X_test)
        # print(y_train_pred_scaled)
        # print(y_test_pred_scaled)
    #     # 예측값을 원래의 스케일로 되돌리기
    #     y_train_pred = scaler_y.inverse_transform(y_train_pred_scaled)
    #     y_test_pred = scaler_y.inverse_transform(y_test_pred_scaled)
    #     # 원래의 스케일로 되돌린 실제값
    #     y_train_real = scaler_y.inverse_transform(y_train_scaled)
    #     y_test_real = scaler_y.inverse_transform(y_test_scaled)
   
        combined_pred = np.concatenate((y_train_pred_scaled, y_test_pred_scaled), axis=0)
        #print(combined_pred)
        #print(len(combined_pred))
        combined_real = np.concatenate((y_train, y_test), axis=0)
        #print(combined_real)
        #print(len(combined_real))
    #     # datetime 형식을 리스트로 바꾸면 유닉스타임 스탬프로 변경돼서 다른 방법 써야 함
    # #     # time = combined_time.tolist()
    #     datetime_list = combined_time.tolist()
        actual_values = combined_real.tolist()
        predict_values = combined_pred.tolist()
        print(predict_values)
        new_list = predict_values.copy()
        ## 이중리스트 단일리스트로 변경하는 방법
        new_list = [item for sublist in new_list for item in sublist]
        new_list = [0]*10 + new_list
        #print('new_list', new_list)
        new_list = [round(num) for num in new_list]

        new_actual_list = data['in_yard_count'][:10].tolist()
        new_actual_list_r = new_actual_list + actual_values        
        # print(len(new_list))
        # print(len(new_actual_list_r))
        
        data['prediction'] = new_list

        data['realdata'] = new_actual_list_r
        data['op'] = data['op'].replace({1:'unload', 2:'load', 3:'both'})
        sorted_file_path = 'data/predict_truck_simulation_results.csv'
        data.to_csv(sorted_file_path, index=False)
        print("predict 저장됨")

            
        
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
