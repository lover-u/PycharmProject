#!/user/bin/python
#_*_coding:utf-8 _*_
import threading,time,Queue,random
def producer():
    print 'p 等人来买包子。。。'
    event.wait()           #默认没有被set时 wait会一直等待
    event.clear()                #清空被设置的set  恢复默认的false
    print 'p 有人来买包子了'
    print 'p 开始为人做包子'
    time.sleep(5)
    #event.set()
    print 'p 包子做好了'
    event.set()           #写在这里比上面更好一些，上面更能理解c 在wait
def consumer():
    print 'c 去买包子。。。'
    event.set()                 #将默认的事件flag设为True 原来是false   开始阻塞
    time.sleep(2)
    print 'c 等包子做好'
    #print event.isSet()     #判断是否set  是的话直接不等了 输出下面内容   类似异步  select
    while True:
        if event.isSet():
            print '准备去拿 thanks...'
        else:
            print '还尼玛没好啊。。。'
            time.sleep(1)
    #print event.wait()   # 效果= event.wait()
    #print 'c 准备去拿 thanks'
event = threading._Event()
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()