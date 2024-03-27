import socket
import random
import json
from datetime import datetime

def main ():
    for i in range(0,30):
        temper=random.randint(-30,50)

        send_data={
            "device":"test",
            "time":str(i),
            "temperature":str(temper)
            }
        send_data=json.dumps(send_data)
        print(send_data)

        #  创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #   发送数据（数据，(ip,端口)）
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 8888))
        #  关闭套接字
        udp_socket.close()


if __name__ == '__main__':
    main()
