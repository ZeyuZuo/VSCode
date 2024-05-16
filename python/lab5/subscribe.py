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
    "temperature": "temperature",
    "humidity": "humidity",
    "pressure": "pressure"
}
client_id = f'subscribe-{random.randint(0, 100)}'

# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'zzy123456',
    'database': 'SensorData'
}

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
        # sensor_type去掉引号
        sensor_type = sensor_type.replace("'", "")
        cursor = conn.cursor()
        
        query = "INSERT INTO " + sensor_type + " (value) VLAUES(" + str(value) + ")"
        print(query)
        cursor.execute(query)
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
        

    client.on_message = on_message

def run():
    client = connect_mqtt()  # 连接到MQTT服务器
    subscribe(client)  # 订阅MQTT主题
    client.loop_forever()  # 进入循环，等待接收消息

if __name__ == '__main__':
    run()
