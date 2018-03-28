#_*_ coding:utf-8 _*_
url = 'www.baidu.com'
www = 'welcome'
while url:
    print url
    url = url[:-1]
else:
    print 'game over.'
#while www:
print www
www = www[::-1]
print www
#else:
#    print 'www game over.'