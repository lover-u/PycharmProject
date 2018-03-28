#_*_coding:utf-8 _*_

#异步处理 不占用CPU，比如IO操作  网络操作
import SocketServer       #主要是封装的该模块实现的功能


class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        print self.request, self.client_address, self.server
        # self.request = socket
        #

    def finish(self):
        pass


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()