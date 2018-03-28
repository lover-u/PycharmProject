#_*_coding:utf-8 _*_

#字符串怎么做运算 eg: ‘8*8’   先split 分开数字 然后转换数据类型作运算
a = '8*8'
print eval(a)    #eval 当作表达式进行运算


#反射       通过字符串导入模块   可以将模块作为变量了
#以字符串形式导入函数
# 以字符串形式执行函数
#temp = 'os'  #mysqlhelper     sqlserverhelper   这是个例子  会抱错  没有写mysqlhelper     sqlserverhelper
temp = 'mysqlhelper'

model = __import__(temp)
print model.count

func = 'count'        #mysqlhelper     sqlserverhelper 模块里有count函数
Funtion = getattr(model,'count')    #如果能找到Funtion就等于找到的整个函数   getattr 获取某一个模块里面的函数 hasattr
                                    #判断有没有这个函数  delattr  删除


#现在的web框架php .net  等都是通过反射的方式去匹配url的方式进行不同的处理 eg

'''
from backend import account
#地址规范 xxx/xxx
#account/login
array = data.split('/')
if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logout()    
elif .....
    pass

'''



data = raw_input('请输入地址')
array = data.split('/')


#array[0] = account
#userspace = __import__('first'+array[0])                    #eclispe下验证
userspace = __import__('account')
print userspace.login
model = getattr(userspace,array[0])
func = getattr(model,array[1])
func()

'''
import first.account
first.account.login()

'''





