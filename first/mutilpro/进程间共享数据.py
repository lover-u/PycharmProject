#!/user/bin/python
#_*_coding:utf-8 _*_
from multiprocessing import Process,Queue    #这里的Queue是multiprocessing里面的自带queue模块，跟Queue模块有区别，应该会有继承关系
import Queue as Q2

def f(q,n):
    q.put([n,'hello'])                   #注意get是随机拿一条   所以这个例子是进程间共享数据

if __name__ == '__main__':
    q = Queue()
    #q = Q2.Queue()
    for i in range(5):
        p = Process(target=f,args=(q,i))
        p.start()
    while True:
        print q.get()
for i in range(5):
    print i