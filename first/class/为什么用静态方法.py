#_*_coding:utf-8 _*_

'''
class sqlhelper:
    def add(self,sql):
        pass
    def delete(self,sql):
        pass
    def update(self,sql):
        pass
    def select(self,sql):
        pass

ms = sqlhelper()   #创建对象   如果有100个对象呢 ？ 1000个呢  怎样用一个对象就全处理了， 方法是创建静态对象，让业务方去调用
ms.update(sql)     #操作对象的方法
'''
class sqlhelper:


    @staticmethod
    def add(sql):
        pass

    @staticmethod
    def delete(sql):
        pass

    @staticmethod
    def update(sql):
        pass

    @staticmethod
    def select(sql):
        pass

#ms = sqlhelper()   #这部省略创建对象   如果有100个对象呢 ？ 1000个呢  怎样用一个对象就全处理了， 方法是创建静态对象，让业务方去调用
#ms.update(sql)     #作用 ，不实例化类就可以调用下面的方法

ms.update(sql)
ms.add(sql)



#那我直接写到一个模块里不是也是这种效果吗  ？ 比如有个sqlhelper.py的文件，其实这里主要是有 静态方法跟类之间的逻辑关系


#反射加模块化编程   完全可以复制面向对象的那套的所有东西