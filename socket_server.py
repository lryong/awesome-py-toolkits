#!/usr/bin/python
# -*- coding:utf-8 -*-


# 使用SocketServer创建一个小型服务器
from SocketServer import TCPServer,StreamRequestHandler
class Handler(StreamRequestHandler):
	def handle (self):	#重载处理方法
		addr = self.request.getpeername()#获取连接对端地址
		print '获取的连接来自：',addr
		self.wfile.write('test:连接成功！') #发送数据
server = TCPServer(('',1234),Handler) #生成TCP服务器
server.serve_forever() #开始监听并处理连接


