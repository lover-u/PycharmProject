#_*_coding:utf-8 _*_
class myexception(Exception):
    def __init__(self,msg):
        self.error = msg

    def __str__(self,*args,**kwargs):       #str是python提供的 用于重写str方法   重写输出的错误的提示
        return self.error
object = myexception('自定义xxx错误信息')
print object

#raise myexception('自定义错误信息')    #主动触发异常 返回消息    注意这里执行会“报错”，触发的

def validate(name,pwd):
    if name == 'alex' and pwd =='456':
        return True
    else:
        return False

try:
    res = validate('alex','456')
    if res:
        print '登陆成功'
    else:
        #print '记录日志到数据库'
        #print '登陆失败'
        raise myexception('登陆失败')
except Exception,e:
    print '记录日志到数据库'
    print e