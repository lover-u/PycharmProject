#!/user/bin/python
#_*_coding:utf-8 _*_

from multiprocessing import  Process
import threading
info = []
def run(info_list,n):
    info_list.append(n)
    print info_list

info = []
for i in range(10):
    p = Process(target=run,args=[info,i])
    p.start()

print '上面的是进程例子结果'
print '-----threading--------'
for i in range(10):
    p = threading.Thread(target=run,args=[info,i])
    p.start()


