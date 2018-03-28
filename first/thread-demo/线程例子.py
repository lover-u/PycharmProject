
#_*_coding:utf-8 _*_
'''
import thread, time, random
count = 0
def threadTest():
    global count
    for i in xrange(10000):
        count += 1
for i in range(10):
    thread.start_new_thread(threadTest, ())
time.sleep(3)
print count
'''
import time
from threading  import Thread
def foo(arg):
    print arg
    for item in range(10):
        print item
        time.sleep(1)

print 'before'
t1 = Thread(target=foo,args=(1,))    #加逗号更能说明这是一个序列    Therad的固定用法 利用target建立与函数之间的联系
t1.setDaemon(True)
t1.start()
t1.join(5)    #作用是在这等待子进程执行完后再接着执行，里面可以设置超时时间 ，比如最多等待5秒   只要有join就会等待
#run()


print t1.getName()     #获取线程的名字
#t1.setDaemon(True)        #写在这里会报错的，要在start 之前
print t1.isDaemon()    #获取线程是否等待  检测是否等待
print 'after'

t2 = Thread(target=foo,args=(1,))
t2.start()
print t2.getName()
print 'after'

print '主程序解析完毕'
#多线程同时进行  数字输出两份     现在这种是等子进程结束主进程才退出的 set之后主进程结束 子进程依然继续，然后子进程执行完随主进程一块销毁

