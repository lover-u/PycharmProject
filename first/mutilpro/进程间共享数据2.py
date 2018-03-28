#!/user/bin/python
#_*_coding:utf-8 _*_
from multiprocessing import Process,Queue    #这里的Queue是multiprocessing里面的自带queue模块，跟Queue模块有区别，应该会有继承关系
import Queue as Q2

def f(q,n):
    q.put([n,'hello'])              #注意get是随机拿一条   所以这个例子是进程间共享数据
    print q.get()
    print q.get()
if __name__ == '__main__':
    #q = Queue()
    q = Q2.Queue()
    q.put('ddd')
    for i in range(5):
        p = Process(target=f,args=(q,i))
        p.start()
    while True:
        print q.get()
#for i in range(5):
#   print i                          #linux 下运行


'''
#!/user/bin/python
#_*_coding:utf-8 _*_
from multiprocessing import Process,Queue    #这里的Queue是multiprocessing里面的自带queue模块，跟Queue模块有区别，应该会有继承关系
#import Queue as Q2

def f(q,n):
    q.put([n,'hello'])              #注意put是随机拿一条   所以这个例子是进程间共享数据
    print q.get()
    print q.get()
if __name__ == '__main__':
    q = Queue()
    #q = Q2.Queue()
    q.put('ddd')
    for i in range(5):
        p = Process(target=f,args=(q,i))
        p.start()
    while True:
        print q.get()
#for i in range(5):
#   print i


'''
'''
1.from Queue import Queue这个是普通的队列模式，类似于普通列表，先进先出模式，get方法会阻塞请求，直到有数据get出来为止
2.from multiprocessing.Queue import Queue这个是多进程并发的Queue队列，用于解决多进程间的通信问题。普通Queue实现不了。例如来跑多进程对一批IP列表进行运算，运算后的结果都存到Queue队列里面，这个就必须使用multiprocessing提供的Queue来实现



'''