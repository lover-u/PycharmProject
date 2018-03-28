#!/user/bin/python
#_*_coding:utf-8 _*_
from multiprocessing import Pool
def f(x):
    return x*x

if __name__  == '__main__':
    p = Pool(5)
    print(p.map(f,[1,2,3]))     #官方介绍的产生多进程的方法 