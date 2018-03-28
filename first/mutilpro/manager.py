#!/user/bin/python
#_*_coding:utf-8 _*_
from multiprocessing import Process,Manager
def f(d,l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))

    p = Process(target=f,args=(d,l))
    p.start()
    p.join()

    print d
    print l

#在多线程里 线程安全需要自己加锁控制  但在多进程里 manager自己会控制锁 保证数据