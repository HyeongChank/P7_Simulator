from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
from matplotlib import font_manager, rc
# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


data = pd.read_excel("data/TBS_data.xlsx", sheet_name='야드크레이인_작업이력')
scd_data = pd.read_excel("data/TBS_data.xlsx", sheet_name='반출입_예정컨테이너')
container_before_data = pd.read_excel("data/TBS_data.xlsx", sheet_name='장치장_전')
container_after_data = pd.read_excel("data/TBS_data.xlsx", sheet_name='장치장_후')

# data, scd_data merge 전 확인
num_common_values = data['컨테이너번호'].isin(scd_data['컨테이너번호']).sum() # 1696개
print(num_common_values)

# data, container_before_data, container_after_data merge
ycb_common_values = data['컨테이너번호'].isin(container_after_data['컨테이너번호']).sum() # 6103개
print('ycb_common_values', ycb_common_values)
yard_con_common_df = pd.merge(data, container_after_data, on='컨테이너번호')

##################### 먼저 공통 값에 대한 merge ################
common_df = pd.merge(data, scd_data, on='컨테이너번호')
print('common_df',common_df)
common_df['작업코드'] = common_df['작업코드'].replace({'VU': 1, 'VL': 2, 'GR': 3, 'GD': 4, 'TM':5,'TS':6})
common_df = common_df[-500:]

#####################################################
n_data = data[['작업코드','블록','야드트럭(번호)','장비번호', '작업생성시간','작업완료시간']]
# print(n_data)
# print(n_data.isna().sum())
# 외부트럭에 1 넣기
n_data['야드트럭(번호)'] = n_data['야드트럭(번호)'].fillna(1)
# print('n_data', n_data)
n_data = n_data[-500:]
# print(n_data.isna().sum())
n_data_dropna = n_data.dropna()
# print('n_data_dropna',n_data_dropna)
# print(n_data_dropna.isna().sum())


# print('uinque',n_data_dropna['작업생성시간'].unique())
# print('uinque',n_data_dropna['작업완료시간'].unique())
# # 텍스트를 날짜 형식으로 변환
def convert_to_datetime(date_value):
    date_string = str(int(date_value))
    datetime_object = datetime.strptime(date_string, "%Y%m%d%H%M%S")
    # datetime 객체를 pandas Timestamp로 변환
    timestamp = pd.Timestamp(datetime_object)

    # pandas Timestamp를 float64 형태의 유닉스 시간으로 변환
    unix_time_float = timestamp.timestamp()
    return timestamp
def convert_to_datetime2(date_value):
    date_string = date_value
    # datetime 변환
    datetime_object = pd.to_datetime(date_string)
    # datetime 객체를 pandas Timestamp로 변환
    timestamp = pd.Timestamp(datetime_object)

    # pandas Timestamp를 float64 형태의 유닉스 시간으로 변환
    unix_time_float = timestamp.timestamp()

    return unix_time_float
def convert_unix_time_to_datetime(unix_time):
    # 유닉스 시간을 datetime 객체로 변환
    datetime_object = datetime.fromtimestamp(unix_time)
    return datetime_object

# print(type(common_df['시간']))
# print(type(common_df['작업생성시간']))
# print(common_df['시간'].dtypes)
# print(common_df['작업생성시간'].dtypes)

# # 모든 행에 함수 적용하여 날짜 형식으로 변환
# common_df.loc[:,'작업생성시간'] = common_df['작업생성시간'].apply(convert_to_datetime)
# common_df.loc[:,'작업완료시간'] = common_df['작업완료시간'].apply(convert_to_datetime)


common_df['작업생성시간'] = pd.to_datetime(common_df['작업생성시간'], format='%Y%m%d%H%M%S')
common_df['작업완료시간'] = pd.to_datetime(common_df['작업완료시간'], format='%Y%m%d%H%M%S')
print('작업생성시간',common_df['작업생성시간'].dtype)
print('작업완료시간',common_df['작업완료시간'].dtype)
print(common_df['작업완료시간'])
print('시간',common_df['시간'].dtype)
print(common_df['시간'])
# datetime64[ns] 타입의 03/23/2023 12:43:45로 변환
common_df['시간'] = pd.to_datetime(common_df['시간'], format='%m/%d/%Y %H:%M:%S')
# datetime 형태 일치
common_df['시간'] = common_df['시간'].dt.strftime('%Y-%m-%d %H:%M:%S')
print(common_df['시간'])
print('시간3',common_df['시간'].dtype)
common_df['시간'] = pd.to_datetime(common_df['시간'])
# common_df.loc[:,'시간'] = common_df['시간'].apply(convert_to_datetime2)
print('시간2',common_df['시간'].dtype)
print(common_df['시간'].isna().sum())
common_df['시간차이'] = common_df['작업생성시간'] - common_df['시간']
common_df['작업+대기시간'] = common_df['작업완료시간'] -common_df['작업생성시간']
# common_df['시간차이'] = common_df['시간차이'].apply(convert_unix_time_to_datetime)
# print(common_df['시간차이'].apply(type).unique())
# print(common_df['시간차이'].isna().sum())
print(common_df[['작업코드','항차_x','야드트럭(번호)','컨테이너(사이즈 코드)','장비번호', '작업생성시간','작업완료시간']])

correlation_matrix = common_df[['작업코드','항차_x','야드트럭(번호)','컨테이너(사이즈 코드)','장비번호', '작업생성시간','작업완료시간','작업+대기시간','시간']].corr()

sns.heatmap(correlation_matrix, annot=True)
plt.show()


# # '시간차이'을 분 단위로 변환
# # '시간차이'를 timedelta로 변환
# print(common_df['시간차이'].dtype)

# common_df['시간차이'] = pd.to_timedelta(common_df['시간차이'])
# # 이제 .dt accessor를 사용하여 분으로 변환 가능
# common_df['시간차이_분'] = common_df['시간차이'].dt.total_seconds() / 60

# # # '시간차이_분'을 y축으로 하는 선 그래프 그리기
# # common_df['시간차이_분'].plot(kind='line')
# # plt.ylabel('시간차이 (분)')
# # plt.show()



# # 작업생성시간 기준으로 오름차순
# common_df = common_df.sort_values(by='작업생성시간', ascending=True)





# ### 대기+작업시간 구하는 부분
# n_data['작업생성시간'] = pd.to_datetime(n_data['작업생성시간'], format='%Y%m%d%H%M%S')
# n_data['작업완료시간'] = pd.to_datetime(n_data['작업완료시간'], format='%Y%m%d%H%M%S')
# n_data['작업+대기시간'] = n_data['작업완료시간'] -n_data['작업생성시간']
# print(n_data['작업+대기시간'].dtype) ##timedelta64[ns]

# print(n_data['작업+대기시간'].tolist())
# # '작업+대기시간'을 ####정수형###으로 변환하여 분 단위로 계산
# n_data['작업+대기시간_분'] = n_data['작업+대기시간'].dt.total_seconds() / 60


# # '시간차이_분'을 y축으로 하는 선 그래프 그리기
# n_data['작업+대기시간_분'].plot(kind='line')
# plt.ylabel('시간차이 (분)')
# plt.ylim(0, 100)  # 분 단위로 범위 설정 (0 ~ 100)

# plt.show()


# # 작업코드 구내이적만 선택
# n_data_dropna = n_data_dropna[n_data_dropna['작업코드']=='VL']
# # print(n_data_dropna)

# # 블록별 구분
# blocks = n_data_dropna['블록'].unique()
# # block_group = n_data_dropna.groupby('블록')
# # print('block_group',block_group)
# # 블록별 명, 데이터 저장
# block_data = {}
# thing_data = {}
# block_device_data = {}
# for block, data in n_data_dropna.groupby('블록'):
#     block_data[block] = data
#     device_data = {}
#     for device, data_device in data.groupby('장비번호'):
#         device_data[device] = data_device
    
#     block_device_data[block] = device_data
# # print(block_device_data)
# print()

# # 전체 subplot 개수
# total_subplots = sum([len(value) for value in block_device_data.values()])

# # sqrt를 이용하여 subplot의 행과 열 개수를 결정
# num_rows = math.ceil(math.sqrt(total_subplots))
# num_cols = num_rows
# fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 15))
# plot_index =0

# for key, value in block_device_data.items():
#     # print(value)
#     # print("")
#     for key2, value2 in value.items():
#         # print(value2)
#         print("")
#         value2['대기시간'] = value2['작업생성시간'] - value2['작업생성시간'].shift(1)
    
#         value2['작업시간'] = value2['작업완료시간']-value2['작업생성시간']
#         print(value2[['블록','야드트럭(번호)', '장비번호','작업생성시간','대기시간', '작업시간']])
#         # '대기시간'을 분 단위로 변환
#         value2['대기시간'] = value2['대기시간'].dt.total_seconds() / 60
#         # '작업생성시간'을 인덱스로 설정
#         value2.set_index('작업생성시간', inplace=True)

#         ax = axs[plot_index // num_cols, plot_index % num_cols]
#         value2['대기시간'].plot(kind='line', ax=ax)
#         ax.set_title(f"{key} Block, Device {key2}")
#         ax.set_ylabel('대기시간 (분)')

#         plot_index += 1

# # 빈 subplot 제거
# if total_subplots < num_rows * num_cols:
#     for i in range(total_subplots, num_rows * num_cols):
#         fig.delaxes(axs.flatten()[i])

# plt.tight_layout()
# plt.show()        



        # # 선 그래프 그리기
        # fig, ax = plt.subplots()
        # value2['대기시간'].plot(kind = 'line', ax =ax)
        # ax.set_ylabel('대기시간')
        # plt.show()
# for block in blocks:
#     print('block',block)
#     block_df = block_device_data[block]
#     block_df = pd.DataFrame(block_df)

#     print(block_df.info())
    # block['대기시간'] = block['작업생성시간'] - block['작업생성시간'].shift(1)
    
    # block['작업시간'] = block['작업완료시간']-block['작업생성시간']
    # print(block[['야드트럭(번호)', '장비번호','작업생성시간','대기시간', '작업시간']])

#     # 장비번호별 구별
#     things = preprocessing_data['장비번호'].unique()

#     thing_group = preprocessing_data.groupby('장비번호')

#     for thing, group in thing_group:
#         thing_data[thing] = group.copy()

#     for thing in things:
#         thing_df = thing_data[thing]
#     print('thing_data',thing_data)
        
    # for thing in thing_data:
    #     df_result = preprocessing_data
    #     print(df_result[['야드트럭(번호)', '장비번호','작업생성시간','대기시간']])

    # print(preprocessing_data['작업시간'])



