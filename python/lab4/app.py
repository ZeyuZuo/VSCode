from flask import Flask, jsonify
import mysql.connector
import requests
import json

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'zzy123456',
    'host': '127.0.0.1',
    'database': 'mqtt',
    'raise_on_warnings': True
}

DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=54803e6bdc1a0bc438ecc97c1ace78f2eb7dfe101298ab24682618429cc0c320"

def getData():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data ORDER BY time DESC")
    data = cursor.fetchall()
    conn.close()
    return data

def send_dingtalk_message(message, sensor_type, timestamp, value):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    # 检查是否已发送过同一警告
    cursor.execute("SELECT id FROM sent_alerts WHERE sensor_type = %s AND timestamp = %s", (sensor_type, timestamp))
    if cursor.fetchone() is None:
        # 发送警告
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        data = {"msgtype": "text", "text": {"content": message}}
        response = requests.post(DINGTALK_WEBHOOK, headers=headers, data=json.dumps(data))
        print("DingTalk response:", response.text)
        # 记录警告
        cursor.execute("INSERT INTO sent_alerts (sensor_type, value, timestamp) VALUES (%s, %s, %s)", (sensor_type, value, timestamp))
        conn.commit()
    cursor.close()
    conn.close()

@app.route('/data')
def data():
    sensor_data = getData()
    result = {'sensor/temperature': [], 'sensor/humidity': [], 'sensor/pressure': [], 'alerts': []}
    alerts = []
    for timestamp, sensor_type, value in sensor_data:
        formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        # 检查是否触发警报,条件为：
        # 温度 > 35°C 或 < 10°C
        # 湿度 > 80% 或 < 20%
        # 气压 > 1025 hPa 或 < 990 hPa
        alert_condition = (
            (sensor_type == 'sensor/temperature' and (value > 35 or value < 10)) or
            (sensor_type == 'sensor/humidity' and (value > 80 or value < 20)) or
            (sensor_type == 'sensor/pressure' and (value > 1025 or value < 990))
        )
        if alert_condition:
            alert_message = f"Alert: {sensor_type} at {formatted_timestamp} is {value}"
            alerts.append(alert_message)
            send_dingtalk_message(alert_message, sensor_type, timestamp, value)
        result[sensor_type].append({'timestamp': formatted_timestamp, 'value': value})
    
    if alerts:
        result['alerts'] = alerts
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)