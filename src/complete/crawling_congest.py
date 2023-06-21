import requests
import pandas as pd
import schedule
import time


def get_data():
    # global trminlCode
    # global vesselStatusStr
    # global vesselStatus
    # global inoutStatusStr
    # global inoutStatus
    # global updtData


    servicekey = 'n10J1U3TXuzNqRQkALNyYk8YzRRN2g8s/z2kM7omSrzjBvLfPkim/g/Oi4fp+y1Qu6bDPnlpD0uw5tOlTyl3/A=='
    url = 'https://apis.data.go.kr/B551220/tmlCongestionStatService/getTmlCongestionStatList'
    params = {
        'serviceKey': servicekey,
        'pageNo': 1,
        'numOfRows': 50,
        'trminlCode': 'BNCT'
        }
    ## json, xml 두 형식을 모두 지원할 경우, json으로 받겠다고 headers 에 넣어서 요청해야 함
    headers = {'Accept': 'application/json'}

    response = requests.get(url, params=params, headers=headers)

    # 요청이 성공적인 경우
    if response.status_code == 200:
        data = response.json() # 응답을 JSON으로 변환합니다.
        print(data) # 출력합니다.
        print(data['response']['body']['items']['item'][0]['vesselStatusStr'])
        trminlCode = data['response']['body']['items']['item'][0]['trminlCode']
        vesselStatusStr =data['response']['body']['items']['item'][0]['vesselStatusStr']
        vesselStatus =data['response']['body']['items']['item'][0]['vesselStatus']
        inoutStatusStr = data['response']['body']['items']['item'][0]['inoutStatusStr']
        inoutStatus = data['response']['body']['items']['item'][0]['inoutStatus']
        updtDate = data['response']['body']['items']['item'][0]['updtDate']
    else:
        print(f"Request failed with status code {response.status_code}")
    return trminlCode, vesselStatusStr, vesselStatus, inoutStatusStr, inoutStatus, updtDate



    

if __name__=='__main__':

    schedule.every(1).minutes.do(get_data)
    while True:
        schedule.run_pending()
        time.sleep(1)


