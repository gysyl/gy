""" 
    粘包演示,接收
"""
import socket
import time
# 创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(("0.0.0.0",8888))

#设置监听
sockfd.listen(5)

connfd,addr = sockfd.accept()

while True:
    time.sleep(1)
    data = connfd.recv(1024)
    print(data.decode())
