## 실행방법.
- Server 실행
	- MySQL 실행 -> import Database(simulpredict.sql 파일)
	- 스프링 PredictSimul 프로젝트 start
	- src -> Flask app.py 실행
- 리액트 App.js 실행
	- npm install -> npm start
	- 웹페이지에서 입력값으로 차량수(대), 블록수, 총 실행시간(초) 작성 및 start 버튼 클릭

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


