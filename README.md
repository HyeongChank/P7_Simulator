## 실행방법.
- git에서 다운로드
- 환경구축(requirements 다운로드) : pip install -r requirements.txt
- FLASK 실행(src 폴더의 app.py 실행) 
- Post : http://10.125.121.220:5001/api/r_predict

## 진행상황.
- 실제 데이터 분석 및 전처리 중(05.24) : 열간 상관관계
- 상관관계 비교적 높은 열들을 학습하여 입차~작업완료시간 예측 모델 생성(randomForest)(05.25)
    - 시간별 예측시간 나옴(datetime에서 Unix timestamp으로 변환해서 모델 돌리고 datetime으로 변환)

- 입차~작업완료시간 학습 및 예측 모델 생성(lstm)(05.25)

- [src->Queue_LSTM.py](05.23) : 반입장, 반출장별 Queue 대기시간 예측

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
    - [src->app.py](flask서버) : 서버
    - 반입, 반출장 각각 5개 블록 총 10개 객체 설정해서 Queue
    
## Todo
- 트럭 대기시간에 영향 끼치는 요소 예측 모델에 추가(선박 입출항 여부)
- LSTM 모델말고 다른 적합한 모델 찾기
- Node.js 시뮬레이션 화면 출력 구현(블록별)
- 반입장, 반출장, 출구까지 이동 시간(초당 50프레임) 당 거리(픽셀) 계산해서 정확히 넣기(react)

## 세부내용
- 새로운 data RandomForest : http://10.125.121.220:5001/api/r_predict
    - 입력값 : 없음 / 출력값 : 10분 간격의 예측시간
- Queue_LSTM.py(05.23) 실행 : 'http://10.125.121.220:5001/api/predict'
    - 입력값 : 없음 / 출력값 : 5분 후 반입장, 반출장 예측 대기시간

- main.py 실행 : 'http://10.125.121.220:5001/api/congest2'
    - 입력예제 : {"입차시간": ["2021-02-07 22:30:37"],"작업코드": ["적하"]} 
    - 출력값 : {"congest_level": [2.0]}, {"waiting_time": 17.703699111938477}

------
<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/5ad11f0e-2cde-49e7-8fe0-5cda92f9bf12.gif"/>

<img width="200" src="https://github.com/HyeongChank/P7_Simulator/assets/122770625/6448b5f8-81ff-43ac-9c23-463cd9c26abe.png"/>