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

## 데이터 정렬해서 다시 저장
file_path = './truck_simulation_results.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]
data_rows = data[1:]
sorted_data = sorted(data_rows, key =lambda row: int(row[0]))


out_times_list = [int(row[3]) for row in sorted_data]
# print(out_times_list)
in_times_list = [int(row[2]) for row in sorted_data]
# print(in_times_list)
index_times_list = [int(row[0]) for row in sorted_data]
print(index_times_list)
# forth_out_times_list = [str(out_time).zfill(4) for out_time in out_times_list]
# forth_in_times_list = [str(in_time).zfill(4) for in_time in in_times_list]
#forth_index_times_list = [str(index_time).zfill(4) for index_time in index_times_list]

# print(forth_out_times_list)
# print(forth_in_times_list)
sorted_data_with_truck_volumn = []

for row in sorted_data:
    in_time = row[2]
    index_time = row[0]
    int_in_time = int(in_time)
    int_index_time = int(index_time)
 
    # 현재 트럭보다 먼저 들어온 트럭 대수 구하기
    in_time_value1 = list(filter(lambda y : y<int_index_time, index_times_list))
    # print('in_time_value1',in_time_value1)
    # 현재 시간보다 출차를 빨리한 차량 대수
    in_time_value2 = list(filter(lambda x: x< int_in_time, out_times_list))
    # print('in_time_value2',len(in_time_value2))
    # 현재 터미널 내 트럭 대수 = 총 트럭 - 출차 대수
    truck_volumn = len(in_time_value1)-len(in_time_value2)
    # print(truck_volumn)
    new_row = row + [truck_volumn]
    sorted_data_with_truck_volumn.append(new_row)
print(sorted_data_with_truck_volumn)

sorted_data_with_truck_volumn.insert(0,['Truck_Num','Code','In_time','Out_time','Work_time','block','In_yard_truck'])

# 정렬된 데이터를 CSV 파일로 저장
sorted_file_path = './sorted_truck_simulation_results.csv'
with open(sorted_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_data_with_truck_volumn)

print("데이터를 첫 번째 트럭 열을 기준으로 오름차순으로 정렬하여 저장했습니다.")


## 애니메이션 구현 부분
file_path = './sorted_truck_simulation_results.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
header = data[0]
data_rows = data[1:]
in_time_out = []
waiting_time = []
truck_v = []

for row in data_rows:
 
    in_time_out.append(int(row[2]))
    waiting_time.append(int(row[4]))
    truck_v.append(int(row[6]))

sinegraph = plt.figure()
sine = plt.axes()
sine.set_xlim(0, max(in_time_out))
sine.set_ylim(0, 20)

x = np.array(in_time_out)
y = np.array(truck_v)

line, = sine.plot([],[])

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,
sineani = animation.FuncAnimation(sinegraph, update, frames = len(x) +1, fargs=(x,y, line),
                                  interval = 100, repeat = False)
animation_filename = "test_animation.gif"
sineani.save(animation_filename, writer="pillow")
print(f"애니메이션을 '{animation_filename}' 파일로 저장했습니다.")
#plt.show()