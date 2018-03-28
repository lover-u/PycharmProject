#!/user/bin/python
#_*_coding:utf-8 _*_
import threading
import time
lock = threading.Lock()
global num     #这里不加global会报错，因为下面的局部要声明的变量num被全局变量num占用了
num = 0
'''
def run(n):
    lock.acquire()
    time.sleep(1)
    global num
    num +=1
    #print '%s\n' %num                 #这行在这的时候就是顺序打印  放在下面则不是，因为这个时候打印锁还没有释放  所以会是顺序打印
    lock.release()
    time.sleep(0.01)
    print '%s\n' % num              #这里也是顺序打印 为什么  因为CPU在分片时只执行100条CPU指令 注意是CPU指令 一行代码可能会有N条CPU指令
'''
#run('dd')

def run(n):
    time.sleep(1)
    global num
    semp.acquire()
    time.sleep(0.001)
    num +=1
    #print '%s\n' %num                 #这行在这的时候就是顺序打印  放在下面则不是，因为这个时候打印锁还没有释放  所以会是顺序打印
    semp.release()
    #time.sleep(0.01)
    print '%s' %num                          #这个时候屏幕输出就会乱了，因为有多个线程在抢着输出


semp = threading.BoundedSemaphore(4)    #允许的信号量，意思是最对允许4个来抢

#lock = threading.Lock()     #在这里报错了  放到上面OK， 注意解释顺序
for i in range(200):
    t = threading.Thread(target=run,args=(i,))
    t.start()

'''  这么些会一直自己等待自己释放锁，会一直卡住
def run(n):
    time.sleep(1)
    global num
    global num2
    lock.acquire()
    num +=1
    lock.acquire()
    num2 +=1
    #print '%s\n' %num                 #这行在这的时候就是顺序打印  放在下面则不是，因为这个时候打印锁还没有释放  所以会是顺序打印
    lock.release()
    lock.release()
    time.sleep(0.01)
    print '%s\n' % num  
    
def run(n):
    time.sleep(1)
    global num
    global num2
    lock.acquire()
    num +=1
    lock.acquire()
    num2 +=1
    #print '%s\n' %num                 #这行在这的时候就是顺序打印  放在下面则不是，因为这个时候打印锁还没有释放  所以会是顺序打印
    lock.release()
    lock.release()
    time.sleep(0.01)
    print '%s\n' % num  
lock = threading.RLock()    RLock递归锁  这种可以同一个宿主同时上多个锁
    
        
    
'''