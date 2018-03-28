#!/user/bin/python
#_*_coding:utf-8 _*_
import threading,time,Queue,random
def producer(name,que):
    while True:
        if que.qsize()  <3:
            que.put('baozi')
            print '%s made a baozi...++++++++++++++++++' %name
        time.sleep(random.randrange(5))

def consumer(name,que):
    while True:
        try:
            que.get_nowait()                    #在不加等待_nowait的情况下，这个看不出来效果，因为有一部分取不到包子的线程实际在阻塞
            print '%s got a baozi...' %name
        except Exception:
            print u'没有包子了'              #不加异常处理的话程序就退出了
        time.sleep(random.randrange(3))
q = Queue.Queue()
p1 = threading.Thread(target=producer,args=['hehe1',q])
p2 = threading.Thread(target=producer,args=['hehe2',q])
p1.start()
p2.start()

c1 = threading.Thread(target=consumer,args=['haha1',q])
c2 = threading.Thread(target=consumer,args=['haha2',q])
c1.start()
c2.start()