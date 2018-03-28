#_*_coding:utf-8 _*_

from abc import ABCMeta,abstractmethod
class Alert:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self):
        pass

try:
#interface IAlert
class weixin(Alert):      #在这继承了抽象类之后就相当于继承了你的接口
    def __init__(self):
        print '__init__'

    def  send(self):
        print 'send weixin'
f = weixin()
f.send()
except  (ImportError,AttributeError),e:      #括号里加目的异常类型 一个不用加括号
        print 1, e
        print '这是捕获异常的'
except  AttributeError,e:
        print 2,e
        print '这是捕获异常的'

except    Exception,e:                  #Exception  关键字是用来捕获所有的异常的
        print 3,e
        rpint '这是捕获异常的'
else:                                    #esle和finally是可以不加的 但except必须出现的
        print '没有出错'                 #被try包围的代码 一旦异常就会终止执行 不在继续其他部分
finally:
        print '无乱是否异常都回执行'