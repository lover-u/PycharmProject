#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import os
import json
import datetime
from html import HTML
from sender import Sender

ALARM_LOG_PATH = "/letv/apps/cdn_alarm/logs"

conn = MySQLdb.connect(host="10.110.100.113", port=3306, user="new_monitor", passwd="NDg1MzQ2NDJkNGE",db="falcon_portal", charset='utf8')

def get_cdn_hostgroup_id():
    cursor = conn.cursor()
    cursor.execute("select id from grp where grp_name like \'%CDN%\'")
    rows = cursor.fetchall()
    cursor.close()
    return map(lambda x: x[0], list(rows))

def get_cdn_endpoints():
    #cdn_group_ids = get_cdn_hostgroup_id()
    cursor = conn.cursor()
    cursor.execute("select distinct(hostname) from host join grp_host on \
            host.id=grp_host.host_id join grp on grp_host.grp_id=grp.id where grp.grp_name like \'%CDN%\'")
    rows = cursor.fetchall()
    cursor.close()
    return map(lambda x: x[0], list(rows))

def write_alarm(date_str, data):
    filename = os.path.join(ALARM_LOG_PATH, "cdn_alarm-%s.log" % date_str)
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()

def get_alarm_layday(endpoint, tupledays=1):
    today_str = (datetime.datetime.now() - datetime.timedelta(days=(tupledays-1))).strftime('%Y-%m-%d')
    last_days_str = (datetime.datetime.now() - datetime.timedelta(days=tupledays)).strftime('%Y-%m-%d')
    conn.select_db('alarm')
    cursor = conn.cursor()
    sql = "select endpoint, counter from history where timestamp > \"%s\" and timestamp < \"%s\"" % (last_days_str, today_str)
    print sql
    cursor.execute("select endpoint, counter, timestamp from history where timestamp > \"%s\" and timestamp < \"%s\"" % (last_days_str, today_str))
    rows = cursor.fetchall()
    cursor.close()
    cdn_endpoint_counter = {}
    for host, counter, timestamp in rows:
        if host in cdn_host:
            if counter not in cdn_endpoint_counter:
                cdn_endpoint_counter[counter] = 1
            else:
                cdn_endpoint_counter[counter] += 1
    alarm_sum = sum(cdn_endpoint_counter.values())

    write_alarm(last_days_str, (cdn_endpoint_counter, alarm_sum, str(len(endpoint))))

    return cdn_endpoint_counter, alarm_sum, str(len(endpoint))

def make_html(data, table_header):
    '''
    [[], []]
    '''
    h = HTML('html')
    h.h4(u"CDN相关业务过去5天的报警统计:")
    t = h.table(border='1')
    r = t.tr
    r.th('Item')
    for i in table_header:
        r.th(i)

    for items in data:
        r = t.tr
        for item in items:
            r.td(str(item))
    return str(h)

if __name__ == '__main__':
    cdn_host = get_cdn_endpoints()
    counter_list = []

    table_header = []
    last_five_day_alarm = {}
    html_data = []
    endpoint_list = [u'监控主机数']
    sum_list = ['SUM']

    for i in range(5):
        tupledays = i+1
        date_str = (datetime.datetime.now() - datetime.timedelta(days=tupledays)).strftime('%Y-%m-%d')
        print "process data: %s" % date_str
        table_header.append(date_str)
        alarm_log_file = os.path.join(ALARM_LOG_PATH, "cdn_alarm-%s.log" % date_str)
        if os.path.exists(alarm_log_file):
            cdn_alarm_counter, alarm_sum, sum_endpoints = json.loads(open(alarm_log_file).read())
        else:
            cdn_alarm_counter, alarm_sum, sum_endpoints = get_alarm_layday(cdn_host, tupledays=tupledays)
        if not counter_list:
            #print sorted(cdn_alarm_counter.items(), key=lambda item:item[1], reverse=True)
            counter_list = map(lambda d: d[0], sorted(cdn_alarm_counter.items(), key=lambda item:item[1], reverse=True))
        else:
            counter_list.extend(list(set(cdn_alarm_counter.keys()) - set(counter_list)))

        last_five_day_alarm[date_str] = cdn_alarm_counter

        endpoint_list.append(sum_endpoints)
        sum_list.append(alarm_sum)

    html_data.append(endpoint_list)
    html_data.append(sum_list)

    for counter in counter_list:
        counter_num = []
        counter_num.append(counter)
        for date in table_header:
            num = last_five_day_alarm.get(date).get(counter, 0)
            counter_num.append(num)
        html_data.append(counter_num)

    # write html table
    h = make_html(html_data, table_header).replace('\n', '')

    sender = Sender()
    sender.EMAIL('iops-cdn@le.com,wangziyin@le.com,wangyanping@le.com,shidi@le.com,baijf@le.com', 'Cdn Alarm Number', h)
    #sender.EMAIL('wangziyin@le.com', 'Cdn Alarm Number', h)
