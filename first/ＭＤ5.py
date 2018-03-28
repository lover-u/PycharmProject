#_*_ coding:utf-8 _*_
import hashlib    #导入模块
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()  #16
print hash.digest()     #长度不同

