#_*_coding:utf-8 _*_
import socket
import select
def handle_request(client):
    buf = client.recv(1024)
    #client.send("HTTP/1.1 200 OK \r\n")
    #client.send("Content-Type:text/html\r\n\r\n")
    client.send("<a bref='www.baidu.com'> Hello World </a>")      #返回带有A标签内容


def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)

    while True:
        connection,address = sock.accept()
        handle_request(connection)
        connection.close()

if __main__ == '__main__':
    main()