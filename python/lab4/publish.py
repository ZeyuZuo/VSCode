import random
from paho.mqtt import client as mqtt_client 
import json  
import time 

# MQTT服务器的配置参数
broker = '127.0.0.1'  # MQTT代理服务器的IP地址
port = 1883  # MQTT使用的端口号，默认为1883
topics = {
    "sensor/temperature": "sensor/temperature",
    "sensor/humidity": "sensor/humidity",
    "sensor/pressure": "sensor/pressure"
}  # MQTT主题，用于发布消息
client_id = f'python-mqtt-{random.randint(0, 1000)}'  # 客户端ID，随机生成以避免冲突

def generate_sensor_data():
    data = {
        "sensor/temperature": random.uniform(20.0, 30.0),  # 模拟温度数据，单位摄氏度
        "sensor/humidity": random.uniform(30.0, 90.0),  # 模拟湿度数据，百分比
        "sensor/pressure": random.uniform(1000.0, 1020.0)  # 模拟气压数据，单位hPa
    }
    return data

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}\n")

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    try:
        while True:
            sensor_data = generate_sensor_data()  # 生成模拟的传感器数据
            for topic, value in sensor_data.items():
                message = json.dumps({topic: value})
                result = client.publish(topic, message)
                status = result[0]
                if status == 0:
                    print(f"Send `{message}` to topic `{topic}`")
                else:
                    print(f"Failed to send message to topic {topic}")
            time.sleep(5)  # 每5秒发送一次数据
    except KeyboardInterrupt:
        print("Publishing stopped by user")

def run():
    client = connect_mqtt()
    client.loop_start()
    try:
        publish(client)
    finally:
        client.loop_stop() 

if __name__ == '__main__':
    run()
