#!/usr/bin/python
# -*- coding: UTF-8 -*-



import datetime, Time
import json
import urllib
import argparse
#import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--host", help="InfluxDB server name/IP", default="localhost")
parser.add_argument("--port", help="InfluxDB server port", default=8086, type=int)
parser.add_argument("--user", help="InfluxDB user name", default='root')
parser.add_argument("--pwd", help="InfluxDB password", default='root')
parser.add_argument("--db", help="InfluxDB database name")


args = parser.parse_args()
server=args.host
port=args.port
user=args.user
pwd=args.pwd
db=args.db


now = datetime.datetime.now()
print now
d7 = now - datetime.timedelta(days=now.isoweekday())
day7 = d7.strftime("%Y-%m-%d") + ' 23:59:59'
d1 = d7 - datetime.timedelta(days=6)
day1= d1.strftime("%Y-%m-%d") +' 00:00:00'


tday1 = str(Time.mktime(Time.strptime(day1, "%Y-%m-%d %H:%M:%S"))).split('.')[0]
tday7 = str(Time.mktime(Time.strptime(day7, "%Y-%m-%d %H:%M:%S"))).split('.')[0]             #strp 格式化 时间    mk  转换为时间戳

sql0 = 'SHOW TAG VALUES FROM "cpu" WITH KEY = "host"'
#sqllist = ('mem','disk','net','cpu')
sql1 = 'select mean(used_percent) as memused from mem where time >= %s000ms and time <= %s000ms group by host;'%(tday1,tday7)
sql2 = 'select mean(usage_user) as cpuused from cpu where time >= %s000ms and time <= %s000ms group by host;'%(tday1,tday7)
sql3 = 'select max(usage_user) as  cpumax from cpu where time >= %s000ms and time <= %s000ms group by host;'%(tday1,tday7)
sql4 = 'select mean(used_percent) as diskused from disk where time >= %s000ms and time <= %s000ms group by host;'%(tday1,tday7)
sql = {
    'memused':sql1,
    'cpuused':sql2,
    'cpumax':sql3,
    'diskused':sql4
    }

def url(sqltext):
    url = 'http://'
    url = url + server + ":" + str(port) + "/query?"
    url = url + urllib.urlencode({"q":sqltext})
    url = url + "&db=" + db
    #print url
    return url


def fetchResult(url):
    fid = urllib.urlopen(url)
    jsonData = fid.read()
    fid.close()
    return json.loads(jsonData)

def getdictname():
    fid = urllib.urlopen(url)
    jsonData = fid.read()
    fid.close()
    json.loads(jsonData)



if __name__ == "__main__":
    for type in sql:
        httpurl = url(sql[type])
		# print url
        jsonData = fetchResult(httpurl)
        #print '01',jsonData
        #jsonData = jsonData["results"]
        #print '02',jsonData
        jsonData=jsonData["results"][0]["series"]
        print '02',jsonData
        #def jsonData():
    v_list = []
    for jsonData in jsonData:
        #for  host in ('appstore','cdh23','cdh24','cdh25','db27','db29','db30','se50','se51','se52'.'zn01','zn02','zn03')

        v_dict = {}
        host = jsonData["tags"]["host"]
        v_dict['host'] = host
        v_dict['type'] = type
        columns = jsonData['columns'][1]
        print 'columns:', columns
        value = str(jsonData["values"][0][1])[0:5]
        v_dict['value'] = value
        print 'dict:',v_dict
        print 'list:',v_list
        #v_list.append(v_dict.items())
        v_list.extend(v_dict.items())
        #print 'dict--itens:',v_dict.items()
        # print v_dict.get('host')
        print(len(v_list))
        print 'v_list:', v_list
        #value = str(jsonData["values"][0][1])[0:5]
        #print jsonData["values"][0][1]
        #print value
        #print host,type,value

