#_*_ coding:utf-8 _*_

import re
result1 = re.match('\d+','23hdu2dhjhbscyugywegd78a8sc9acgabc')
print result1  #输出的是一个对象，需要再使用对象下的方法去取出文件的内容
print type(result1)   #获取对象类型
print result1.group()
result2 = re.search('\d+','23hdu2dhjhbscyugywegd78a8sc9acgabc')
print result2
print result2.group()
# match 是在给定的字符创的范围内匹配    search是在整个的文本范围内搜索   注意都是只拿一个值


result1 = re.match('\d+','hdu2dhjhbscyugywegd78a8sc9acgabc')
if result1:
    print result1  #输出的是一个对象，需要再使用对象下的方法去取出文件的内容
    print type(result1)   #获取对象类型
else:
    print 'nothing'     #只有在匹配成功才会输出 ，不成功会返回None
    #print result1.group()
result2 = re.search('\d+','hdu2dhjhbscyugywegd78a8sc9acgabc')
if result2:
    print result2
    #print result2.group()
else:
    print 'nothing'

result3 = re.findall('\d+','hdu2dhjhbscyugy2321wegd78a8sc9acga34bc')
print result3   #输出找到的所有的

com = re.compile('\d+')     #对正则表达式进行编译后使用   可以一次编译多处使用
print type(com)
print com.findall('hdu2dhjhbscyugy2321wegd78a8sc9acga34bc')     #只能是一条字符串


result4 = re.search('(\d+)\w*(\d+)','hdu2dhjhbscyugywegd78a8sc9acgabc')    #(\d+)在正则里是分组的概念
result4 = re.search('(\d+)dhjhbscyugywegd78a8sc(\d+)','hdu2dhjhbscyugywegd78a8sc9acgabc')
print result4.group()    #group跟findall没关系 只跟正则表达式的分组有关
print result4.groups()   #分组只获取组里面的东西

import time
print time.time(),'1'  #输出时间戳
print time.mktime(time.localtime()),'2'
#以时间戳形式存在的部分

print time.gmtime(),'3' # 可加时间戳参数
print time.localtime(),'4'  # 可加时间戳参数
print time.strptime('2014-11-11', '%Y-%m-%d'),'5'    #结构化的字符串 转化为后面指定的时间格式
#以结构化存在的部分

print time.strftime('%Y-%m-%d %H%M%S'),'6' # 默认当前时间    用的最多的部分
print time.strftime('%Y-%m-%d', time.localtime()),'7'  # 默认当前时间
print time.asctime(),'8'
print time.asctime(time.localtime()),'9'
print time.ctime(time.time()),'10'
#以字符串形式存在的部分

import datetime

'''
datetime.date：表示日期的类。常用的属性有year, month, day
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond
datetime.datetime：表示日期时间
datetime.timedelta：表示时间间隔，即两个时间点之间的长度
timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
strftime("%Y-%m-%d")
'''
import datetime

print datetime.datetime.now()
print datetime.datetime.now() - datetime.timedelta(days=5)

