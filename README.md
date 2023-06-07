## 실행방법.
- git에서 다운로드
- 환경구축(requirements 다운로드) : pip install -r requirements.txt
- FLASK 실행(src 폴더의 app.py 실행) 
- cnn모델
    - 작업+대기시간 예측 : http://10.125.121.220:5001/api/cnn_time_predict
    - 작업+대기차량 수 예측 : http://10.125.121.220:5001/api/cnn_count_predict

- lstm모델 : http://10.125.121.220:5001/api/lstm_predict
- randomforest 모델 : http://10.125.121.220:5001/api/r_predict

## 내용
- cnn모델 요청 시 index_time(10분 단위), actual_time, predict_time 값 전송
    - 입력값 : 없음
- simulator 데이터 생성 : simulator_sort2.py
------
<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/7074be29-84d9-4b16-8526-a5448c99bc81.gif"/>

<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/5ad11f0e-2cde-49e7-8fe0-5cda92f9bf12.gif"/>

<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/6448b5f8-81ff-43ac-9c23-463cd9c26abe.png"/>


## Todo
- simul 서버 연결 해야 함 / 1. 플라스크에서 보내는 데이터를 db에 들어갈(스프링의 simul 객체) 데이터와 동일하게 만들어야 하고  2. 스프링에서 ResponseEntity<String> 로 받은 데이터를 list로 변환해야 함(플라스크로부터 바로 list로 받을 수 있는 방법이 있으면 가장 적합)  3. front 육면체 제대로 그려서 3개씩 만 하고 속도 계산 정확히 하기


pip freeze > requirements.txt