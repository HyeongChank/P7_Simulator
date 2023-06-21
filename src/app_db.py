from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from DA import crawling_congest
import schedule
import time
import threading
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/crawlingcongest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# db 연결(table 생성)
class CongestData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trminlCode = db.Column(db.String(50))
    vesselStatusStr = db.Column(db.String(50))
    vesselStatus = db.Column(db.String(50))
    inoutStatusStr = db.Column(db.String(50))
    inoutStatus = db.Column(db.String(50))
    updtData = db.Column(db.String(50))

    def __init__(self, trminlCode, vesselStatusStr, vesselStatus, inoutStatusStr, inoutStatus, updtData):
        self.trminlCode = trminlCode
        self.vesselStatusStr = vesselStatusStr
        self.vesselStatus = vesselStatus
        self.inoutStatusStr = inoutStatusStr
        self.inoutStatus = inoutStatus
        self.updtData = updtData
    


@app.route('/api/crawlingdata', methods=['GET', 'POST'])
def crawling():
    trminlCode, vesselStatusStr, vesselStatus, inoutStatusStr, inoutStatus, updtData = crawling_congest.get_data()
    return f"Data: {trminlCode}, {vesselStatus}, {vesselStatusStr}, {inoutStatusStr}, {inoutStatus}, {updtData}"
def scheduled_crawling():
    with app.app_context():
        trminlCode, vesselStatusStr, vesselStatus, inoutStatusStr, inoutStatus, updtData = crawling_congest.get_data()
        # 데이터베이스에 저장
        data = CongestData(trminlCode, vesselStatusStr, vesselStatus, inoutStatusStr, inoutStatus, updtData)
        try:
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            print(e)

# schedule
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)
    
 

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    schedule.every(10).minutes.do(scheduled_crawling)
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()
    # host, port를 설정하고 여기로 요청을 하게 하면 됨
    app.run(host='0.0.0.0', port=5000, debug=True)