#!/usr/bin/python
#!-*- coding:utf8 -*-

import requests
import time
import json
import commands
import re
import os
cephCmd = "ceph -s"
status, output = commands.getstatusoutput(cephCmd)
if status != 0:
    print("Get Ceph Status Failed!")

#cephStatus = "Failed"
cephStatus = "0"
if "HEALTH_OK" or "HEALTH_WARN" in output:
#    cephStatus = "OK"
    cephStatus = "1"
#else

filename = r'/usr/local/LeMonitor/falcon-agent/cfg.json'
if os.path.exists(filename):
   fp = open(filename,'rb').read()
   #arr = []
   print type(fp)
   print fp
   pre_ip = re.findall(r'^\s+"hostname":.*$',fp,re.M)
   print pre_ip
   ip = str(pre_ip)
   #l=re.findall(r'\d+.\d+.\d+.\d+', ip)
   IP = ip.split('"')[3]
   print IP
   #for lines in fp.readlines():
   #  print (lines);
   #  match1 = re.search(p1,line)
   #  print(match1.group(0))
     #p = re.findall('"hostname":', lines)
     #print p.group()
   #fp.close()
'''
    fp = open(filename)
    arr = []
    for lines in fp.readlines():
        matchObj = lines.
    fp.close()
'''


#cephTag = "cephStatus=" + cephStatus

ts = int(time.time())
payload = [
    {
        "endpoint": IP ,
        "metric": "ceph-status",
        "timestamp": ts,
        "step": 60,
        #"value": 2,
        "value": cephStatus,
        "counterType": "GAUGE",
        #"tags": cephTag,
        "tags": "",
    },
]
data=json.dumps(payload)
print data
#r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))

#print r.text