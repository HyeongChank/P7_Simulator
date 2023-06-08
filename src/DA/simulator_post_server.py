
import csv

def operate():
    file_path = 'data/predict_truck_simulation_results.csv'
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
   
    headers = data[0]
    rows = data[1:]
    json_data = [dict(zip(headers, row)) for row in rows]
    print(json_data)
    return json_data

if __name__=='__main__':
    operate()