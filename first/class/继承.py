#_*_coding:utf-8 _*_

class father(object):      #两种方法 一种是不继承object （经典类）   另 一种是super必须要继承object 叫新式类
    def __init__(self):     #类本质上也是object创建的
        self.fname = 'ffff'
        print 'father.init'

    def func(self):
        print 'father.func'

    def bad(self):
        print 'father.喝酒烫头'



class son(father):        #这就是继承
    def __init__(self):
        self.sname = 'ssss'
        print 'son.init'
        father.__init__(self)   #显示的调用父类的构造函数 这行不加 不输出father.init
        super(son,self).__init__()     #这个函数也能执行父类的构造函数,上面父类也要继承object类
    def bar(self):
        print 'son.bar'     #这是重写父类的方法

    def bad(self):
        print 'son.烫头'

    def bad(self):
        father.bad(self)
        print 'son.赌博'
#父类 又叫基类    子类 又叫派生类

s1 = son()
s1.bar()
s1.func()
s1.bad()


#新式类较经典提供了更多的方法    继承顺序
区别： 经典类在重复继承，多继承的时候



class d(b,c)    #多重继承 从左到右继承 


#.2.2以前的时候type和object还不统一. 在2.2统一以后到3之间,  要用class Foo(object)来申明新式类, 因为他的type是 < type 'type' > .
# 不然的话, 生成的类的type就是 < type 'classobj' >
#继承了object的类是新式类，由于他们都是object的派生类，便于统一操作。py2由于一些类不继承object，就弄了一些内置函数，
#Python 2.7 里面新式类和经典类在多继承方面会有差异：