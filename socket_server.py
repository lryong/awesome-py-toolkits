#!/usr/bin/python
# -*- coding:utf-8 -*-


# ʹ��SocketServer����һ��С�ͷ�����
from SocketServer import TCPServer,StreamRequestHandler
class Handler(StreamRequestHandler):
	def handle (self):	#���ش�����
		addr = self.request.getpeername()#��ȡ���ӶԶ˵�ַ
		print '��ȡ���������ԣ�',addr
		self.wfile.write('test:���ӳɹ���') #��������
server = TCPServer(('',1234),Handler) #����TCP������
server.serve_forever() #��ʼ��������������


