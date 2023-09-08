from datetime import datetime
import pandas as pd

date_string = "20230323082354"
datetime_object = datetime.strptime(date_string, "%Y%m%d%H%M%S")
print(datetime_object)

data = pd.read_excel("data/TBS_data.xlsx", sheet_name='야드크레이인_작업이력')
print(data.head())

print(data.shape)
print(data.info())

n_data = data[['작업코드','블록','야드트럭(번호)','작업생성시간','작업완료시간']]
print(n_data)
print(n_data.isna().sum())
n_data['야드트럭(번호)'] = n_data['야드트럭(번호)'].fillna(1)
print(n_data.isna().sum())
n_data_dropna = n_data.dropna()
print('n_data_dropna',n_data_dropna)
print(n_data_dropna.isna().sum())


print('uinque',n_data_dropna['작업생성시간'].unique())
print('uinque',n_data_dropna['작업완료시간'].unique())
# 텍스트를 날짜 형식으로 변환
def convert_to_datetime(date_value):
    date_string = str(int(date_value))
    datetime_object = datetime.strptime(date_string, "%Y%m%d%H%M%S")
    return datetime_object

# # 모든 행에 함수 적용하여 날짜 형식으로 변환
n_data_dropna['작업생성시간'] = n_data_dropna['작업생성시간'].apply(convert_to_datetime)
n_data_dropna['작업완료시간'] = n_data_dropna['작업완료시간'].apply(convert_to_datetime)
# 작업생성시간 기준으로 오름차순
n_data_dropna = n_data_dropna.sort_values(by='작업생성시간', ascending=True)

# 블록별 구분
blocks = n_data_dropna['블록'].unique()
print(blocks)
print(len(blocks))
print(n_data_dropna)
block_group = n_data_dropna.groupby('블록')
# 블록별 명, 데이터 저장
block_data = {}
for block, group in block_group:
    block_data[block] = group.copy()

for block in blocks:
    block_df = block_data[block]

print(block_data)

for block in block_data:
    preprocessing_data = n_data_dropna
    preprocessing_data['대기시간'] = preprocessing_data['작업생성시간'] - preprocessing_data['작업생성시간'].shift(1)
    print(preprocessing_data[['작업생성시간','대기시간']])
    preprocessing_data['작업시간'] = n_data_dropna['작업완료시간']-n_data_dropna['작업생성시간']
    print(preprocessing_data['작업시간'])



