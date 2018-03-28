#!/user/bin/python
#_*_coding:utf-8 _*_

from multiprocessing import Pool
import time
def f(x):
    print x*x
    time.sleep(1)
    return x*x

#pool.map 起多进程  mutiprocess  两种  下面第三种

pool = Pool(processes=4)
res_list = []
for i in range(10):
    res = pool.apply_async(f,[i,])
    #res = pool.apply_async(f,[i,]) #默认会等待完成一个一个输出 相当于同步，阻塞
    #等于它 res = Process(target=f,[i,])
    res.get()    #等着结果执行完毕后返回   get放在这里就相当于进程是串行启动的方式 所以放在这里不合理
    #res.start()   没有这个方法启动  直接是启动的
    #res_list.append(res)
for i in res_list:          # 这种是四个四个进程同时执行，输出
    print i.get(timeout=1)   #设置超时，不会一直等待返回

# Linux 下测试
# print pool.map(f,range(10))   map 实现的和上面一样的效果

'''
from multiprocessing import Pool
import time
def f(x):
    print x*x
    time.sleep(1)
    return x*x

#pool.map 起多进程  mutiprocess  两种  下面第三种

pool = Pool(processes=4)
res_list = []
for i in range(10):
    res = pool.apply_async(f,[i,])
    #等于它 res = Process(target=f,[i,])
    #res.get()
    print '------:',i
    #res.start()   没有这个方法启动  直接是启动的
    res_list.append(res)
#res.get()
for i in res_list:
    print i            #这个时候print 的是列表的对象  




'''