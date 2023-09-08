import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from tensorflow import keras
import csv
from scipy.interpolate import interp1d
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.model_selection import train_test_split
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
        data['container_status'] =data['container_status'].replace({'fresh':1, 'short-term':2, 'long-term':3})
        data['container_size'] = data['container_size'].replace({'small':1, 'medium':2, 'large':3})
        return data


    # 데이터 전처리
    def make_model(df_in_model):
       
        # 데이터 전처리
        X_data = df_in_model[['work_time', 'spot_wait_time', 'op', 'container_status', 'container_size']]
        y_data = df_in_model['in_yard_count'].values

        # 데이터 랜덤하게 분할
        X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)

        # 랜덤 포레스트 모델 생성
        model = RandomForestRegressor(n_estimators=300, max_depth=10, min_samples_split=2, min_samples_leaf=1, max_features='auto')

        # 모델 학습
        model.fit(X_train, y_train)

        # 모델 예측
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
       
        # 성능 평가
        rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
        r2_train = r2_score(y_train, y_train_pred)

        rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
        r2_test = r2_score(y_test, y_test_pred)

        print('Train RMSE: ', rmse_train)
        print('Train R-squared: ', r2_train)
        print('Test RMSE: ', rmse_test)
        print('Test R-squared: ', r2_test)   
        combined_pred = np.concatenate((y_train_pred, y_test_pred), axis=0)
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

    
        data['prediction'] = new_list


        data['realdata'] = actual_values
        data['op'] = data['op'].replace({1:'unload', 2:'load', 3:'both'})
        sorted_file_path = 'data/rfpredict_truck_simulation_results.csv'
        data.to_csv(sorted_file_path, index=False)
        print("predict 저장됨")


        index_list = range(len(actual_values))
        index_list = index_list[-200:]
        actual_values = actual_values[-200:]
        predict_values = predict_values[-200:]
        # 그래프의 크기 설정
        plt.figure(figsize=(14, 7))
        plt.plot(index_list, actual_values, color='blue', label='Actual values')
        plt.plot(index_list, predict_values, color='red', label='Predicted values')
        plt.xlabel('Time')
        plt.ylabel('Values')
        plt.title('plot of actual and predicted values over time')
        plt.legend()
        graph_image_filename = "rfsimul_graph.png"
        plt.savefig(graph_image_filename)
        print(f"그래프를 '{graph_image_filename}' 파일로 저장했습니다.")
        plt.show()
  
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
