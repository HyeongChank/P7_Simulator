import simpy 
import random
import csv
import numpy as np
import csv
import json
from datetime import datetime, timedelta
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
# Truck,Operation,entry_Time,arrive_unload_spot,start_unload_work,complete_unload_work,arrive_load_spot,start_load_work,complete_load_work,exit_Time,waiting_Time,block
## 데이터 정렬해서 다시 저장
def operate():
    file_path = 'data/truck_simulation_results.csv'
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    header = data[0]
    data_rows = data[1:]
    sorted_data = sorted(data_rows, key =lambda row: int(row[0]))
    # print(sorted_data)

    out_times_list = [int(row[9]) for row in sorted_data]

    in_times_list = [int(row[2]) for row in sorted_data]

    # 블록 구분(반입, 반출장)
    index_times_list = [int(row[0]) for row in sorted_data]
    unload_block_list = [row[14] for row in sorted_data]
    unload_block_list_unique = list(set(unload_block_list))
    unload_block_dict = dict(zip(unload_block_list_unique, ['A','B','C','D','E']))
    unload_block_list = [unload_block_dict[val] for val in unload_block_list]

    print(unload_block_dict)
    load_block_list = [row[15] for row in sorted_data]
    load_block_list_unique = list(set(load_block_list))
    load_block_dict = dict(zip(load_block_list_unique, ['Q','W','X','Y','Z']))
    load_block_list = [load_block_dict[val] for val in load_block_list]

    sorted_data_with_In_yard_truck_volume = []

    for row in sorted_data:
        in_time = row[2]
        index_time = row[0]
        int_in_time = int(in_time)
        int_index_time = int(index_time)
    
        # 현재 트럭보다 먼저 들어온 트럭 대수 구하기
        in_time_value1 = list(filter(lambda y : y<int_index_time, index_times_list))
        # 현재 시간보다 출차를 빨리한 차량 대수
        in_time_value2 = list(filter(lambda x: x< int_in_time, out_times_list))
        # 현재 터미널 내 트럭 대수 = 총 트럭 - 출차 대수(본인 트럭 제외)
        In_yard_truck_volume = len(in_time_value1)-len(in_time_value2)
        # print(In_yard_truck_volume)
        unload_count = row[12]
        load_count = row[13]
        row[14] = unload_block_dict[row[14]]
        row[15] = load_block_dict[row[15]]
    
        new_row = row + [In_yard_truck_volume]
        sorted_data_with_In_yard_truck_volume.append(new_row)


    sorted_data_with_In_yard_truck_volume.insert(0,['number','code','entryTime','arrive_unload_spot', 'start_unload_work','complete_unload_work','arrive_load_spot','start_load_work','complete_load_work','out_time','work_time', 'op', 'unload_count','load_count','unload_block', 'load_block', 'entry_count', 'exit_count', 'spot_wait_time','unload_progress_truck_count', 'load_progress_truck_count','visible', 'in_yard_count'])
    # print(sorted_data_with_In_yard_truck_volume)        1      2      3                  4                5                       6                       7               8                    9                 10         11      12    13               14               15             16              17           18        19                20                                21                         22          23      
    # 정렬된 데이터를 CSV 파일로 저장

    headers = data[0]
    rows = data[1:]
    json_data = [dict(zip(headers, row)) for row in rows]
    # json_output = json.dumps(json_data, ensure_ascii=False)


    sorted_file_path = 'data/sorted_truck_simulation_results.csv'
    with open(sorted_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sorted_data_with_In_yard_truck_volume)

    print("데이터를 첫 번째 트럭 열을 기준으로 오름차순으로 정렬하여 저장했습니다.")


    ## 애니메이션 구현 부분
    file_path = 'data/sorted_truck_simulation_results.csv'
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    header = data[0]
    data_rows = data[1:]
    in_time_out = []
    unload_waiting_time = []
    unload_waiting_count = []
    load_waiting_time = []
    load_waiting_count = []
    In_yard_truck_volume_entry_time = []
    spot_wait_time = 0
    for row in data_rows:
        # 별도 계산 값들
        in_time_out.append(int(row[2]))
        unload_waiting_time.append(int(row[5])-int(row[4]))
        load_waiting_time.append(int(row[8])-int(row[7]))
        unload_waiting_count.append(int(row[12]))
        load_waiting_count.append(int(row[13]))
        spot_wait_time += int(row[18])
        # wait_time_all = int(row[5])-int(row[4])
        # print(row(5))
        # print(int(row(4)))
        # waiting_time.append(wait_time_all)
    print('총 대기시간', spot_wait_time)
    terminalgraph = plt.figure()
    term = plt.axes()
    term.set_xlim(0, max(in_time_out))
    term.set_ylim(0, 50)

    x = np.array(in_time_out)
    y1 = np.array(unload_waiting_time)
    y11 = np.array(unload_waiting_count)
    y2 = np.array(load_waiting_time)
    y22 = np.array(load_waiting_count)

    line1, = term.plot([],[], label='반입 대기시간')
    line11, = term.plot([],[], label='반입 대기차량 수')
    line2, = term.plot([],[], label='반출 대기시간')
    line22, = term.plot([],[], label='반출 대기차량 수')

    term.legend()

    def update(num, x, y1,y11,y2,y22, line1,line11, line2, line22):
        line1.set_data(x[:num], y1[:num])
        line11.set_data(x[:num], y11[:num])
        line2.set_data(x[:num], y2[:num])
        line22.set_data(x[:num], y22[:num])

        return line1, line2
    termani = animation.FuncAnimation(terminalgraph, update, frames = len(x) +1, fargs=(x,y1,y11,y2,y22, line1,line11, line2, line22),
                                    interval = 100, repeat = False)
    animation_filename = "images/test_animation.gif"
    termani.save(animation_filename, writer="pillow")
    print(f"애니메이션을 '{animation_filename}' 파일로 저장했습니다.")
    #plt.show()
    return json_data

if __name__=='__main__':
    json_output = operate()
    print(json_output)