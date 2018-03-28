#_*_coding:utf-8 _*_
class person:
    xue = 'xue'    #有类了怎么创建对象？  需要一个特殊的函数
    def __init__(self,name,age):     #为了实例化动作提供的一个函数
        self.name = name
        self.age = age

p1 = person('liyang',18)                #创建类的时候都需要__init__函数，并且第一个参数一定要是self
print p1.name,p1.age

class anaime:
    xx = 'xx'


class Province:
    memo = '中国的23 个省之一'    #声明， memo 属于类（）直接
    #这种方式的叫字段--〉memo <  = '中国的23 个省之一'
    def __init__(self,name,capital,leader):
        self.Name = name
        self.Capital = capital          #其实name leader之类的无所谓 只是字符串
        self.Leader = leader              #一般称这种为字段

    #动态方法
    #def > sports_meet(self):  <--这种方式的叫方法
    def sports_meet(self):
         print self.Name + '正在开运动会'

    @staticmethod       #加一个特定的装饰器和去除self转化为静态方法
    def foo():
        print '每个省都要带头反腐'

    # 属性 特性
    @property
    def bar(self):
        print self
        return 'somthing'



#hb.sports_meet()    #放在这执行和放在下面执行效果是不一样的
#sd.sports_meet()

hb = Province('hebei','shijiazhuang','AA')
sd = Province('shangdong','jinan','BBB')
#其实self = hb sd
print hb.Capital  #对象的字段      动态字段
print Province.memo   #类的方法  属于类的字段叫静态字段
#print Province.Name    # 可以吗 ？  静态的类不可以访问动态的字段 ！
print hb.memo      #是可以的  对象可以访问静态字段

print hb.bar     #在这以这种方式访问    可以 直接 hb.bar  执行属性特性


hb.sports_meet()
sd.sports_meet()
Province.foo()

#类的字段叫静态字段  对象的字段叫动态字段
#带self的叫动态方法    加装饰器和去除self转化为静态方法    用加()的方式访问

#类里面三种结构，字段  方法 特性
# ！！
#hb.Name   对象的访问方法
#hb.sports_meet()   方法的访问方法
#hb.bar    属性的访问不在是方法 是以类似字段的访问形式

'''
#coding:utf-8

class Car:
    # 下面是静态字段
    memo = u'车辆具有出厂合格证'
    
    def __init__(self, brand, model, speed, price, engine):
        # 下面是动态字段
        self.Brand = brand
        self.Model = model
        self.Speed = speed
        self.Price = price
        self.__EngineType = engine
        
    # 下面是动态方法
    def Turnleft(self):
        print self.Brand + u'开始向右转向。'
        
那么关于这四种类型，有什么特点？以下进行总结：

    四种类型，均可以被“对象”进行调用，但不建议使用“对象”调用“静态方法”和“静态字段”，而建议使用“类”对其进行调用
    “动态方法”和“动态字段”只能由“对象”进行调用，而无法使用“类”进行调用        

'''