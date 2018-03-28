
#_*_ coding:utf-8 _*_
temp = None
if 1>3:
    temp = 'gt'
else:
    temp = 'lt'
print temp
result = 'gt' if 1>3 else 'lt'       #一行代码
print result

a = lambda x,y:x+y            #lamda 关键字不能用作变量,参数的个数不限，可以是x ,x,y x,y,z
print a(4,10)    #结果14   等效于下面   且只能调用一次
'''
def foo(x,y):
    return x+y
print foo(4,1）
[x*2 for x in range(10)]   #这种写法会返回1-9之间每个数字的2倍 
for i in [lambda x:x**x for x in range(10)]:print i   #看看输出     lambda是匿名函数，功能是做运算后返回  

map(lambda x:x*2,range(10)   #等效上面的
map(lambda x:x**x,range(10)    #什么用？  省代码

内置函数
help()
dir()  关于相关函数的  的Key
vars（）列出相关的key和value 

a = []    #通过这种方式去创建列表，本质上调用list去创建一个类
a1 = list()  #等效于这种


'''

#from file import demo
#from file import demo   #python 默认在执行一次导入后是不会再导入的，重新导入需要relaod
# reload(demo)

t = 1
print id(1)    #id函数是返回内存地址的

print abs(-9)  #返回绝对值
print bool(15)  #返回布尔值 0 false   1 ture
print divmod(9,3)  #得到商和余数   用处计算页数 有余数要加1
print max([1,2,3,4,5,6])
print min([1,2,3,4,5,6])
print sum([1,2,3,4,5,6])
print pow(2,10)

print len('oooo')  #中文指的是字节的长度，而不是字符
print all([1,2,3,4])    #迭代里面的所有值，所有的(布尔值)都为真就是ture有一个为假就为false
print all([1,2,3,0])
print any([1,0,0,0,0])     #迭代里面的所有值，所有的(布尔值)有一个为真，就为真
print any([1,2,3,4])
print bool('')     #空值和None 结果都是false
print bool(None)


print chr(66)    #打印ascii 码中该数字序列对应的字母编码
print chr(67)
print chr(68)
print chr(69)
print ord('A')    #与cha相反 取字符的asc序列       验证码是不能随即生成的，随机生成的是asc对应的数字

print hex(2) #16进制
print bin(2)  #2进制
print oct(2)  #8进制的2

liwu = ['手表','鲜花','糖','汽车']
for item in liwu:
    print item

for item in enumerate(liwu):
    print item


#可变参数对于列表来说是一个*对于字典来说是**
