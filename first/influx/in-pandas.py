#!/usr/bin/python
# -*- coding: UTF-8 -*-



import datetime, time
import json
import urllib
import argparse
import pandas as pd

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


tday1 = str(time.mktime(time.strptime(day1, "%Y-%m-%d %H:%M:%S"))).split('.')[0]
tday7 = str(time.mktime(time.strptime(day7, "%Y-%m-%d %H:%M:%S"))).split('.')[0]             #strp 格式化 时间    mk  转换为时间戳

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
    v_list = []
    def getjson():

        for type in sql:
            httpurl = url(sql[type])
            # print url
            jsonData = fetchResult(httpurl)
            #print '01',jsonData
            #jsonData = jsonData["results"]
            #print '02',jsonData
            jsonData=jsonData["results"][0]["series"]
            print '02',jsonData
            #def getjson():

            for jsonData in jsonData:
                #for  host in ('appstore','cdh23','cdh24','cdh25','db27','db29','db30','se50','se51','se52'.'zn01','zn02','zn03')
                v_dict = {}

                host = jsonData["tags"]["host"]
                v_dict['host'] = host
                v_dict['type'] = type
                #columns = jsonData['columns'][1]
                #print 'columns:', columns
                value = str(jsonData["values"][0][1])[0:5]
                v_dict['value'] = value
                #print 'dict:',v_dict
                #print 'list:',v_list
                #v_list.append(v_dict.items())
                v_list.extend(v_dict.items())
                print 'dict--itens:',v_dict.items()
                # print v_dict.get('host')
                #print(len(v_list))
                print 'v_list:', v_list

                print host,type,value
                #print v_list[0][1],v_list[1][1],v_list[2][1],
                #print(len(v_list))
                #value = str(jsonData["values"][0][1])[0:5]
                #print jsonData["values"][0][1]
                #print value
        return v_list
    getjson()
    #print v_list
    #for k, v in enumerate(v_list):
    #    print(k,v)
    new_list = []
    def new():
        #new_list = []
        for id in v_list:
            if id not in new_list:
                new_list.append(id)
        return new_list
    new()
    print new_list
    for k, v in enumerate(new_list):
        print(k,v)
    print ("Host: diskused: cpumax:  memused: cpuused:")
    #print '主机名','diskuser','cpumax','memused','cpuused'
    print new_list[0][1],new_list[2][1],new_list[28][1],new_list[41][1],new_list[55][1]
    print new_list[3][1], new_list[4][1], new_list[29][1], new_list[42][1], new_list[56][1]
    print new_list[5][1], new_list[6][1], new_list[30][1], new_list[43][1], new_list[57][1]
    print new_list[7][1], new_list[8][1], new_list[31][1], new_list[44][1], new_list[58][1]
    print new_list[9][1], new_list[10][1], new_list[32][1], new_list[45][1], new_list[59][1]
    print new_list[11][1], new_list[12][1], new_list[33][1], new_list[46][1], new_list[60][1]
    print new_list[13][1], new_list[14][1], new_list[34][1], new_list[47][1], new_list[61][1]
    print new_list[15][1], new_list[16][1], new_list[35][1], new_list[48][1], new_list[62][1]
    print new_list[17][1], new_list[18][1], new_list[36][1], new_list[49][1], new_list[63][1]
    print new_list[19][1], new_list[20][1], new_list[36][1], new_list[50][1], new_list[64][1]
    print new_list[21][1], new_list[22][1], new_list[37][1], new_list[51][1], new_list[65][1]
    print new_list[23][1], new_list[24][1], new_list[38][1], new_list[52][1], new_list[66][1]
    print new_list[25][1], new_list[26][1], new_list[39][1], new_list[53][1], new_list[67][1]
    #string = str(v_list)
    #print string




'''
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
            #columns = jsonData['columns'][1]
            #print 'columns:', columns
            value = str(jsonData["values"][0][1])[0:5]
            v_dict['value'] = value
            #print 'dict:',v_dict
            #print 'list:',v_list
            #v_list.append(v_dict.items())
            v_list.extend(v_dict.items())
            #print 'dict--itens:',v_dict.items()
            # print v_dict.get('host')
            print(len(v_list))
            print 'v_list:', v_list
            i = 0
            i+=1
            print v_list[0][1],v_list[1][1],v_list[2][1],
            print(len(v_list))
            #value = str(jsonData["values"][0][1])[0:5]
            #print jsonData["values"][0][1]
            #print value
'''

