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

def load():
    data = pd.read_excel("data/TBS_data.xlsx", sheet_name='야드크레이인_작업이력')
    scd_data = pd.read_excel("data/TBS_data.xlsx", sheet_name='반출입_예정컨테이너')
    cbd_data = pd.read_excel("data/TBS_data.xlsx", sheet_name='장치장_전')
    cad_data = pd.read_excel("data/TBS_data.xlsx", sheet_name='장치장_후')
    quay_work_data = pd.read_excel("data/TBS_data.xlsx", sheet_name='본선크레인_작업이력')

    # int 타입임
    print(quay_work_data['작업완료시간'].dtype)
    quay_work_data['작업완료시간'] = quay_work_data['작업완료시간'].astype(str).replace('^2020', '2023', regex=True)

 
    # data, container_before_data, container_after_data merge
    ycb_common_values = data['컨테이너번호'].isin(quay_work_data['컨테이너번호']).sum() # 6103개
    print('ycb_common_values', ycb_common_values)
    yard_con_common_df = pd.merge(data, quay_work_data, on='컨테이너번호')
    print(yard_con_common_df)
    print(yard_con_common_df.columns)
    return yard_con_common_df

def make_df(common_df):
    # 데이터 전처리
    common_df['작업코드_x'] = common_df['작업코드_x'].replace({'VU': 1, 'VL': 2, 'GR': 3, 'GD': 4, 'TM':5,'TS':6})
    common_df['장비번호'] = common_df['장비번호'].replace({'Y02': 1})

    # 외부트럭에 1 넣기
    common_df['야드트럭(번호)'] = common_df['야드트럭(번호)'].fillna(1)
 
    # print('n_data', n_data)
    print('common_df',common_df.info())
    # print(n_data.isna().sum())

    # 시간 타입 통합
    common_df['작업생성시간'] = pd.to_datetime(common_df['작업생성시간'], format='%Y%m%d%H%M%S')
    common_df['작업완료시간_x'] = pd.to_datetime(common_df['작업완료시간_x'], format='%Y%m%d%H%M%S')
    common_df['작업완료시간_y'] = pd.to_datetime(common_df['작업완료시간_y'], format='%Y%m%d%H%M%S')
    print('common_df',common_df)
    print('작업생성시간',common_df['작업생성시간'].dtype)
    print('작업완료시간_x',common_df['작업완료시간_x'].dtype)
    print('작업완료시간_y',common_df['작업완료시간_y'].dtype)
    print('작업완료시간_y',common_df['작업완료시간_y'])
    common_df['작업+대기시간'] = common_df['작업완료시간_x'] -common_df['작업생성시간']
    # print(common_df[['작업코드','항차','야드트럭(번호)','컨테이너(사이즈 코드)','장비번호', '작업생성시간','작업완료시간']])



    common_df_truck_yard = common_df[common_df['야드트럭(번호)'] != 1]
    print(common_df_truck_yard.info())

    common_df_truck_normal = common_df[common_df['야드트럭(번호)'] == 1]
    print(common_df_truck_normal.info())

    correlation_matrix = common_df_truck_normal[['작업코드_x','항차_x','야드트럭(번호)','컨테이너(사이즈 코드)','장비번호', '작업생성시간','작업완료시간_x', '작업완료시간_y','작업+대기시간','해치순서','해치번호']].corr()

    sns.heatmap(correlation_matrix, annot=True)
    plt.show()
    

if __name__=='__main__':
    common_df = load()
    make_df(common_df)