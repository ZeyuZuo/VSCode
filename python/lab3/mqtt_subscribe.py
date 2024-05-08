# python 3.11

import random
from datetime import datetime
from paho.mqtt import client as mqtt_client
import json


broker = '127.0.0.1'
port = 1883
topic = "zzy/mqtt"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
username = 'zzy'
password = '123456'

count=0
start_time=-1
end_time=-1

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    global count
    global start_time
    def on_message(client, userdata, msg):
        global count
        global start_time
        count = count + 1
        msg = msg.payload.decode()
        msg = json.loads(msg)
        if(start_time==-1):
            start_time=datetime.strptime(msg['time'], '%Y-%m-%d %H:%M:%S.%f')
        end_time=datetime.utcnow()
        print(msg)
        if(count == 100000):
            print("发送的消息", msg)
            print("start time: ", start_time)
            print("end time: ", end_time)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
