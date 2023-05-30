## 실행방법.
- git에서 다운로드
- 환경구축(requirements 다운로드) : pip install -r requirements.txt
- FLASK 실행(src 폴더의 app.py 실행) 
- cnn모델 : http://10.125.121.220:5001/api/cnn_predict
- randomforest 모델 : http://10.125.121.220:5001/api/r_predict

## 내용
- cnn모델 요청 시 index_time(10분 단위), actual_time, predict_time 값 전송
    - 입력값 : 없음

------
<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/7074be29-84d9-4b16-8526-a5448c99bc81.gif"/>

<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/5ad11f0e-2cde-49e7-8fe0-5cda92f9bf12.gif"/>

<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/6448b5f8-81ff-43ac-9c23-463cd9c26abe.png"/>