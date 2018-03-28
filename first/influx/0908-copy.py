#!/bin/python
# -*- coding: UTF-8 -*-

import datetime,time
import json
import urllib
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--host", help="InfluxDB server name/IP", default="172.20.0.20")
parser.add_argument("--port", help="InfluxDB server port", default=8086, type=int)
parser.add_argument("--user", help="InfluxDB user name", default="root")
parser.add_argument("--pwd", help="InfluxDB password", default="root")
parser.add_argument("--db", help="InfluxDB database name",default="telegraf")


args = parser.parse_args()
server=args.host
port=args.port
user=args.user
pwd=args.pwd
db=args.db


now = datetime.datetime.now()
d7 = now - datetime.timedelta(days=now.isoweekday())
day7 = d7.strftime("%Y-%m-%d") + ' 23:59:59'
d1 = d7 - datetime.timedelta(days=6)
day1= d1.strftime("%Y-%m-%d") +' 00:00:00'


tday1 = str(time.mktime(time.strptime(day1, "%Y-%m-%d %H:%M:%S"))).split('.')[0]
tday7 = str(time.mktime(time.strptime(day7, "%Y-%m-%d %H:%M:%S"))).split('.')[0]
print tday1
print tday7

#sql0 = 'SHOW TAG VALUES FROM "cpu" WITH KEY = "host"'
sql1 = 'select mean(used_percent) as memused from mem where time >= %s000ms and time <= %s000ms group by host;'%(tday1,tday7)
sql2 = 'select min("usage_idle") * -1 + 100  as  cpumax from cpu where time >= %s000ms and time <= %s000ms group by host;'%(tday1,tday7)
sql3 = 'select mean("usage_idle") * -1 + 100 as cpuused from cpu  where time >= %s000ms and time <= %s000ms group by host;'%(tday1,tday7)
sql4 = "select max(used_percent)   as  diskused from disk where time >= %s000ms and time <= %s000ms and path='/' group by host;"%(tday1,tday7)
sql = {
		'memused':sql1,
		'cpumax':sql2,
		'cpuused':sql3,
                'diskused':sql4
       }

def url(sqltext):
    url = "http://"
    url = url + server + ":" + str(port) + "/query?"
    url = url + urllib.urlencode({"q":sqltext})
    url = url + "&db=" + db
    return url


def fetchResult(url):
    fid = urllib.urlopen(url)
    jsonData = fid.read()
    fid.close()
    return json.loads(jsonData)

if __name__ == "__main__":
        list=[]
	for type in sql:
		httpurl = url(sql[type])
		jsonData = fetchResult(httpurl)
		jsonData=jsonData["results"][0]["series"]
        list.append(jsonData)
        print list
        all_dict = {}
        for line in list:
                host_dict = {}
                for item in line:
                    host = item.get("tags").get("host")
                    name = item.get("columns")[1]
                    values = str(item.get("values")[0][1])[0:4]
                    host_dict[host] = {name: values}
                    print host_dict
                #for k, v in host_dict.items():
                    #if k in all_dict:
                    #   all_dict.get(k).update(v)
                    #else:
                #       all_dict[k] = v
        #print all_dict
        print '01:', host_dict
        for k, v in host_dict.items():
            pass
        print json.dumps(host_dict)