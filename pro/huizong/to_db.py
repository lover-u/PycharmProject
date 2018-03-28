#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import os
import json
import datetime

ALARM_LOG_PATH = "/letv/apps/cdn_alarm/logs"
conn = MySQLdb.connect(host="10.110.98.109", port=3306, user="wangziyin", passwd="wangziyinpw",db="leutil", charset='utf8')

def into_db(sql_values, alarm_tree, date_str):
    '''
	into db : node_monitor , date,treeid,tiem,number
    '''
    #sql_values = ('koko', 900, '999999', 0)
    cursor = conn.cursor()
    cursor.execute("delete from node_monitor where date=\"%s\" and treeid=\"%s\"" % (date_str,alarm_tree))
    cursor.executemany("insert into node_monitor(date,treeid,item,number) values (%s,%s,%s,%s)" , sql_values)
    cursor.close()

def get_items(alarm_tree,date_str):
    alarm_log_file = os.path.join(ALARM_LOG_PATH, alarm_tree+"_alarm-%s.log" % date_str)
    if not os.path.exists(alarm_log_file):
        cdn_alarm_counter = {}
    else:
        cdn_alarm_counter, alarm_sum, sum_endpoints = json.loads(open(alarm_log_file).read())
	cdn_alarm_counter['alarm_sum'] = int(alarm_sum)
	cdn_alarm_counter['endpoint_sum'] = int(sum_endpoints)
    return cdn_alarm_counter

def make_sql(alarm_items, alarm_tree, date_str):
    sql_values=[]
    for k,v in alarm_items.items():
        sql_values.append((date_str,alarm_tree,str(k),str(v)))
    return sql_values

if __name__ == '__main__':
    date_str = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    #date_str = '2017-11-29'
    #alarm_tree_list = {'cdn':221,'video':47}
    alarm_tree_list = {'cdn':221,'video':5181}
    for alarm_tree_name,alarm_tree_id in alarm_tree_list.items():
        alarm_items = get_items(alarm_tree_name, date_str)
        sql_values = make_sql(alarm_items, alarm_tree_id, date_str)
        #print sql_values
        if len(sql_values) == 0:
            print "null"
        else:
            into_db(sql_values,alarm_tree_id,date_str)