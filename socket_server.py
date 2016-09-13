#!/usr/bin/python
#encoding:utf-8

# 创建一个小型的服务器
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #生成Socket对象
# host = socket.gethostname() #获取服务器名称
# port = 1234
# s.bind((host,port)) #绑定服务器Socket地址
# s.listen(5) #开始监听
# while True:
	# c,addr = s.accept() #接受一个连接,addr为连接对端地址，c为生成的连接对象
	# print '连接来自:' ,addr 
	# c.send('test:一个简单的服务器创建成功！') #发送一个数据
	# c.close() #关闭连接


使用SocketServer创建一个小型服务器
from SocketServer import TCPServer,StreamRequestHandler
class Handler(StreamRequestHandler):
	def handle (self):	#重载处理方法
		addr = self.request.getpeername()#获取连接对端地址
		print '获取的连接来自：',addr
		self.wfile.write('test:连接成功！') #发送数据
server = TCPServer(('',1234),Handler) #生成TCP服务器
server.serve_forever() #开始监听并处理连接
		

