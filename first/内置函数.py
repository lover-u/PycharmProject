
#_*_coding:utf-8 _*_
liwu = ['手表','鲜花','糖','汽车']
for item in liwu:
    print item

for item in enumerate(liwu):
    print item


for item in enumerate(liwu,1):      #enumerate  参数可以增加一个序列，第二个参数指定序列的起始值
    print item


for item in enumerate(liwu,5):
    print item[0],item[1]


#占位符
s = 'i am {0}'          #{0} 在这里是占位符
print s.format('alex')

s1 = 'i am %s'         #占位符 ?
print s1.format('alex')



#函数的另一种调用
def  fun(arg):
    return arg + 100

#fun(arg)
#apply(fun,('2'))     #apply调用函数
#print map(,)   #遍历


liwu = [11,22,33]               #给每个liwu加100
temp = []
for item in liwu:
    temp.append(item + 100)
print 1,temp                             #可以用map一句实现


liwu = [11,22,33]               #给每个liwu加100  调用fun 的方式
temp = []
for item in liwu:
    temp.append(fun(item))
print 2,temp                             #可以用map一句实现

print 3,map(fun,liwu)                   #可以用map一句实现
temp = map(lambda arg:arg+100,liwu)    #相当于map遍历了liwu里的参数        #all
print 4,temp


#过滤  filter 如果返回的是ture就加入到一个新列表  false 不加        Ture序列
liwu = [11,22,33]
def foo(arg):
    if arg<22:
        return True
    else:
        return False
temp1 = filter(foo,liwu)
print temp1

#累加
liwu = [11,22,33]
print reduce(lambda x,y:x+y,liwu)        #做累计    这个时候如果lambda是一个值 是不通过的


liwu = [11,]
print reduce(lambda x,y:x+y,liwu)     #当参数为一个值  reduce必须接受两个参数 当传入一个2个时内部会做处理



#zip
x = [1,2,3,4]
y = [4,5,6,7]
z = [1,2,3,4]
print zip(x,y,z)      #传入n个列表，将每列表的相同列作为一个单位输出  多列变行

x = [1,2,3]
y = [4,5,6,7]
z = [1,2,3,4]
print zip(x,y,z)      #另一种情况

m = 'i am {0}，{1}'          #{0} 在这里占位符可以多个
print m.format('alex','xxxx')