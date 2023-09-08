import requests
import pandas as pd
import csv
from xml.etree import ElementTree as ET


##servicekey = 'n10J1U3TXuzNqRQkALNyYk8YzRRN2g8s/z2kM7omSrzjBvLfPkim/g/Oi4fp+y1Qu6bDPnlpD0uw5tOlTyl3/A=='
url = 'https://www.upa.or.kr/data/portal/openapi/frgt031'

params = {

    'G_IN_OUT_NM': '출항',
    # 'CTRY_CODE_NM': '베트남'
}
## json, xml 두 형식을 모두 지원할 경우, json으로 받겠다고 headers 에 넣어서 요청해야 함
headers = {'Accept': 'application/xml'}

response = requests.get(url, params=params, headers=headers)

# 요청이 성공적인 경우
if response.status_code == 200:
    data = response.content # 응답을 JSON으로 변환합니다.
    print(data) # 출력합니다.
else:
    print(f"Request failed with status code {response.status_code}")

# XML 데이터 파싱
root = ET.fromstring(response.content)

# XML 데이터에서 필요한 정보를 추출
# 여기서는 모든 태그의 텍스트를 추출
data = []
for elem in root.iter():
    data.append([elem.tag, elem.text])

# CSV 파일로 저장
with open('data/APIXML.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
