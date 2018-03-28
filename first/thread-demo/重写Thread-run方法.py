#_*_coding:utf-8 _*_
from threading import Thread
import time
class Mythread(Thread):            #因为这里有继承所以此时的run方法优先级高于Thread里的run
    def run(self):
        time.sleep(2)
        print '我是线程'
        #Thread.run(self)        #打开后会执行run bar     调用了父类的run方法


def bar():           #这个函数不能定义在class同级 因为他不属于class
    print 'bar'

t1 = Mythread(target=bar)    #target 从Therad 继承来的构造函数
t1.start()
print 'over'
