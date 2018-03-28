#_*_coding:utf-8 _*_

#构造函数就是__init__
import time
class foo:
    def __init__(self):
        pass

    def __del__(self):
        print '解释器要销毁我了，要发出最后一次呐喊'   #这个是最后执行的 __del__方法

    def go(self):
        print 'go'

    def __call__(self, *args, **kwargs):
        print 'call'

#time.sleep(10)    #睡眠10秒
#__call__ 方法
f1 = foo()   #根据一个类创建一个对象
f1.go()  #这是一般印象中的对象使用方法
f1()    #对象 加（） 这相当于去执行一个__call__方法 ，抱错，我们就去写一个call 方法
foo()()