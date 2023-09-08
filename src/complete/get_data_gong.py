import requests
import pandas as pd
import schedule
import time


def get_data():
    servicekey = 'n10J1U3TXuzNqRQkALNyYk8YzRRN2g8s/z2kM7omSrzjBvLfPkim/g/Oi4fp+y1Qu6bDPnlpD0uw5tOlTyl3/A=='
    url = 'https://apis.data.go.kr/B551220/vsslWorkStatService/getVsslWorkStatList'
    params = {
        'serviceKey': servicekey,
        'pageNo': 1,
        'numOfRows': 200,
        'startDate': '20210101',
        'endDate': '20230530',
        'trminlCode': 'BNCT'
    }
    headers = {'Accept': 'application/json'}

    response = requests.get(url, params=params, headers=headers)

    results = []

    data = response.json()
    total_count = data['response']['body']['totalCount']
    total_pages = (total_count // params['numOfRows']) + (1 if total_count % params['numOfRows'] else 0)
        
    for page in range(1, total_pages +1):
        params['pageNo'] = page
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            items = data['response']['body']['items']['item']        
            for item in items:
                trminlCode = item['trminlCode']
                trminlShipnm = item['trminlShipnm']
                trminlVoyg= item['trminlVoyg']
                berthCode= item['berthCode']
                etryptYear= item['etryptYear']
                wtorcmpCode= item['wtorcmpCode']
                csdhpPrarnde= item['csdhpPrarnde']
                csdhpDate= item['csdhpDate']
                tkoffPrarnde= item['tkoffPrarnde']
                tkoffDate= item['tkoffDate']
                opertBeginDate= item['opertBeginDate']
                landngComptQy= item['landngComptQy']
                landngRemndrQy= item['landngRemndrQy']
                landngSmQy= item['landngSmQy']
                shipngComptQy= item['shipngComptQy']
                shipngRemndrQy= item['shipngRemndrQy']
                shipngSmQy= item['shipngSmQy']
                creatDate= item['creatDate']
                updtDate= item['updtDate']
                
                results.append((trminlCode, trminlShipnm, trminlVoyg, berthCode, etryptYear,
                                wtorcmpCode, csdhpPrarnde,csdhpDate,tkoffPrarnde,tkoffDate,opertBeginDate,
                                landngComptQy,landngRemndrQy,landngSmQy,shipngComptQy,shipngRemndrQy,shipngSmQy,
                                creatDate,updtDate))

        else:
            print(f"Request failed with status code {response.status_code}")

    return results, total_count, total_pages




    

if __name__=='__main__':

    data, total_count, total_pages = get_data()
    print(total_count)
    print(total_pages)
    columns = ['trminlCode(터미널코드)', 'trminlShipnm(모선명)', 'trminlVoyg(모선항차)', 'berthCode(선석코드)',
               'etryptYear(입항연도)', 'wtorcmpCode(선사)', 
            'csdhpPrarnde(접안예정일시)', 'csdhpDate(접안일시)', 'tkoffPrarnde', 'tkoffDate', 'opertBeginDate(작업시작일시)', 'landngComptQy(양하완료수량)', 
            'landngRemndrQy(양하잔여수량)', 'landngSmQy(양하합계수량)', 'shipngComptQy(적하완료수량)', 'shipngRemndrQy(적하잔여수량)', 'shipngSmQy(적하합계수량)', 'creatDate(생성일자)', 
            'updtDate']
    df = pd.DataFrame(data, columns=columns)

    # DataFrame을 엑셀 파일로 저장
    df.to_excel('data/data_output.xlsx', index=False)
    print("Data saved to 'data_output.xlsx'")
