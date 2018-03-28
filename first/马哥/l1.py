# -*- coding:utf-8 -*-
import time
import json
def tail(file_name):
    f1 = open(file_name,'r',-1)
    f1.seek(0,2)
    while 1:
        n = f1.tell()
        time.sleep(10)
        m = f1.seek(n,2)
        
        n <= 10


tail('/var/log')

json.dump(1,'123dfg')