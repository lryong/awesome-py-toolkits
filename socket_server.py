#!/usr/bin/python
#encoding:utf-8

# ����һ��С�͵ķ�����
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #����Socket����
# host = socket.gethostname() #��ȡ����������
# port = 1234
# s.bind((host,port)) #�󶨷�����Socket��ַ
# s.listen(5) #��ʼ����
# while True:
	# c,addr = s.accept() #����һ������,addrΪ���ӶԶ˵�ַ��cΪ���ɵ����Ӷ���
	# print '��������:' ,addr 
	# c.send('test:һ���򵥵ķ����������ɹ���') #����һ������
	# c.close() #�ر�����


ʹ��SocketServer����һ��С�ͷ�����
from SocketServer import TCPServer,StreamRequestHandler
class Handler(StreamRequestHandler):
	def handle (self):	#���ش�����
		addr = self.request.getpeername()#��ȡ���ӶԶ˵�ַ
		print '��ȡ���������ԣ�',addr
		self.wfile.write('test:���ӳɹ���') #��������
server = TCPServer(('',1234),Handler) #����TCP������
server.serve_forever() #��ʼ��������������
		

