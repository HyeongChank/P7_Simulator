## 프로젝트 개요
- 프로젝트명 : 컨테이너 야드 혼잡도 분석 및 대기시간 예측 웹서비스 개발
- 대&nbsp;&nbsp;&nbsp;&nbsp;상 : 컨테이너 야드 운송사
- 내&nbsp;&nbsp;&nbsp;&nbsp;용 : 이 프로젝트는 실제 부산항, 인천항의 데이터를 참고하여 컨테이너 야드 내 반출입 트럭의 대기열을 시뮬레이션하고, 해당 데이터를 분석하여 차량 대기에 영향을 미치는 요인을 찾습니다. 이를 기반으로 머신러닝, 딥러닝 모델을 개발하고 야드 내 혼잡도 및 대기차량 수를 예측합니다.

## 실행방법
- git에서 다운로드
- Front
  - Visual Studio Code(IDE) 실행 -> Front 이동
  - my-react-app 이동 -> node_modules 설치(npm install) -> React 실행(npm start)
- Server
  - Spring 실행 -> import 'PredictSimul' -> 서버 실행
- Data Analysis
  - 가상환경 : python -m venv venv .\venv\Scripts\activate
  - 환경구축(requirements 다운로드) : pip install -r requirements.txt
  - FLASK 실행(src 폴더의 app.py 실행)
  - 모델 예측값 출력(POST 방식)
    - 작업+대기시간 예측 : http://10.125.121.220:5001/api/cnn_time_predict
    - 작업+대기차량 수 예측 : http://10.125.121.220:5001/api/cnn_count_predict

## 현황
- chart 화면에 그리고, 입차시간에 맞게 재랜더링되는 것까지 완료
- 메인페이지, 시뮬페이지 구분(BrowserRouter로 Routes 무조건 감싸야 함)
- 현재는 truckcount 에 in_yard_count가 들어가고 있음. 예측치도 구해서 chart 페이지에 실제값, 예측값이 전달되고 그려지도록 해야 함
- 예측 모델을 써서 만들어야 함
- 애초에 데이터 db에 넣을 때 예측값 구해서 추가로 넣기
- main페이지 화면 구성
## Todo


## 