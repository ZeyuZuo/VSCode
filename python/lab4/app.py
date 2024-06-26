from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from dingtalkchatbot.chatbot import DingtalkChatbot
import requests
import json
from datetime import datetime

app = Flask(__name__)

# 数据库配置
db_config = {
    'user': 'root',
    'password': 'zzy123456',
    'host': 'localhost',
    'database': 'SensorData',
    'raise_on_warnings': True
}

def get_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, sensor_type, value FROM sensor_data ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()
    return data

def send_dingtalk_message(message, sensor_type, timestamp, value):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=54803e6bdc1a0bc438ecc97c1ace78f2eb7dfe101298ab24682618429cc0c320'
    secret = 'SECbc64bc7f21cc7aba5cb444dbdedfd82b14aea021229f654c22c199a255c39cd5'  # 可选：创建机器人勾选“加签”选项时使用
    xiaoding = DingtalkChatbot(webhook, secret=secret)
    msg = 'Alert: ' + message + ' at ' + timestamp.strftime('%Y-%m-%d %H:%M:%S') + ' is ' + str(value) + ' !'
    xiaoding.send_text(msg=msg)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # 允许所有来源访问，也可以设置为具体的来源
    return response

@app.route('/data')
def data():
    sensor_data = get_data()
    result = {'sensor/temperature': [], 'sensor/humidity': [], 'sensor/pressure': [], 'alerts': []}
    alerts = []
    for timestamp, sensor_type, value in sensor_data:
        formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        result[sensor_type].append({'timestamp': formatted_timestamp, 'value': value})
    
    if alerts:
        result['alerts'] = alerts
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
