import json
import socket

def run():
    count = 0
    start = -1
    end = -1
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ("10.26.44.17", 8888)  
    udp_socket.bind(local_addr)
    while(True):
        recv_data = udp_socket.recvfrom(1024) 
        count = count + 1
        data = json.loads(recv_data[0].decode("utf-8"))
        if(start == -1):
            start = data['time']
        end = data['time']
        print(count)
        
    udp_socket.close()


if __name__ == '__main__':
    run()