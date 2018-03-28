#_*_coding:utf-8 _*_

from threading import Thread
from Queue import Queue
import time

class producer(Thread):
#    def __init__(self, group=None, target=None, name=None,
#                 args=(), kwargs=None, verbose=None):                 #重写Thread的构造函数
    def __init__(self,name,queue):
        '''
        @param name : 生产者的名称
        @param queue: 容器
        '''
        self.__name = name
        self.__Queue = queue                     #重写构造函数 不一定会成功
        super(producer,self).__init__()          #继承父类的构造函数
    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('baozi')
                time.sleep(1)
                print '%s 生产了一个包子' %(self.__name)
        self.__Queue.put('baozi')
        Thread.run(self)

class consumer(Thread):
    def __init__(self,name,queue):
        self.__name = name
        self.__Queue = queue
        super(consumer, self).__init__()
    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                self.__Queue.get()
                time.sleep(1)
                print '%s 消费了一个包子' % (self.__name)
        self.__Queue.get()
        Thread.run(self)

queue = Queue(maxsize=10)   #先进先出  负责线程安全
pro1 = producer('pro1',queue)
pro1.start()                            #start方法需要父类构造函数的一些东西
pro2 = producer('pro2',queue)
pro2.start()
pro3 = producer('pro3',queue)
pro3.start()


for item in range(20):
    name = 'lm%d' %(item,)
    temp = consumer(name,queue)
    temp.start()


#线程栈就像是弹夹  后进先出    队列是先进先出
queue = Queue(maxsize=10)   #先进先出  负责线程安全
queue.put('1')
queue.put('2')
print queue.qsize()
print queue                #养成看类源码的习惯
print 'empty start:',queue.empty()
print 'get:',queue.get()   #默认取出第一个
print 'get:',queue.get()    #第二行取第二个
#print 'get:',queue.get()
print 'empty end:',queue.empty()