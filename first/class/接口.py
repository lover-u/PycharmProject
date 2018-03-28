#_*_coding:utf-8 _*_

#有一种数据类型叫interface
interface IAlert:
        #这种结构也可以定义方法 但不能有具体的实现  会抱错
        pass   #类似于只能写pass   具体的实现由”客户端“完成

class weixin(IAlert):
    def send(self):
        print 'shi weixin '
class email(IAlert):
    def send(self):
        print 'shi email '
class phone(IAlert):
    def send(self):
        print 'shi phone '


#抽象类加抽象方法  就等于 接口（规范）