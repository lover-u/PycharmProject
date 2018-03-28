#_*_coding:utf-8 _*_
import os
import socket        #这个程序是阻塞的，只能支持一个链接 ！
#sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print sk
sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen(5)
#conn,address = sk.accept()      #这里的conn 代指一个变量  指连接来的客户端  是一个自带的变量  address 才是IP和port
#conn.send('hello')
#conn.close()

    #这个会一直打开socket 占用端口
while True:
    result = sk.accept()
    print result
    print type('result')
    #conn = result[0]
    #address = result[1]
    conn.send('hello.')
    flag = True
    while True:
        data = conn.recv(1024)
        print data
        if data == 'exit':
            flag = False
        conn.send('sb')
    conn.close()


'''
while True:
    conn,address = sk.accept()
    conn.send('hello.')
    conn.close()
'''



#[10048] = "The network address is in use."   注意会报这个错误