#encoding:utf-8

#�����ͻ���
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #����һ��Socket����
host = socket.gethostname()
port = 1234
s.connect((host,port))
print s.recv(1024)
s.close()
