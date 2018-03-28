#!/usr/bin/python
#!-*- coding:utf8 -*-
# -------------------------------------------------------------------------------
# Filename: 60_CheckCeph.py
# Revision: 1.0
# Date: 2018/02/22
# Eco: 乐视云
# Author: 李明磊
# Email: liminglei@le.com
# Description: 实现每分钟检测ceph存储集群的健康状态
# -------------------------------------------------------------------------------

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
#   cephStatus = "Failed"
    cephStatus = "0"

#if "HEALTH_OK" or "HEALTH_WARN" in output:
if "HEALTH_OK"  in output:
#   cephStatus = "OK"
    cephStatus = "1"
elif "HEALTH_WARN" in output:
    cephStatus = "3"
else:
#   cephStatus = "ERR"
    cephStatus = "2"

#Get Agent IP
filename = r'/usr/local/LeMonitor/falcon-agent/cfg.json'
if os.path.exists(filename):
    fp = open(filename,'rb').read()
    pre_ip = re.findall(r'^\s+"hostname":.*$',fp,re.M)
    ip = str(pre_ip)
    IP = ip.split('"')[3]
else:
    ipCmd = "hostname"
    IP = commands.getstatusoutput(ipCmd)

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