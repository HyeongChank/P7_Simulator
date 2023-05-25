import simpy 
import random
import csv

class Truck:
    def __init__(self, env, name, arrival_time, unload_trucks_completed, load_trucks_completed, unload_load_trucks_completed, block, unload_spot, load_spot, end_wait_start_unload_work, end_wait_start_load_work):
        self.env = env
        self.name = name
        self.block = block
        # 각 장소마다의 대기차량 구하기 위해 세분화(arrive, completed)
        self.unload_spot = unload_spot
        self.load_spot = load_spot
        self.unload_trucks_completed = unload_trucks_completed
        self.load_trucks_completed = load_trucks_completed
        self.arrival_time = arrival_time
        self.unload_load_trucks_completed = unload_load_trucks_completed
        self.end_wait_start_unload_work = end_wait_start_unload_work
        self.end_wait_start_load_work = end_wait_start_load_work
        # self.in_progress_trucks = []
        #분포에 따라 customer 도착
        self.action = env.process(self.truck_generate())

    def truck_generate(self):
        yield env.timeout(self.arrival_time)
   
        print(f"트럭 {self.name}이(가) 입차했습니다. 시간: {env.now}")
        
        select_block = random.choice(self.block)
        print(f"트럭 {self.name}이(가) {select_block} 블록으로 배정되습니다.")

        in_yard_time = env.now
        ## 차량대수 계산 위해 wating_times 딕셔너리 생성
        waiting_times[self.name] = in_yard_time
        self.env.process(self.in_out_work(waiting_times, select_block))
        # self.in_progress_trucks.append(self.name)


    def in_out_work(self, waiting_times, select_block):
        select_num = random.randint(1,10)
        if select_num <= 4:
            entry_to_unload_move = 5
            yield env.timeout(entry_to_unload_move)
            print(f"트럭 {self.name}이 반입장소에 도착했습니다. 시간: {env.now}")
            arrive_unload_spot_time = env.now
            ## capacity 에 따라 앞차가 작업 중일 시 뒤에 온 차는 대기!! 앞 차 작업완료시 뒤 차 작업 시작
            unload_spot_count = len(self.unload_spot.queue)
            load_spot_count = len(self.load_spot.queue)
            print(f"현재 반입장소에서 대기 중인 차량의 수: {len(self.unload_spot.queue)}")                
            with self.unload_spot.request() as req:
                
                yield req
                # 트럭이 반입장소 도착해서 대기시작할 때의 대기 중인 차량의 수임
                self.end_wait_start_unload_work = env.now
                print(f"트럭 {self.name}이 반입장소에서 작업시작하는 시간 : {self.end_wait_start_unload_work}")
                unload_spot_wait_time = self.end_wait_start_unload_work- arrive_unload_spot_time
                print(f"트럭 {self.name}이 반입장소에서 대기하는 시간 : {unload_spot_wait_time}")
                #
                arrive_load_spot_time = 0
                complete_load_work_time = 0
                self.end_wait_start_load_work = 0
                #
                # 작업 시간
                in_work_time = random.randint(10,25)
                yield env.timeout(in_work_time)
                print(f"트럭 {self.name}이(가) 반입을 완료했습니다. 시간: {env.now}")
                complete_unload_work_time = env.now

            # exit gate 까지 이동
            out_before_wait_time = 5
            yield env.timeout(out_before_wait_time)
            print(f"트럭 {self.name}이(가) 출차했습니다. 시간: {env.now}")
            out_yard_time = env.now

            # 트럭번호를 통해 딕셔너리로 저장한 입차시간을 출차시간에서 빼서 총 대기시간 산출(out, in 저장해서 차감)
            in_yard_time = waiting_times[self.name]
            print('key', in_yard_time)
            waiting_time = out_yard_time- in_yard_time
            result_waiting.append(waiting_time)
            print(f"트럭 {self.name}의 (반입) 총 터미널 내 소요시간: {waiting_time}")
            new_data = [self.name, "in", in_yard_time, arrive_unload_spot_time, self.end_wait_start_unload_work, complete_unload_work_time, arrive_load_spot_time, complete_load_work_time, self.end_wait_start_load_work, out_yard_time, waiting_time, select_block, unload_spot_count, load_spot_count]
            unload_trucks_completed.append(new_data)

        elif select_num <= 7:
            entry_to_unload_move = 5
            yield env.timeout(entry_to_unload_move)
            print(f"트럭 {self.name}이 반입장소에 도착했습니다. 시간: {env.now}")
            arrive_unload_spot_time = env.now
            unload_spot_count = len(self.unload_spot.queue)

            print(f"현재 반입장소에서 대기 중인 차량의 수: {len(self.unload_spot.queue)}") 
            ## capacity 에 따라 앞차가 작업 중일 시 뒤에 온 차는 대기!! 앞 차 작업완료시 뒤 차 작업 시작
            with self.unload_spot.request() as req:
                yield req
                self.end_wait_start_unload_work = env.now
                print(f"트럭 {self.name}이 반입장소에서 작업시작하는 시간 : {self.end_wait_start_unload_work}")
                unload_spot_wait_time = self.end_wait_start_unload_work- arrive_unload_spot_time

                print(f"트럭 {self.name}이 반입장소에서 대기하는 시간 : {unload_spot_wait_time}")
                # 반입 작업 시간
                in_work_time = random.randint(10,25)
                yield env.timeout(in_work_time)
        
                print(f"트럭 {self.name}이(가) 반입을 완료했습니다. 시간: {env.now}")
                complete_unload_work_time = env.now

            # 반출 작업장 이동
            unload_to_load_move = 5
            yield env.timeout(unload_to_load_move)
            print(f"트럭 {self.name}이 반출 장소에 도착했습니다. 시간: {env.now}")
            arrive_load_spot_time = env.now

            load_spot_count = len(self.load_spot.queue)
            print(f"현재 반출장소에서 대기 중인 차량의 수: {len(self.load_spot.queue)}")
            with self.load_spot.request() as req:
                yield req
                
                self.end_wait_start_load_work = env.now
                print(f"트럭 {self.name}이 반출장소에서 작업시작하는 시간 : {self.end_wait_start_load_work}")
                load_spot_wait_time = self.end_wait_start_load_work- arrive_load_spot_time

                print(f"트럭 {self.name}이 반출장소에서 대기하는 시간 : {load_spot_wait_time}")                
                # 반출 작업 시간
                out_work_time = random.randint(15,20)
                yield env.timeout(out_work_time)
                print(f"트럭 {self.name}이(가) 반출 작업을 완료했습니다. 시간: {env.now}")
                complete_load_work_time = env.now

            # exit gate 까지 이동
            out_before_wait_time = 5
            yield env.timeout(out_before_wait_time)
            print(f"트럭 {self.name}이(가) 출차했습니다. 시간: {env.now}")
            out_yard_time = env.now
            print(out_yard_time)

            in_yard_time = waiting_times[self.name]
            print('key', in_yard_time)
            waiting_time = out_yard_time- in_yard_time
            result_waiting.append(waiting_time)
            print(f"트럭 {self.name}의 반입, 출차 대기시간: {waiting_time}")
            new_data = [self.name, "in_out", in_yard_time, arrive_unload_spot_time, self.end_wait_start_unload_work, complete_unload_work_time, arrive_load_spot_time, self.end_wait_start_load_work, complete_load_work_time, out_yard_time, waiting_time, select_block, unload_spot_count, load_spot_count]
            unload_load_trucks_completed.append(new_data)

        else:
 
            # 반출 작업장 이동
            entry_to_load_move = 5
            yield env.timeout(entry_to_load_move)
            print(f"트럭 {self.name}이 반출장소에 도착했습니다. 시간: {env.now}")
            arrive_load_spot_time = env.now
            load_spot_count = len(self.load_spot.queue)
            unload_spot_count = len(self.unload_spot.queue)
            print(f"현재 반출장소에서 대기 중인 차량의 수: {len(self.load_spot.queue)}")
            ## 앞 차 있을 시 대기
            with self.load_spot.request() as req:
                yield req
                self.end_wait_start_load_work = env.now
                print(f"트럭 {self.name}이 반출장소에서 작업시작하는 시간 : {self.end_wait_start_load_work}")
                load_spot_wait_time = self.end_wait_start_load_work- arrive_load_spot_time
                print(f"트럭 {self.name}이 반출장소에서 대기하는 시간 : {load_spot_wait_time}")
                #
                arrive_unload_spot_time = 0
                complete_unload_work_time = 0
                self.end_wait_start_unload_work = 0
                # 반출 작업
                out_work_time = random.randint(15,20)
                yield env.timeout(out_work_time)
                print(f"트럭 {self.name}이(가) 반출 작업을 완료했습니다. 시간: {env.now}")
                complete_load_work_time = env.now

            # exit gate 이동
            out_before_wait_time = 5
            yield env.timeout(out_before_wait_time)
            print(f"트럭 {self.name}이(가) 출차했습니다. 시간: {env.now}")
            out_yard_time = env.now

            in_yard_time = waiting_times[self.name]
            print('key', in_yard_time)
            waiting_time = out_yard_time- in_yard_time
            result_waiting.append(waiting_time)
            
            print(f"트럭 {self.name}의 반출만 대기시간: {waiting_time}")
            new_data = [self.name, "out", in_yard_time, arrive_unload_spot_time, self.end_wait_start_unload_work, complete_unload_work_time, arrive_load_spot_time, self.end_wait_start_load_work, complete_load_work_time, out_yard_time, waiting_time, select_block, unload_spot_count, load_spot_count]
            load_trucks_completed.append(new_data)
        # self.in_progress_trucks.remove(self.name)
        

env = simpy.Environment()
unload_spot = simpy.Resource(env, capacity=5)
load_spot = simpy.Resource(env, capacity=5)
arrival_interval = random.randint(2,4)  # 트럭 도착 주기 (분 단위)
unload_trucks_completed = []
load_trucks_completed = []
waiting_times = {}
result_waiting = []
unload_load_trucks_completed = []
block = ['A','B','C']
end_wait_start_unload_work = 0
end_wait_start_load_work = 0
# 트럭 대수
arrival_interval =0
for i in range(200):
    arrival_time = random.randint(1,3)
    arrival_interval += arrival_time
    Truck(env, i+1, arrival_interval, unload_trucks_completed, load_trucks_completed, unload_load_trucks_completed, block, unload_spot, load_spot, end_wait_start_unload_work, end_wait_start_load_work)

### 파일에 저장되는 데이터 개수와 관련됨
env.run(until=1440)  # 시뮬레이션 시간 (분 단위)

print(f"반입 작업을 완료한 트럭 수: {len(unload_trucks_completed)}")
print(f"반출 작업을 완료한 트럭 수: {len(load_trucks_completed)}")

# 결과를 저장할 CSV 파일 이름
csv_filename = "data/truck_simulation_results.csv"

    # CSV 파일에 결과를 기록하는 함수
def save_results_to_csv(filename, unload_trucks_completed, load_trucks_completed, unload_load_trucks_completed):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Truck", "Operation", "entry_Time", "arrive_unload_spot", "start_unload_work", "complete_unload_work", "arrive_load_spot", "start_load_work","complete_load_work", "exit_Time", "waiting_Time", "block", "unload_spot_truck_count", "load_spot_truck_count"])  # 헤더 라인 작성

        # 반입 작업 완료 트럭 기록
        for truck in unload_trucks_completed:
            
            writer.writerow([truck[0], truck[1], truck[2], truck[3], truck[4], truck[5], truck[6], truck[7], truck[8], truck[9], truck[10], truck[11], truck[12], truck[13]])

        # 반출 작업 완료 트럭 기록
        for truck in load_trucks_completed:
        
            writer.writerow([truck[0], truck[1], truck[2], truck[3], truck[4], truck[5], truck[6], truck[7], truck[8], truck[9], truck[10], truck[11], truck[12] , truck[13]])

        # 반입+반출 작업 완료 트럭 기록
        for truck in unload_load_trucks_completed:
        
            writer.writerow([truck[0], truck[1], truck[2], truck[3], truck[4], truck[5], truck[6], truck[7], truck[8], truck[9], truck[10], truck[11], truck[12] , truck[13]])

        env.run(until=1441)  # 시뮬레이션 시간 (분 단위)

        print(f"반입 작업을 완료한 트럭 수: {len(unload_trucks_completed)}")
        print(f"반출 작업을 완료한 트럭 수: {len(load_trucks_completed)}")
        print(f"반출 작업을 완료한 트럭 수: {len(unload_load_trucks_completed)}")

# 결과를 CSV 파일로 저장
save_results_to_csv(csv_filename, unload_trucks_completed, load_trucks_completed, unload_load_trucks_completed)

print(f"결과를 '{csv_filename}' 파일로 저장했습니다.")