#/user/bin/python
#_*_ coding:utf-8 _*_
from  demo import  *
print 'index',__name__


def login(username):
    if username == 'alex':
        return '登陆成功'
    else:
        return '登陆失败'
def detail(user):
    print user,'xxxx'
if __name__ == '__main__':
    print 'this file is main process interface'
    user = raw_input('请输入用户名')
    login(user)
    result = login(user)
    if result == '登陆成功':
       detail(user)
    else:
        print 'invalit user'

def foo(name):
    print name,  '去旅游'
def bar(name):
    print name,  '去吃饭'
def haha(name):
    print name, '去睡觉'


def foo1(name,action='go to eta',where='Beijing'):             #mutil value  = is set default  如果有默认参数，必须写到最后面，否则会抱错
    print name,'去',action,where        #可以将上面函数合并,


foo('li')
bar('wang')
foo1('lili','go to sleep')
foo1('haha',where='shanghai')
foo1('haha','shanghai','henan')          #不显示的指定时，默认是按顺序显示变量
foo1('haha',where='shanghai',action='henan')     #显示指定时与变量的顺序就没有关系了

'''
def show(arg):
    for item in arg:
        print item
def show2(arg1,arg2):
    print arg1,arg2
'''

def show(*arg):            #*arg 表示不限传入参数的个数 1234个无所谓，汇总成一个列表传入
    for item in arg:
        print item
show(['lml','haha','hehe','aaa'])

'''
def show(**karg):            #**karg 表示不限传入参数的个数 1234个无所谓，汇总成一个字典传入
    for item in karg.items:
        print item
show([name='lml',sex='haha',aa='hehe',ab='aaa'])      #可以直接传入字典样式数据


user_dict = {'k1':123,'k2':456,'k3':789}   #可以构造好字典传入（传入字典），但这样写是错误的
show(user_dict)                   #show(**user_dict)   这样才是正确的 
                                  #元组合集合应该是一个星
'''


