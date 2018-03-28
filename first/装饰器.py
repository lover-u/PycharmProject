#_*_ coding:utf-8 _*_
def outer(fun):         #相当于执行包装原函数之后的wrapper函数
    def wrapper(arg):
        print '验证'
        fun(arg)
        print '西西西'
        result = fun(arg)
        print result
    return wrapper     #作用在所有＠的函数前加通用功能　

@outer                  #@outer = outer(Func1)  相当于返回去执行上面的
def Fun1(arg):
    print 'func1',arg
    return 'return result'       #返回值需要单独处理

@outer
def Fun2():
    print 'func2'

@outer
def Fun3():
    print 'func3'

response = Fun1('haha')
print response

'''
Fun1 =
  def wrapper(arg):
        print '验证'
        fun(arg)
        print '西西西'
        result = fun(arg)
        print result
    return wrapper
'''
