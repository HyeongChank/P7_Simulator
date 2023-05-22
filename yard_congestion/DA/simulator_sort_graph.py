import simpy 
import random
import csv
import numpy as np
import csv
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
file_path = './truck_simulation_results.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]
data_rows = data[1:]
sorted_data = sorted(data_rows, key =lambda row: int(row[0]))
print(sorted_data)

out_times_list = [int(row[9]) for row in sorted_data]

in_times_list = [int(row[2]) for row in sorted_data]

index_times_list = [int(row[0]) for row in sorted_data]

# arrive_unload_spot_list = [int(row[3]) for row in sorted_data]
# complete_unload_work_list = [int(row[4]) for row in sorted_data]
# arrive_load_spot_list = [int(row[5]) for row in sorted_data]
# complete_load_work_list = [int(row[6]) for row in sorted_data]

# # forth_out_times_list = [str(out_time).zfill(4) for out_time in out_times_list]
# # forth_in_times_list = [str(in_time).zfill(4) for in_time in in_times_list]
# #forth_index_times_list = [str(index_time).zfill(4) for index_time in index_times_list]

# # print(forth_out_times_list)
# # print(forth_in_times_list)
sorted_data_with_In_yard_truck_volume = []

for row in sorted_data:
    in_time = row[2]
    index_time = row[0]
    int_in_time = int(in_time)
    int_index_time = int(index_time)
    # arrive_unload_spot = row[3]
    # int_arrive_unload_spot = int(arrive_unload_spot)
    # complete_unload_work = row[4]
    # arrive_load_spot = row[5]
    # complete_load_work = row[6]
    # int_complete_unload_work = int(complete_unload_work)
    # int_arrive_load_spot = int(arrive_load_spot)
    # int_complete_load_work = int(complete_load_work)

 
    # 현재 트럭보다 먼저 들어온 트럭 대수 구하기
    in_time_value1 = list(filter(lambda y : y<int_index_time, index_times_list))
    # 현재 시간보다 출차를 빨리한 차량 대수
    in_time_value2 = list(filter(lambda x: x< int_in_time, out_times_list))
    # 현재 터미널 내 트럭 대수 = 총 트럭 - 출차 대수(본인 트럭 제외)
    In_yard_truck_volume = len(in_time_value1)-len(in_time_value2)
    # print(In_yard_truck_volume)

    # ## 먼저 도착한 트럭에 대해서 조건 추가해야 함
    # # 반입장 대기 트럭 대수 구하기 = 작업완료 트럭수 - 반입장 도착 트럭수
    # arrive_unload_spot_data = list(filter(lambda x : x<int_arrive_unload_spot, arrive_unload_spot_list))
    # complete_unload_spot_data = list(filter(lambda y : y<int_complete_unload_work, complete_unload_work_list))
    # unload_spot_wait_volume = len(arrive_unload_spot_data)-len(complete_unload_spot_data)
    # print(row)
    # print(complete_unload_spot_data)
    # print(arrive_unload_spot_data)
    # print(unload_spot_wait_volume)
    # arrive_load_spot_data = list(filter(lambda x : x<int_arrive_load_spot, arrive_load_spot_list))
    # complete_load_spot_data = list(filter(lambda y : y<int_complete_load_work, complete_load_work_list))
    # load_spot_wait_volume = len(complete_load_spot_data)-len(arrive_load_spot_data)
    # print(load_spot_wait_volume)


    new_row = row + [In_yard_truck_volume]
    sorted_data_with_In_yard_truck_volume.append(new_row)


sorted_data_with_In_yard_truck_volume.insert(0,['number','code','entryTime','arrive_unload_spot', 'start_unload_work','complete_unload_work','arrive_load_spot','start_load_work','complete_load_work','Out_time','Work_time','block','unload_count','load_count','yard_truck_count'])
print(sorted_data_with_In_yard_truck_volume)
# 정렬된 데이터를 CSV 파일로 저장
sorted_file_path = './sorted_truck_simulation_results.csv'
with open(sorted_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_data_with_In_yard_truck_volume)

print("데이터를 첫 번째 트럭 열을 기준으로 오름차순으로 정렬하여 저장했습니다.")


## 애니메이션 구현 부분
file_path = './sorted_truck_simulation_results.csv'
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

for row in data_rows:
 
    in_time_out.append(int(row[2]))
    unload_waiting_time.append(int(row[5])-int(row[4]))
    load_waiting_time.append(int(row[8])-int(row[7]))
    unload_waiting_count.append(int(row[12]))
    load_waiting_count.append(int(row[13]))
    # wait_time_all = int(row[5])-int(row[4])
    # print(row(5))
    # print(int(row(4)))
    # waiting_time.append(wait_time_all)
    In_yard_truck_volume_entry_time.append(int(row[14]))

terminalgraph = plt.figure()
term = plt.axes()
term.set_xlim(0, max(in_time_out))
term.set_ylim(0, 50)

x = np.array(in_time_out)
y1 = np.array(unload_waiting_time)
y11 = np.array(unload_waiting_count)
y2 = np.array(load_waiting_time)
y22 = np.array(load_waiting_count)
y3 = np.array(In_yard_truck_volume_entry_time)
line1, = term.plot([],[], label='반입 대기시간')
line11, = term.plot([],[], label='반입 대기차량 수')
line2, = term.plot([],[], label='반출 대기시간')
line22, = term.plot([],[], label='반출 대기차량 수')
line3, = term.plot([],[], label='터미널 내 총 트럭대수')
term.legend()

def update(num, x, y1,y11,y2,y22,y3, line1,line11, line2, line22,line3):
    line1.set_data(x[:num], y1[:num])
    line11.set_data(x[:num], y11[:num])
    line2.set_data(x[:num], y2[:num])
    line22.set_data(x[:num], y22[:num])
    line3.set_data(x[:num], y3[:num])

    return line1, line2, line3
termani = animation.FuncAnimation(terminalgraph, update, frames = len(x) +1, fargs=(x,y1,y11,y2,y22,y3, line1,line11, line2, line22,line3),
                                  interval = 100, repeat = False)
animation_filename = "test_animation.gif"
termani.save(animation_filename, writer="pillow")
print(f"애니메이션을 '{animation_filename}' 파일로 저장했습니다.")
#plt.show()