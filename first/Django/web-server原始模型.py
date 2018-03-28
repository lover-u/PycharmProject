#!/usr/bin/env python
#coding:utf-8

from wsgiref.simple_server import make_server



'''
根据获取的URL的不同匹配到不同路径
if userUrl == '/index/':
    return '<h1>index</h1>'
elif userUrl == '/login/':
    return '<h1>login</h1>'
elif userUrl == '/logout/':
    return '<h1>logout</h1>'
elif userUrl == '/welcome/':
    return '<h1>welcome</h1>'
else:
    return '<h1>404 not found</h1>'
'''

def login():
    return 'login'
def logout():
    return 'logout'
def man():
    return 'man'

url = (
    ('/login/',login),
    ('/man/',man),
    ('logout',logout),
 )

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    userUrl = environ['PATH_INFO']  # 获取environ下的PATH_INFO参数的具体值   值来自客户端

    func = None
    for item in url:
        if item[0] == userUrl:
            func = item[1]
            break  # 找到之后不再继续找   #

    if func:
        result = func()                       # ？？？注意这里
    else:
        result = '404'
        return result
    result = func()
    return result
    #return '<h1>Hello, web!</h1>'

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()


#  mvc   业务处理通过controller 去做  数据库 操作方到 model 里  HTML js等的页面代码放到view里去做