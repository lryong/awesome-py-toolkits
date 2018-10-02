#encoding:utf-8

#创建客户端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个Socket对象
host = socket.gethostname()
port = 1234
s.connect((host,port))
print s.recv(1024)
s.close()
