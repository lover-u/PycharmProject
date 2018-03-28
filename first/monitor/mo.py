#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time,re
file = open('/var/log/accsess.log')
while 1:
    where = file.tell()
    #print 'first', where
    #pos = file.seek(0,2)
    #print pos
    line = file.readline()
    if not line:
       time.sleep(3)
       file.seek(where)
    else:
       #print str(line)
       print line
       p = re.compile(r"(error)")
       m = p.search(line)
       print m.
       #result = re.findall('error',line,[re.I])
       #result.group()
       #print result

~