# -*- coding: UTF-8 -*-
from datetime import datetime
from datetime import timedelta
import time
now = datetime.now()
aDay = timedelta(days=1)
print aDay
now = now + aDay
print now.strftime('%Y-%m-%d')                           #timedelta代表两个datetime之间的时间差
print time.mktime(time.localtime())

sql1 = 1
sql2 = 2
sql3 = 3

sql = {
		'memused':sql1,
		'cpuused':sql2,
		'cpumax':sql3
       }
for type in sql:
    #httpurl = url(sql[type])
    print sql
    print 'sql:type:',sql[type]
    print type