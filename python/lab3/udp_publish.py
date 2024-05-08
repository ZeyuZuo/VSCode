import socket
from datetime import datetime
import random
import json

def run():
    for i in range(1,100001):
        temper=random.randint(0,30)

        send_data={
            "device":"test",
            "time":str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]),
            "temperature":str(temper),
            "count":str(i)
            }
        send_data=json.dumps(send_data)
        # print(send_data)

        #  创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #   发送数据（数据，(ip,端口)）
        udp_socket.sendto(send_data.encode("utf-8"), ("10.26.44.17", 8888))
        #  关闭套接字
        udp_socket.close()

if __name__ == '__main__':
    run()
