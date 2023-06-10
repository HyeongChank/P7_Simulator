from flask import Flask, render_template, jsonify, request

# from complete import process_count_model
# from complete import process_model
# from DA import main
# from DA import Queue_LSTM
# from complete import cnn_predict
# from complete import lstm_retrain
# from complete import randomForest_predict
from DA import simulator_post_server
from DA import test
import json
import requests
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    
# @app.route('/api/cnn_time_predict', methods=['GET', 'POST'])
# def cnn_prediction():
#     if request.method == 'POST':
#         print('******************request in*********************')
#         time_group, predict_group, actual_group = process_model.operate()
        
#         return jsonify({'time': time_group, 'predict_group': predict_group, 'actual_group': actual_group})
#     else:
#         return 'error'

# @app.route('/api/cnn_count_predict', methods=['GET', 'POST'])
# def cnn_count_prediction():
#     if request.method == 'POST':
#         print('******************request in*********************')
#         time_group, predict_group, actual_group = process_count_model.operate()
        
#         return jsonify({'time': time_group, 'predict_group': predict_group, 'actual_group': actual_group})
#     else:
#         return 'error'
    

# @app.route('/api/r_predict', methods=['GET', 'POST'])
# def r_prediction():
#     if request.method == 'POST':
#         # new_data = request.get_json()
#         # print('json 전달 받은 데이터', new_data)
#         # new_data_df = pd.DataFrame(new_data)
        
#         grouped_df = randomForest_predict.operate()
#         grouped_df_json = grouped_df.to_json(date_format='iso', orient='records')
#         grouped_df_parsed = json.loads(grouped_df_json)
#         grouped_df_clean = json.dumps(grouped_df_parsed, ensure_ascii=False)
#         return jsonify({'grouped_df_json': grouped_df_clean})
#     else:
#         return 'error'
    

@app.route('/api/inputDataPost', methods=['GET', 'POST'])
def inputDataPost():
    if request.method == 'POST':
        input_data = request.get_json()
        trucknum = input_data['trucknum']
        processtime = input_data['processtime']
        blocknum = input_data['blocknum']
        print(trucknum, processtime, blocknum)
        test.make_simul_operate(trucknum, processtime, blocknum)
        json_output = simulator_post_server.operate()
        
        return jsonify({'json_output': json_output})
    else:
        return 'error'
    



@app.route('/api/simul_predict', methods=['GET', 'POST'])
def simul_prediction():
    if request.method == 'POST':
        print('**********request in')
        json_output = simulator_post_server.operate()
        # Convert float32 to native Python float
        
        
        return jsonify({'json_output': json_output})
    else:
        return 'error'




if __name__ == '__main__':
    # host, port를 설정하고 여기로 요청을 하게 하면 됨
    app.run(host='0.0.0.0', port=5000, debug=True)