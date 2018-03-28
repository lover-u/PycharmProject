#!/usr/bin/python
#coding:utf-8
import StringIO
import pycurl
import sys
import os
class urlpass:
    def __init__(self):
        self.contents = ''
    def body_callback(self,buf):
        self.contents = self.contents + buf
def urlgzip(input_url):
    t = urlpass()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)#响应代码
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)#远程服务器连接时间
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)#连接上后开始传输的时间
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)#接收第一个字节的时间
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)#上一请求总时间
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)#下载数据大小
    #print 'http_code http_size conn_time pre_tran start_tran total_time'
    return "http_code:%d,http_size:%d,conn_time:%f,pre_tran:%f,start_tran:%f,total_time:%f"%(http_code,http_size,http_conn_time,http_pre_tran,http_start_tran,http_total_time)
if __name__ == '__main__':
    #input_url = sys.argv[1]
    input_url='http://los-cn-north-1.lecloudapis.com/monitor-s3/monitor'
    urlinfo=urlgzip(input_url)
    print type(urlinfo)
    print urlinfo