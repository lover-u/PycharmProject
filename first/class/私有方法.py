#_*_coding:utf-8 _*_

class Province(object):                      #类需要继承object
    memo = '中国的23 个省之一'
    def __init__(self,name,flag):
        self.Name = name
        self.__thailand = flag    #定义私有字段
    def show(self):
         print self.__thailand

    def __sha(self):            #定义私有方法
        print 'i am alex'

    def foo(self):
        self.__sha()     #定义一个公有方法  用它去掉用私有方法  达到使用私有方法的目的

    @property             #只读，   私有方法的只读属性
    def thailand(self):
        return self.__thailand

    @thailand.setter         #如果需要可改的特性，需要两步，上面类需要加继承object   这是推荐的访问和修改私有字段的方式
    def thailand(self,value):
        self.__thailand = value

sd = Province('shangdong',True)
# print sd.__thailand     去掉#号会抱错，不能那样访问
sd.show()           #true
#sd.__sha()    #私有方法，外面是无法访问的    会抱错
sd.foo()      # i am alex
sd.thailand   #这个不输出         #通过这种方式获取私有字段     需要先需要先构造一个特性property
sd._Province__sha()    #显示的调用私有方法，但不建议使用
sd.thailand = False
print sd.thailand


#私有字段 私有方法

#继承了object之后是不可以被更改的， 这就是为什么加seter的原因