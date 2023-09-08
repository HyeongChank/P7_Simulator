import requests
import pandas as pd

servicekey = 'n10J1U3TXuzNqRQkALNyYk8YzRRN2g8s/z2kM7omSrzjBvLfPkim/g/Oi4fp+y1Qu6bDPnlpD0uw5tOlTyl3/A=='
url = 'http://apis.data.go.kr/B551220/vsslWorkStatService/getVsslWorkStatList'


for page in range(1,11):
    params = {
        'serviceKey': servicekey,
        'numOfRows': 50,
        'pageNo': page,
        'startDate': 20220607,
        'endDate': 20220711,
    }
## json, xml 두 형식을 모두 지원할 경우, json으로 받겠다고 headers 에 넣어서 요청해야 함
headers = {'Accept': 'application/json'}

response = requests.get(url, params=params, headers=headers)

# 요청이 성공적인 경우
if response.status_code == 200:
    data = response.json() # 응답을 JSON으로 변환합니다.
    print(data) # 출력합니다.
else:
    print(f"Request failed with status code {response.status_code}")

df = pd.DataFrame(data)
df.to_csv('data/APIdata.csv', index=False)
print("APIdata.csv 저장되었씁니다.")

