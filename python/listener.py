import socket


def main ():
    # 1 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2 绑定本地信息
    local_addr = ("127.0.0.1", 8080)  # ip不写表示 任何ip
    udp_socket.bind(local_addr)
    while True:
        # 3 等待接收
        recv_data = udp_socket.recvfrom(1024)  # 1024 表示本次接收的最大字节数 ,recv 只是接受数据,recvfrom 接受数据和 对方ip 端口
        # 4 显示接收数据
        print(recv_data.decode("gbk"))
    # 5 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

