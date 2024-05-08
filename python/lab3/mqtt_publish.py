import random
import time
from datetime import datetime
import json

from paho.mqtt import client as mqtt_client


broker = '47.236.122.23'
port = 1883
topic = "zzy/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'zzy'
password = '123456'

def connect_mqtt():
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


def publish(client):
    msg_count = 1
    # print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    while True:
        temper=random.randint(0,30)
        msg = {
            "device":"test",
            "time":str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]),
            "temperature":str(temper),
            "count":str(msg_count)
            }
        send_data=json.dumps(msg)
        # print(send_data)
        result = client.publish(topic, send_data)
        # result: [0, 1]
        status = result[0]
        # if status == 0:
        #     print(f"Send `{msg}` to topic `{topic}`")
        # else:
        #     print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 100000:
            # print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()
