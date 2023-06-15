## 실행방법.
- Server 실행
	- MySQL 실행 및 Database(simulpredict) 생성
	- 스프링 PredictSimul 프로젝트 start
	- Flask app.py 실행
- 리액트 App.js 실행(npm start)
	- 입력값으로 차량수(대), 블록수, 총 실행시간(초) 작성 및 start 버튼 클릭

## 내용
- 입력값을 바탕으로 컨테이너 야드 내 시뮬레이션 구성 및 딥러닝을 통한 향후 차량 수 예측
- Simulator : simpy 사용
- 딥러닝
	- CNN(합성곱 신경망)모델
		- 작업+대기시간 예측 : http://10.125.121.220:5001/api/cnn_time_predict
		- 작업+대기차량 수 예측 : http://10.125.121.220:5001/api/cnn_count_predict
	- RNN 중 lstm (순환신경망)모델 : http://10.125.121.220:5001/api/lstm_predict
- 머신러닝(비교)
	- randomforest 모델 : http://10.125.121.220:5001/api/r_predict 

------
<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/7074be29-84d9-4b16-8526-a5448c99bc81.gif"/>

<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/5ad11f0e-2cde-49e7-8fe0-5cda92f9bf12.gif"/>

<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/6448b5f8-81ff-43ac-9c23-463cd9c26abe.png"/>


pip freeze > requirements.txt


<<<<<<< HEAD
 input_shape 는 (시퀀스의 길이(시간 스텝의 수), 특성의 수)가 들어가야 함
    model.add(keras.layers.LSTM(units=64, input_shape=(X_train.shape[1], X_train.shape[2])))

# 시간 순서를 유지하면서 데이터 분할(분할할 때, X_train, y_train 값 같게 분할 해야하고 차원
# 신경 써야 함)
X_train, X_test = X[:train_size, :, :], X[train_size:, :, :]
y_train, y_test = y[:train_size, :], y[train_size:, :]


## 실행방법 내부
- simulator 데이터 생성 및 예측
	- simulator_post.py 실행 시 아래 단계에 따라 실행됨
		- simulator_optimizer.make_simul_data()
		- simulator_sort2.operate()
		- simulator_predict.operate()

<!-- - 플라스크 켜고, 스프링 서버 켜고 postman으로 post, http://localhost:8081/api/simul_predict,
	- json  	{
	    "json_output": [
	        {
	            "arrive_load_spot": "0",
	            "arrive_unload_spot": "22",
	            "code": "unload",
	            "complete_load_work": "0",
	            "complete_unload_work": "34",
	            "entryTime": "17",
	            "entry_count": "5",
	            "exit_count": "1",
	            "load_block": "X",
	            "load_count": "0",
	            "load_progress_truck_count": "0",
	            "number": "5",
                "prediction":"10",
                "realdata":"10",
	            "op": "unload",
	            "out_time": "39",
	            "spot_wait_time": "0",
	            "start_load_work": "0",
	            "start_unload_work": "22",
	            "unload_block": "B",
	            "unload_count": "0",
	            "unload_progress_truck_count": "0",
	            "visible": "True",
	            "work_time": "22"
	        }
	    ]
	}

	- 전송
	- db 들어왔는지 확인
	- 리액트 npm start
	- 화면 확인  -->
=======
>>>>>>> cb3e62e1df39456fef22b3c6b668fcfe9ba640cf
