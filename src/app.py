from flask import Flask, render_template, jsonify, request

from DA import simulator_post_server
from DA import test
import json
import requests
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.update(
    CELERY_BROKER_URL='amqp://localhost//',
    CELERY_RESULT_BACKEND='rpc://'
)

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