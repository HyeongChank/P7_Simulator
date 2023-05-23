## 진행상황.
- [yard_congestion->Queue_LSTM.py](05.23) : 반입장, 반출장별 Queue 대기시간 예측

- predict_LSTM.py : 향후 대기시간(5분 단위) 예측
    - 향후 예측시간(현재 기준 5분단위 개수) 입력 시 향후 대기시간s 출력

- main.py : 혼잡도 분석 및 Congest_level 출력
    - 예측 입차시기 입력 / 예측 대기시간 및 혼잡도 출력

- simulator 터미널 시뮬레이션 및 애니메이션 실행
    - 트럭 500대, 24시간 내 터미널 작업 시뮬레이션
    - 기능 : 입차, 배정 블록 이동, 작업(반입, 반출), 대기시간, 작업장별 대기차량 수, 출차
    - 목표
        - 터미널 소요시간, 반입, 반출 작업장별 대기차량, 대기시간 데이터 생성(완료 5/22)
        - 애니메이션 실행(완료)
    - simulator_now_test.py : 시뮬레이션 데이터 생성
    - simulator_sort_graph.py : 데이터 전처리
    - [Server->Simulator](spring서버) : 데이터 전달(mysql db 저장)
    - [front->my-react-app](node.js) : 터미널 화면 출력(트럭 이동 간이 구현)
    - [yard_congestion->app.py](flask서버) : 예측값 전달
    - 반입, 반출장 각각 5개 블록 총 10개 객체 설정해서 Queue
    
- randomForest.py : 현재 대기차량, 혼잡도 입력 시 대기시간 예측(+오차 측정)
- xgboost_test2.py : 야드 내 블록별 혼잡도 level 2 -> 1이 되는 데 걸리는 시간(+정확도 측정)
- Arima.py : 시간 입력 시 해당 시간의 야드 내 트럭 대수 분석

## Todo
- 트럭 대기시간에 영향 끼치는 요소 예측 모델에 추가(선박 입출항 여부)
- LSTM 모델말고 다른 적합한 모델 찾기
- Node.js 시뮬레이션 화면 출력 구현(블록별)
- 반입장까지 이동, 반출장까지 이동, 출구까지 이동 시간(초당 50프레임) 당 거리(픽셀) 계산해서 정확히 넣기(react)

## 세부내용
- Queue_LSTM.py(05.23) 실행 : 'http://10.125.121.220:5001/api/predict'
    - 입력값 : 없음
    - 출력값 : 5분 후 반입장, 반출장 예측 대기시간

- main.py 실행 : 'http://10.125.121.220:5001/api/congest2'
    - 입력예제 : {"입차시간": ["2021-02-07 22:30:37"],"작업코드": ["적하"]} 
    - 출력값 : {"congest_level": [2.0]}, {"waiting_time": 17.703699111938477}

------

<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/6448b5f8-81ff-43ac-9c23-463cd9c26abe.png"/>