import random
import json
import mysql.connector
from mysql.connector import Error
from paho.mqtt import client as mqtt_client
from dingtalkchatbot.chatbot import DingtalkChatbot

# MQTT服务器的配置参数
broker = '127.0.0.1'
port = 1883
topics = {
    "sensor/temperature": "sensor/temperature",
    "sensor/humidity": "sensor/humidity",
    "sensor/pressure": "sensor/pressure"
}
client_id = f'subscribe-{random.randint(0, 100)}'

# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'zzy123456',
    'database': 'SensorData'
}

def send_dingtalk_message(message):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=54803e6bdc1a0bc438ecc97c1ace78f2eb7dfe101298ab24682618429cc0c320'
    secret = 'SECbc64bc7f21cc7aba5cb444dbdedfd82b14aea021229f654c22c199a255c39cd5'  # 可选：创建机器人勾选“加签”选项时使用
    xiaoding = DingtalkChatbot(webhook, secret=secret)
    xiaoding.send_text(msg=message)

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            # 订阅所有配置的主题
            for topic in topics.values():
                client.subscribe(topic)
        else:
            print(f"Failed to connect, return code {rc}\n")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def store_data(sensor_type, value):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO sensor_data (timestamp, sensor_type, value) VALUES (NOW(), %s, %s)"
        cursor.execute(query, (sensor_type, value))
        conn.commit()
        cursor.close()
        conn.close()
        print("Data stored successfully")
    except Error as e:
        print(f"Error: {e}")

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        data = json.loads(msg.payload.decode())
        for sensor, value in data.items():
            store_data(sensor, value)
            # 检查是否触发警报,条件为：
            # 温度 > 35°C 或 < 10°C
            # 湿度 > 80% 或 < 20%
            # 气压 > 1025 hPa 或 < 990 hPa
            alert_condition = (
                (sensor == 'sensor/temperature' and (value > 35 or value < 10)) or
                (sensor == 'sensor/humidity' and (value > 80 or value < 20)) or
                (sensor == 'sensor/pressure' and (value > 1025 or value < 990))
            )
            if alert_condition:
                alert_message = f"Alert: {sensor} is {value}"
                send_dingtalk_message(alert_message)
        

    client.on_message = on_message

def run():
    client = connect_mqtt()  # 连接到MQTT服务器
    subscribe(client)  # 订阅MQTT主题
    client.loop_forever()  # 进入循环，等待接收消息

if __name__ == '__main__':
    run()
