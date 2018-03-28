#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict01 = {u'values': [[u'2017-08-27T16:00:00Z', 3.6815819343501612]], u'name': u'disk', u'columns': [u'time', u'diskused'], u'tags': {u'host': u'cdh23'}}

dict02 = {u'values': [[u'2017-08-27T16:00:00Z', 3.6815819343501612]], u'name': u'disk', u'columns': [u'time', u'diskused'], u'tags': {u'host': u'cdh23'}}



jsonData = dict(dict01.items()+dict02.items())
print jsonData
#jsonData01 = dict(jsonData,**jsonData)
#jsonData = jsonData["results"][0]["series"]
#dictnerge = jsonData01(jsonData01.ite)
#print jsonData02
#print type(jsonData02)
print jsonData
v_dict = {}
host = jsonData["tags"]["host"]
v_dict['host'] = host
v_dict['type'] = type
# columns = jsonData['columns'][1]
# print 'columns:', columns
value = str(jsonData["values"][0][1])[0:5]
v_dict['value'] = value
# print 'dict:',v_dict
# print 'list:',v_list
# v_list.append(v_dict.items())
v_list.extend(v_dict.items())
# print 'dict--itens:',v_dict.items()
# print v_dict.get('host')
#print '01',jsonData
#jsonData = jsonData["results"]
#print '02',jsonData
#jsonData02=jsonData01["results"][0]["series"]
#host = jsonData["tags"]["host"]
#jsonData = jsonData01+jsonData02
#Data = type,jsonData
#print jsonData
#host = jsonData["tags"]["host"]
#print host
#jsonData = dict(jsonData.items()+jsonData.items())
