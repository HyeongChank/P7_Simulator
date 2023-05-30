from flask import Flask, render_template, jsonify, request

from DA import quarter
from DA import test2
from DA import congestAnal
from DA import main
from DA import retraining
from DA import predict_LSTM
from DA import Queue_LSTM
from DA import cnn_predict
from complete import randomForest_predict
import json
import requests
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    
@app.route('/api/congest2', methods=['GET', 'POST'])
def congestion():
    if request.method == 'POST':
        new_data = request.get_json()
        print('json 전달 받은 데이터', new_data)
        new_data_df = pd.DataFrame(new_data)
        waitingTime, congest_level = main.commit_model(new_data_df)
        
        return jsonify({'congest_level': congest_level.tolist()}, {'waiting_time': waitingTime.tolist()})
    else:
        return 'error'

@app.route('/api/predict', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # new_data = request.get_json()
        # print('json 전달 받은 데이터', new_data)
        # new_data_df = pd.DataFrame(new_data)

        predicted_data_unload, predicted_data_load = Queue_LSTM.postdata()
        return jsonify({'predicted_data_unload': predicted_data_unload}, {'predicted_data_load': predicted_data_load})
    else:
        return 'error'
    

@app.route('/api/r_predict', methods=['GET', 'POST'])
def r_prediction():
    if request.method == 'POST':
        # new_data = request.get_json()
        # print('json 전달 받은 데이터', new_data)
        # new_data_df = pd.DataFrame(new_data)
        
        grouped_df = randomForest_predict.operate()
        grouped_df_json = grouped_df.to_json(date_format='iso', orient='records')
        grouped_df_parsed = json.loads(grouped_df_json)
        grouped_df_clean = json.dumps(grouped_df_parsed, ensure_ascii=False)
        return jsonify({'grouped_df_json': grouped_df_clean})
    else:
        return 'error'
    

@app.route('/api/cnn_predict', methods=['GET', 'POST'])
def cnn_prediction():
    if request.method == 'POST':
        
        time_group, predict_group, actual_group = cnn_predict.operate()
        
        return jsonify({'time': time_group, 'predict_group': predict_group, 'actual_group': actual_group})
    else:
        return 'error'

if __name__ == '__main__':
    # host, port를 설정하고 여기로 요청을 하게 하면 됨
    app.run(host='10.125.121.220', port=5001, debug=True)