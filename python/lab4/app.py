from flask import Flask, jsonify
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

@app.route('/data')
def data():
    sensor_data = get_data()
    result = {'sensor/temperature': [], 'sensor/humidity': [], 'sensor/pressure': [], 'alerts': []}
    alerts = []
    for timestamp, sensor_type, value in sensor_data:
        formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        # 检查是否触发警报,条件为：
        # 温度 > 35°C 或 < 10°C
        # 湿度 > 80% 或 < 20%
        # 气压 > 1025 hPa 或 < 990 hPa
        # alert_condition = (
        #     (sensor_type == 'sensor/temperature' and (value > 35 or value < 10)) or
        #     (sensor_type == 'sensor/humidity' and (value > 80 or value < 20)) or
        #     (sensor_type == 'sensor/pressure' and (value > 1025 or value < 990))
        # )
        # if alert_condition:
        #     alert_message = f"Alert: {sensor_type} at {formatted_timestamp} is {value}"
        #     alerts.append(alert_message)
        #     send_dingtalk_message(alert_message, sensor_type, timestamp, value)
        result[sensor_type].append({'timestamp': formatted_timestamp, 'value': value})
    
    if alerts:
        result['alerts'] = alerts
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
