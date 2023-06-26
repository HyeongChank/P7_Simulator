import simpy 
import random
import csv

entry_count = 0
exit_count =0
before_unload = ''
before_load = ''
def make_simul_operate(trucknum, processtime, blocknum):
    class Truck:
        def __init__(self, env, name, arrival_time,unload_trucks_completed, load_trucks_completed, unload_load_trucks_completed, operation, unload_spot, load_spot, end_wait_start_unload_work, end_wait_start_load_work, visible, container_status, container_size):
            self.env = env
            self.name = name
            self.operation = operation
            # 각 장소마다의 대기차량 구하기 위해 세분화(arrive, completed)
            self.unload_spot = unload_spot
            self.load_spot = load_spot
            self.unload_trucks_completed = unload_trucks_completed
            self.load_trucks_completed = load_trucks_completed

            self.arrival_time = arrival_time
            self.unload_load_trucks_completed = unload_load_trucks_completed
            self.end_wait_start_unload_work = end_wait_start_unload_work
            self.end_wait_start_load_work = end_wait_start_load_work
            self.visible = visible
            self.container_status = container_status
            self.container_size = container_size
           
            # self.in_progress_trucks = []
            #분포에 따라 truck 도착
            self.action = env.process(self.truck_generate())
            
        def enter(self):
            global entry_count
            entry_count +=1
            return entry_count
        
        def out(self):
            global exit_count
            exit_count +=1
            return exit_count
            
        def truck_generate(self):
            # before_unload, before_load를 truck generate에 포함시키니 이전에 할당한 블록이
            # 아니라 self 에 설정한 값으로 변경되기 때문에 전역으로 설정함
            global before_unload
            global before_load
            yield env.timeout(self.arrival_time)
            entry_truck_count = self.enter()
            # print(entry_truck_count)
            # print(f"트럭 {self.name}이(가) 입차했습니다. 시간: {env.now}")
            
            self.visible = True
            self.container_size = random.choice(self.container_size)
            self.container_status = random.choice(self.container_status)
            # assigned 일단 부여해놓고 나중에 주석처리해야 함
            assigned_unload_spot = None
            assigned_load_spot = None
            min_unload = float('inf')
            min_load = float('inf')
            if before_unload != None:
                print("before_unload" + before_unload)
                print("before_load" + before_load)
            if before_unload == None:
                print("before_unload None")
                
                
            select_operation = random.choice(self.operation)
            
            
            #### 오류가 났다 안났다 반복했었음 : 원인 조건을 이전에 할당한 블록을 제외하고 대기차량 적은 곳으로 배정했어야 하는데 반대로 했었음
            ## 해결됨 ~~~~~~~~~~
            if select_operation == 'unload':
                print('unload')
                print('min_unload' + str(min_unload))
                print('min_load' + str(min_load))
                ## 대기차량 및 작업 차량 수가 가장 적은 블록으로 할당(최적화)
                min_unload_spots = []
                min_load_spots = []
                for spot, resource in self.unload_spot.items():
                    print(spot + '대기차량+작업차량' + str(len(resource.queue)+resource.count))
                    print('min_unload' +str(min_unload))
                    if spot != before_unload:
                        if (len(resource.queue)+resource.count)  < min_unload:
                            min_unload = (len(resource.queue)+resource.count)
                            # 바로 직전에 할당한 블록 제외(최적화)
                            min_unload_spots.append(spot)
                            
                        elif (len(resource.queue)+resource.count) == min_unload:
                            min_unload_spots.append(spot)
                        

                for spot, resource in self.load_spot.items():
                    print(spot + '대기차량+작업차량' + str(len(resource.queue)+resource.count))
                    print('min_load' + str(min_load))
                    if spot != before_load:
                        if (len(resource.queue)+resource.count)  < min_load:
                            min_load = (len(resource.queue)+resource.count)
                            min_load_spots.append(spot)
                        elif (len(resource.queue)+resource.count) == min_load:
                            min_load_spots.append(spot)

                print(min_unload_spots)
                print(self.container_status + self.container_size)
                assigned_unload_spot = random.choice(min_unload_spots)
                before_unload = assigned_unload_spot
                print('할당된 before_unload' + before_unload)
                assigned_load_spot = random.choice(min_load_spots)
                before_load =  assigned_load_spot
                print(f"트럭 {self.name}이(가) {assigned_unload_spot} 블록으로 배정되습니다.")
                
            if select_operation == 'load':
                print('load')
                min_unload_spots = []
                min_load_spots = []
                for spot, resource in self.unload_spot.items():
                    print(spot + '대기차량+작업차량' + str(len(resource.queue)+resource.count))
                    print('min_unload' + str(min_unload))
                    if spot != before_unload:
                        if (len(resource.queue)+resource.count)  < min_unload:
                            min_unload = (len(resource.queue)+resource.count)
                            # 바로 직전에 할당한 블록 제외(최적화)
                            min_unload_spots.append(spot)
      
                        elif (len(resource.queue)+resource.count) == min_unload:
                            min_unload_spots.append(spot)
                        

                for spot, resource in self.load_spot.items():
                    print(spot + '대기차량+작업차량' + str(len(resource.queue)+resource.count))
                    print('min_load' + str(min_load))
                    if spot != before_load:
                        if (len(resource.queue)+resource.count)  < min_load:
                            min_load = (len(resource.queue)+resource.count)
                            min_load_spots.append(spot)
                        elif (len(resource.queue)+resource.count) == min_load:
                            min_load_spots.append(spot)

            
                print(self.container_status + self.container_size)
                assigned_unload_spot = random.choice(min_unload_spots)
                before_unload = assigned_unload_spot
                assigned_load_spot = random.choice(min_load_spots)
                before_load =  assigned_load_spot

                print(f"트럭 {self.name}이(가) {assigned_load_spot} 블록으로 배정되습니다.")
            print('min_unload_out' + str(min_unload))    
            
            
            if select_operation == 'both':
                min_unload_spots = []
                min_load_spots = []
                print('min_unload_in' + str(min_unload))   
                for spot, resource in self.unload_spot.items():
                    print(self.unload_spot)
                    print('min_unload_re' + str(min_unload))
                    print(spot + '대기차량+작업차량' + str(len(resource.queue)+resource.count))
                    if spot != before_unload:
                        if (len(resource.queue)+resource.count)  < min_unload:
                            min_unload = (len(resource.queue)+resource.count)
                            print(min_unload)   
                            # 바로 직전에 할당한 블록 제외(최적화)
                            min_unload_spots.append(spot)
                            print(min_unload_spots)
                         
                        elif (len(resource.queue)+resource.count) == min_unload:
                            min_unload_spots.append(spot)

                        
                print('min_load_in' + str(min_load))   

                min_load = float('inf')
                for spot, resource in self.load_spot.items():
                    print(spot + '대기차량+작업차량' + str(len(resource.queue)+resource.count))
                    print('bbmin_load' + str(min_load))
                    if spot != before_load:
                        if (len(resource.queue)+resource.count)  < min_load:
                            min_load = (len(resource.queue)+resource.count)
                            print(min_load)
                            min_load_spots.append(spot)
                            print(min_load_spots)
                        elif (len(resource.queue)+resource.count) == min_load:
                            min_load_spots.append(spot)

                print(min_unload_spots)
                print(min_load_spots)
                print(self.container_status + self.container_size)
                assigned_unload_spot = random.choice(min_unload_spots)
                before_unload = assigned_unload_spot
                print('할당된 before_unload' + before_unload)
                
                assigned_load_spot = random.choice(min_load_spots)
                before_load =  assigned_load_spot
                print('할당된 before_load' + before_load)
                print(f"트럭 {self.name}이(가) {assigned_unload_spot} 와 {assigned_load_spot} 블록으로 배정되습니다.")

            in_yard_time = env.now
            ## 차량대수 계산 위해 wating_times 딕셔너리 생성
            waiting_times[self.name] = in_yard_time
            self.env.process(self.in_out_work(waiting_times, select_operation, assigned_unload_spot, assigned_load_spot, entry_truck_count))
            # self.in_progress_trucks.append(self.name)


        def in_out_work(self, waiting_times, select_operation, assigned_unload_spot, assigned_load_spot, entry_truck_count):
            entry_truck_count = entry_truck_count
            if select_operation == 'unload':
                entry_to_unload_move = 5
                yield env.timeout(entry_to_unload_move)
                print(f"트럭 {self.name}이 반입장소에 도착했습니다. 시간: {env.now}")
                arrive_unload_spot_time = env.now
                ## capacity 에 따라 앞차가 작업 중일 시 뒤에 온 차는 대기!! 앞 차 작업완료시 뒤 차 작업 시작
                unload_spot_count = len(self.unload_spot[assigned_unload_spot].queue)
                unload_progress_truck_count = self.unload_spot[assigned_unload_spot].count
                load_progress_truck_count = self.load_spot[assigned_load_spot].count
                load_spot_count = 0
                print(f"현재 반입장소에서 대기 중인 차량의 수: {len(self.unload_spot[assigned_unload_spot].queue)}")                
                with self.unload_spot[assigned_unload_spot].request() as req:
                    
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
                    if self.container_size == 'small':
                        in_work_time = random.randint(18,25)
                    elif self.container_size =='medium':
                        in_work_time = random.randint(13,20)
                    else:
                        in_work_time = random.randint(10,15)
                        
                    if self.container_status == 'long-term':
                        in_work_time +=3
                    elif self.container_status =='fresh':
                        in_work_time -=3
                        
                    yield env.timeout(in_work_time)
                    print(f"트럭 {self.name}이(가) 반입을 완료했습니다. 시간: {env.now}")
                    complete_unload_work_time = env.now

                # exit gate 까지 이동
                out_before_wait_time = 5
                yield env.timeout(out_before_wait_time)
                exit_truck_count = self.out()
                print(exit_truck_count)
                print(f"트럭 {self.name}이(가) 출차했습니다. 시간: {env.now}")
                out_yard_time = env.now

                # 트럭번호를 통해 딕셔너리로 저장한 입차시간을 출차시간에서 빼서 총 대기시간 산출(out, in 저장해서 차감)
                in_yard_time = waiting_times[self.name]
                print('key', in_yard_time)
                waiting_time = out_yard_time- in_yard_time
                result_waiting.append(waiting_time)
                print(f"트럭 {self.name}의 (반입) 총 터미널 내 소요시간: {waiting_time}")

                spot_wait_time = unload_spot_wait_time
                new_data = [self.name, "unload", in_yard_time, arrive_unload_spot_time, self.end_wait_start_unload_work, complete_unload_work_time, arrive_load_spot_time, complete_load_work_time, self.end_wait_start_load_work, out_yard_time, waiting_time, select_operation, unload_spot_count, load_spot_count, self.unload_spot[assigned_unload_spot], self.load_spot[assigned_load_spot], entry_truck_count, exit_truck_count, spot_wait_time, unload_progress_truck_count, load_progress_truck_count, self.visible, self.container_status, self.container_size]
                unload_trucks_completed.append(new_data)

            elif select_operation == 'both':
                entry_to_unload_move = 5
                yield env.timeout(entry_to_unload_move)
                print(f"트럭 {self.name}이 반입장소에 도착했습니다. 시간: {env.now}")
                arrive_unload_spot_time = env.now
                unload_spot_count = len(self.unload_spot[assigned_unload_spot].queue)
                unload_progress_truck_count = self.unload_spot[assigned_unload_spot].count
                load_progress_truck_count = self.load_spot[assigned_load_spot].count
                
                print(f"현재 반입장소에서 대기 중인 차량의 수: {len(self.unload_spot[assigned_unload_spot].queue)}") 
                ## capacity 에 따라 앞차가 작업 중일 시 뒤에 온 차는 대기!! 앞 차 작업완료시 뒤 차 작업 시작
                with self.unload_spot[assigned_unload_spot].request() as req:
                    yield req
                    self.end_wait_start_unload_work = env.now
                    print(f"트럭 {self.name}이 반입장소에서 작업시작하는 시간 : {self.end_wait_start_unload_work}")
                    unload_spot_wait_time = self.end_wait_start_unload_work- arrive_unload_spot_time

                    print(f"트럭 {self.name}이 반입장소에서 대기하는 시간 : {unload_spot_wait_time}")
                    # 반입 작업 시간
                    if self.container_size == 'small':
                        in_work_time = random.randint(18,25)
                    elif self.container_size =='medium':
                        in_work_time = random.randint(13,20)
                    else:
                        in_work_time = random.randint(10,15)
                        
                    if self.container_status == 'long-term':
                        in_work_time +=3
                    elif self.container_status =='fresh':
                        in_work_time -=3
                    yield env.timeout(in_work_time)
            
                    print(f"트럭 {self.name}이(가) 반입을 완료했습니다. 시간: {env.now}")
                    complete_unload_work_time = env.now

                # 반출 작업장 이동
                unload_to_load_move = 5
                yield env.timeout(unload_to_load_move)
                print(f"트럭 {self.name}이 반출 장소에 도착했습니다. 시간: {env.now}")
                arrive_load_spot_time = env.now

                load_spot_count = len(self.load_spot[assigned_load_spot].queue)
                print(f"현재 반출장소에서 대기 중인 차량의 수: {len(self.load_spot[assigned_load_spot].queue)}")
                with self.load_spot[assigned_load_spot].request() as req:
                    yield req
                    
                    self.end_wait_start_load_work = env.now
                    print(f"트럭 {self.name}이 반출장소에서 작업시작하는 시간 : {self.end_wait_start_load_work}")
                    load_spot_wait_time = self.end_wait_start_load_work- arrive_load_spot_time

                    print(f"트럭 {self.name}이 반출장소에서 대기하는 시간 : {load_spot_wait_time}")                
                    # 반출 작업 시간
                    if self.container_size == 'small':
                        out_work_time = random.randint(18,25)
                    elif self.container_size =='medium':
                        out_work_time = random.randint(13,20)
                    else:
                        out_work_time = random.randint(10,15)
                    if self.container_status == 'long-term':
                        out_work_time +=3
                    elif self.container_status =='fresh':
                        out_work_time -=3
                        
                    # out_work_time = random.randint(15,25)                        
                    yield env.timeout(out_work_time)
                    print(f"트럭 {self.name}이(가) 반출 작업을 완료했습니다. 시간: {env.now}")
                    complete_load_work_time = env.now

                # exit gate 까지 이동
                out_before_wait_time = 5
                yield env.timeout(out_before_wait_time)
                exit_truck_count = self.out()
                print(f"트럭 {self.name}이(가) 출차했습니다. 시간: {env.now}")
                out_yard_time = env.now
                print(out_yard_time)

                in_yard_time = waiting_times[self.name]
                print('key', in_yard_time)
                waiting_time = out_yard_time- in_yard_time
                result_waiting.append(waiting_time)
                print(f"트럭 {self.name}의 입차~출차시간: {waiting_time}")
                spot_wait_time = unload_spot_wait_time + load_spot_wait_time
                new_data = [self.name, "both", in_yard_time, arrive_unload_spot_time, self.end_wait_start_unload_work, complete_unload_work_time, arrive_load_spot_time, self.end_wait_start_load_work, complete_load_work_time, out_yard_time, waiting_time, select_operation, unload_spot_count, load_spot_count, self.unload_spot[assigned_unload_spot], self.load_spot[assigned_load_spot], entry_truck_count, exit_truck_count, spot_wait_time, unload_progress_truck_count, load_progress_truck_count, self.visible, self.container_status, self.container_size]
                unload_load_trucks_completed.append(new_data)

            # else:
            elif select_operation =='load':
                # 반출 작업장 이동
                entry_to_load_move = 5
                yield env.timeout(entry_to_load_move)
                print(f"트럭 {self.name}이 반출장소에 도착했습니다. 시간: {env.now}")
                arrive_load_spot_time = env.now
                print(self.load_spot[assigned_load_spot])
                load_spot_count = len(self.load_spot[assigned_load_spot].queue)
                unload_spot_count = 0
                unload_progress_truck_count = self.unload_spot[assigned_unload_spot].count
                load_progress_truck_count = self.load_spot[assigned_load_spot].count
                print(f"현재 반출장소에서 대기 중인 차량의 수: {len(self.load_spot[assigned_load_spot].queue)}")
                ## 앞 차 있을 시 대기
                with self.load_spot[assigned_load_spot].request() as req:
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
                    if self.container_size == 'small':
                        out_work_time = random.randint(18,25)
                    elif self.container_size =='medium':
                        out_work_time = random.randint(13,20)
                    else:
                        out_work_time = random.randint(10,15)
                    if self.container_status == 'long-term':
                        out_work_time +=3
                    elif self.container_status =='fresh':
                        out_work_time -=3
                        
                    yield env.timeout(out_work_time)
                    print(f"트럭 {self.name}이(가) 반출 작업을 완료했습니다. 시간: {env.now}")
                    complete_load_work_time = env.now

                # exit gate 이동
                out_before_wait_time = 5
                yield env.timeout(out_before_wait_time)
                exit_truck_count = self.out()
                print(f"트럭 {self.name}이(가) 출차했습니다. 시간: {env.now}")
                out_yard_time = env.now

                in_yard_time = waiting_times[self.name]
                print('key', in_yard_time)
                waiting_time = out_yard_time- in_yard_time
                result_waiting.append(waiting_time)
                

                print(f"트럭 {self.name}의 입차~출차시간: {waiting_time}")
                spot_wait_time = load_spot_wait_time
                new_data = [self.name, "load", in_yard_time, arrive_unload_spot_time, self.end_wait_start_unload_work, complete_unload_work_time, arrive_load_spot_time, self.end_wait_start_load_work, complete_load_work_time, out_yard_time, waiting_time, select_operation, unload_spot_count, load_spot_count, self.unload_spot[assigned_unload_spot], self.load_spot[assigned_load_spot], entry_truck_count, exit_truck_count, spot_wait_time, unload_progress_truck_count, load_progress_truck_count, self.visible, self.container_status, self.container_size]
                load_trucks_completed.append(new_data)
            # self.in_progress_trucks.remove(self.name)
    
   
    env = simpy.Environment()
    # unload_spot = simpy.Resource(env, capacity=5)
    ## 객체 하나를 만들고 capacity를 5개 부여하려고 했으나, 이렇게 하면 블록 구분이 안됨.
    ## 따라서 객체를 5개 만들어야 함
    unload_spot = {'a': simpy.Resource(env, capacity=1),
                    'b': simpy.Resource(env, capacity=1),
                    'c': simpy.Resource(env, capacity=1),
                    'd': simpy.Resource(env, capacity=1),
                    'e': simpy.Resource(env, capacity=1)}
    # load_spot = simpy.Resource(env, capacity=5)
    load_spot = {'f': simpy.Resource(env, capacity=1),
                    'g': simpy.Resource(env, capacity=1),
                    'h': simpy.Resource(env, capacity=1),
                    'i': simpy.Resource(env, capacity=1),
                    'j': simpy.Resource(env, capacity=1)}



    arrival_interval = random.randint(2,4)  # 트럭 도착 주기 (분 단위)
    unload_trucks_completed = []
    load_trucks_completed = []
    waiting_times = {}
    result_waiting = []
    unload_load_trucks_completed = []
    operation = ['unload', 'load', 'both']
    end_wait_start_unload_work = 0
    end_wait_start_load_work = 0
    container_status = ['fresh', 'long-term', 'short-term']
    container_size = ['small','medium', 'large']

    visible = True
    # 트럭 대수
    arrival_interval =0
    for i in range(trucknum):
        arrival_time = random.randint(2,4)
        arrival_interval += arrival_time
        Truck(env, i+1, arrival_interval, unload_trucks_completed, load_trucks_completed, unload_load_trucks_completed, operation
            , unload_spot, load_spot, end_wait_start_unload_work, end_wait_start_load_work, visible, container_status, container_size)

    ### 파일에 저장되는 데이터 개수와 관련됨
    env.run(until=processtime)  # 시뮬레이션 시간 (분 단위)
    print('********************')
    print('result_waiting' + str(sum(result_waiting)))
    # 결과를 저장할 CSV 파일 이름
    csv_filename = "data/truck_simulation_results.csv"

        # CSV 파일에 결과를 기록하는 함수
    def save_results_to_csv(filename, unload_trucks_completed, load_trucks_completed, unload_load_trucks_completed):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["number", "code", "entryTime", "arrive_unload_spot", "start_unload_work", "complete_unload_work", "arrive_load_spot", "start_load_work", "complete_load_work", "out_time", "work_time", "op", "unload_count", "load_count", "unload_block", "load_block", 'entry_count', 'exit_count', 'spot_wait_time', 'unload_progress_truck_count', 'load_progress_truck_count', 'visible', 'container_status', 'container_size'])  # entry_count(16)
            #                     1       2         3            4                          5                   6                       7                   8                   9               10              11       12       13             14             15           16             17              18              19          20                              21                                    
            # 반입 작업 완료 트럭 기록
            for truck in unload_trucks_completed:
                writer.writerow([truck[0], truck[1], truck[2], truck[3], truck[4], truck[5], truck[6], truck[7], truck[8], truck[9], truck[10], truck[11], truck[12], truck[13], truck[14], truck[15], truck[16], truck[17], truck[18], truck[19], truck[20], truck[21], truck[22], truck[23]])
                #print(truck[0], truck[1], truck[2], truck[3], truck[4], truck[5], truck[6], truck[7], truck[8], truck[9], truck[10], truck[11], truck[12], truck[13], truck[14], truck[15], truck[16], truck[17], truck[18], truck[19], truck[20], truck[21])

            # 반출 작업 완료 트럭 기록
            for truck in load_trucks_completed:
                writer.writerow([truck[0], truck[1], truck[2], truck[3], truck[4], truck[5], truck[6], truck[7], truck[8], truck[9], truck[10], truck[11], truck[12] , truck[13], truck[14], truck[15], truck[16], truck[17], truck[18], truck[19], truck[20], truck[21], truck[22], truck[23]])

            # 반입+반출 작업 완료 트럭 기록
            for truck in unload_load_trucks_completed:
                writer.writerow([truck[0], truck[1], truck[2], truck[3], truck[4], truck[5], truck[6], truck[7], truck[8], truck[9], truck[10], truck[11], truck[12] , truck[13], truck[14], truck[15], truck[16], truck[17], truck[18], truck[19], truck[20], truck[21], truck[22], truck[23]])

           

            print(f"반입 작업을 완료한 트럭 수: {len(unload_trucks_completed)}")
            print(f"반출 작업을 완료한 트럭 수: {len(load_trucks_completed)}")
            print(f"반입, 반출 작업을 완료한 트럭 수: {len(unload_load_trucks_completed)}")


    save_results_to_csv(csv_filename, unload_trucks_completed, load_trucks_completed, unload_load_trucks_completed)

    print(f"결과를 '{csv_filename}' 파일로 저장했습니다.")
    
if __name__=='__main__':
    trucknum = 10000
    processtime = 28800
    blocknum = 5
    make_simul_operate(trucknum, processtime, blocknum)

