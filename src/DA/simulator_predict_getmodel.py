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
from datetime import datetime
import seaborn as sns
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
        data['container_status'] =data['container_status'].replace({'fresh':1, 'short-term':2, 'long-term':3})
        data['container_size'] = data['container_size'].replace({'small':1, 'medium':2, 'large':3})
        data['unload_block'] = data['unload_block'].replace({'A':1, 'B':2,'C':3, 'D':4, 'E':5})
        data['load_block'] = data['load_block'].replace({'Q':1, 'W':2,'X':3, 'Y':4, 'Z':5})
        return data


    # 데이터 전처리
    def make_model(df_in_model):
        lookback = 50
        # 데이터 전처리
        X_data = df_in_model[['work_time', 'spot_wait_time', 'op', 'container_status', 'container_size','unload_block', 'load_block']]
        y_data = df_in_model['in_yard_count'].values
        #print(y_data)
        # 상관관계 히트맵 그리기
        correlation_matrix = df_in_model[['work_time', 'spot_wait_time', 'op', 'container_status', 'container_size','unload_block', 'load_block', 'in_yard_count']].corr()

        sns.heatmap(correlation_matrix, annot=True)
        plt.tight_layout()
        graph_image_filename = "corelate_simul_graph.png"
        plt.savefig(graph_image_filename)
        print(f"그래프를 '{graph_image_filename}' 파일로 저장했습니다.")
        plt.show()
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

         # 모델 로드
        with open('models/lstm_simul_model.pkl', 'rb') as f:
            model = pickle.load(f)
        # 모델 예측
        y_train_pred_scaled = model.predict(X_train)
        y_test_pred_scaled = model.predict(X_test)
            # Mean Absolute Error (MAE)
        mae_train = mean_absolute_error(y_train, y_train_pred_scaled)
        mae_test = mean_absolute_error(y_test, y_test_pred_scaled)

        print(f'Train MAE: {mae_train}, Test MAE: {mae_test}')

        # Mean Squared Error (MSE)
        mse_train = mean_squared_error(y_train, y_train_pred_scaled)
        mse_test = mean_squared_error(y_test, y_test_pred_scaled)

        print(f'Train MSE: {mse_train}, Test MSE: {mse_test}')

        # Root Mean Squared Error (RMSE)
        rmse_train = np.sqrt(mse_train)
        rmse_test = np.sqrt(mse_test)

        print(f'Train RMSE: {rmse_train}, Test RMSE: {rmse_test}')

        # R^2 Score
        r2_train = r2_score(y_train, y_train_pred_scaled)
        r2_test = r2_score(y_test, y_test_pred_scaled)

        print(f'Train R^2: {r2_train}, Test R^2: {r2_test}')
        combined_pred = np.concatenate((y_train_pred_scaled, y_test_pred_scaled), axis=0)
        #print(combined_pred)
        #print(len(combined_pred))
        combined_real = np.concatenate((y_train, y_test), axis=0)
        #print(combined_real)
        #print(len(combined_real))
        # datetime 형식을 리스트로 바꾸면 유닉스타임 스탬프로 변경돼서 다른 방법 써야 함
    #     # time = combined_time.tolist()
        
        actual_values = combined_real.tolist()
        predict_values = combined_pred.tolist()
        new_list = predict_values.copy()

        ## 이중리스트 단일리스트로 변경하는 방법
        ### 개수 오류 나서 일정한 값으로 되어있던 것을 lookback으로 수정함
        new_list = [item for sublist in new_list for item in sublist]
        new_list = [0]*lookback + new_list
        #print('new_list', new_list)
        # new_list = [round(num) for num in new_list]
        new_list = [round(num,1) for num in new_list]

        ### 개수 오류 나서 일정한 값으로 되어있던 것을 lookback으로 수정함
        new_actual_list = data['in_yard_count'][:lookback].tolist()
        new_actual_list_r = new_actual_list + actual_values        
        print(len(new_list))
        print(len(new_actual_list_r))
       
        data['prediction'] = new_list


        data['realdata'] = new_actual_list_r
        data['op'] = data['op'].replace({1:'unload', 2:'load', 3:'both'})
        sorted_file_path = 'data/predict_truck_simulation_results.csv'
        data.to_csv(sorted_file_path, index=False)
        print("predict 저장됨")

   
        # x축으로 사용할 인덱스 생성
        # new_actual_list_r = new_actual_list_r[lookback:]
        # new_list = new_list[lookback:]
        new_actual_list_r = new_actual_list_r[-200:]
        new_list = new_list[-200:]
        index_list = range(len(new_actual_list_r))
        # 그래프의 크기 설정
        plt.figure(figsize=(14, 7))
        plt.scatter(index_list, new_actual_list_r, color='blue', label='Actual values')
        plt.scatter(index_list, new_list, color='red', label='Predicted values')
        plt.xlabel('Time')
        plt.ylabel('Values')
        plt.title('Scatter plot of actual and predicted values over time')
        plt.legend()
        graph_image_filename = "lstm_simul_graph.png"
        plt.savefig(graph_image_filename)
        print(f"그래프를 '{graph_image_filename}' 파일로 저장했습니다.")
        # plt.show()
  
        # 모델 저장
        with open('./models/lstm_simul_model.pkl', 'wb') as f:
            pickle.dump(model, f)
        # return X_test_time_original, y_train_pred, y_test_pred
        
       
    
    data = load()
    df_in_model = preprocessing(data)
    make_model(df_in_model)    


    # return X_test_time_original, y_train_pred, y_test_pred

if __name__=='__main__':
    operate()
