#_*_coding:utf-8 _*_
import pickle
li = ['alex',11,22,'ok''sb']
dumpsed = pickle.dumps(li)           #不光可以序列化字符串 还有类和对象
print pickle.dumps(li)
print type(pickle.dumps(li))
loadsed = pickle.loads(dumpsed)
print loadsed
print type(loadsed)                   #可以把字符串序列化到文件  再从文件反序列化回来


pickle.dump(li,open('C:\work\temp.pk','w'))   #序列化保存进一个文件
result = pickle.load(open('C:\work\temp.pk','r'))
print result

#数据之间交互需要这种序列化方式共享数据（内存，比如在一个字典比较复杂的情况下，可能3行 5行
#100行 这时数据的共享在单纯写入文件的时候就会比较麻烦 ，所以 要序列化），字典是不能直接写到文件中去的     socket只能传字符串

#pickle 和json（json也是一种序列化）都是序列化的,只是pickle是python专用，而json化序列是多语言通用的
#json只能序列化常规的数据类型，字典 集合 列表 之类的

import json
name_dic = {'name':'lml','age':23}
serialized_obj =  json.dumps(name_dic)
print json.dumps(name_dic)
json.loads(serialized_obj)   #再序列化回来   输出结果前面会带u 是因为往内存里存是unicode形式存 再解回来还是unicode
