#_*_coding:utf-8 _*_

import MySQLdb
import conf

'''
class MySQLHelper(object):
    def __init__(self):
        pass
        #self.conn_dict = dict(host='localhost',user='root',passwd='123',db='08day5')  #还可以这样
                         #等于这种形式{'host':'localhost','user'='root'....}

    def Get_Dict(self.sql,params):
        conn = MySQLdb.connect(host='localhost',user='root',passwd='123',db='08day5')
        cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)           #这种方式拿出cursor拿出的数据是一个字典
        sql = "insert into UserInfo (name,address) value(%s,%s)"
        #sql = "delete from UserInfo where id = %s"    #删除操作
        #params = ('1',)   # 这里加不加逗号都是一样的 加逗号说明是一个序列
        #sql = "update UserInfo set name = %s where id =7"  #更新操作
        #params = ('sb',)
        params = ('alex_1','usa')
        reCount = cursor.execute(sql,params)
        data = cursor.fetchall()

        #MySQL 创建的自增列，在序列号自增时，如果原来 12345 有第五列被删除，新建的列序号会从6开始
        #conn.rollback()

        conn.commit
        #关闭连接，释放资源
        cursor.close();
        conn.close()
        return data


    def Get_One(self,sql,params):
        conn = MySQLdb.connect(host='localhost',user='root',passwd='123',db='08day5')
        cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)           #这种方式拿出cursor拿出的数据是一个字典
        sql = "insert into UserInfo (name,address) value(%s,%s)"
        #sql = "delete from UserInfo where id = %s"    #删除操作
        #params = ('1',)   # 这里加不加逗号都是一样的 加逗号说明是一个序列
        #sql = "update UserInfo set name = %s where id =7"  #更新操作
        #params = ('sb',)
        params = ('alex_1','usa')
        reCount = cursor.execute(sql,params)
        data = cursor.fetchone()

        #MySQL 创建的自增列，在序列号自增时，如果原来 12345 有第五列被删除，新建的列序号会从6开始
        #conn.rollback()

        conn.commit
        #关闭连接，释放资源
        cursor.close();
        conn.close()
        return data
helper = MySQLHelper()
sql = "select * from UserInfo where id >%s"
params = (1,)
help.Get_One(sql,params)

simple_data = helper.Get_One(sql,params)
dict_data = helper.Get_Dict(sql.params)
'''



class MySQLHelper(object):
    def __init__(self):
        self.__conn_dict = conf.conn_dict
        #self.conn_dict = dict(host='localhost',user='root',passwd='123',db='08day5')  #还可以这样
                         #等于这种形式{'host':'localhost','user'='root'....}

    def Get_Dict(self.sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)           #这种方式拿出cursor拿出的数据是一个字典
        sql = "insert into UserInfo (name,address) value(%s,%s)"
        #sql = "delete from UserInfo where id = %s"    #删除操作
        #params = ('1',)   # 这里加不加逗号都是一样的 加逗号说明是一个序列
        #sql = "update UserInfo set name = %s where id =7"  #更新操作
        #params = ('sb',)
        params = ('alex_1','usa')
        reCount = cursor.execute(sql,params)
        data = cursor.fetchall()

        #MySQL 创建的自增列，在序列号自增时，如果原来 12345 有第五列被删除，新建的列序号会从6开始
        #conn.rollback()

        conn.commit
        #关闭连接，释放资源
        cursor.close();
        conn.close()
        return data


    def Get_One(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)         #要想把前面的参数字典拿来用，要  加了**号传进来的相当于host='localhost',user='root',passwd='123',db='08day5' 原来是loaclhost,root...
        cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)           #这种方式拿出cursor拿出的数据是一个字典
        sql = "insert into UserInfo (name,address) value(%s,%s)"
        #sql = "delete from UserInfo where id = %s"    #删除操作
        #params = ('1',)   # 这里加不加逗号都是一样的 加逗号说明是一个序列
        #sql = "update UserInfo set name = %s where id =7"  #更新操作
        #params = ('sb',)
        params = ('alex_1','usa')
        reCount = cursor.execute(sql,params)
        data = cursor.fetchone()

        #MySQL 创建的自增列，在序列号自增时，如果原来 12345 有第五列被删除，新建的列序号会从6开始
        #conn.rollback()

        conn.commit
        #关闭连接，释放资源
        cursor.close();
        conn.close()
        return data



