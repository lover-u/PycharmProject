#!/user/bin/python
#_*_coding:utf-8 _*_
import time
from multiprocessing import Process,Value,Array
def f(n,a,raw):
    n.Value = 3.1415927
    for i in range(5):
        a[1] = -a[i]
    raw_append(9999)
    print raw

if __name__ == '__main__':
    num = Value('d',0.0)
    arr = Array('1',range(10))
    raw_list = range(10)
    print num.value
    print arr[:]
    print arr  #不加：号打印的是一个实例，加冒号是整个列表值

    p = Process(target=f,args=(num,arr,raw_list))
    p.start()
    p.join()

    print num.value
    print arr[:]
    print raw_list
