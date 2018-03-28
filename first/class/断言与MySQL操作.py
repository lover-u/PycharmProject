#_*_coding:utf-8 _*_

assert(1==1)   #一句话 ，后面是判断条件 ，比如在是否执行前判断一下

'''
import MySQLdb
#建立和数据库系统的连接
conn = MySQLdb.connect(host='localhost',user='root',passwd='123',db='08day5')


#获取操作游标
#cur = conn.cursor
cursor = conn.cursor()
#执行SQL,创建一个数据库.
sql = "insert into UserInfo (name,address) value(%s,%s)"
params = ('alex_1','usa')
reCount = cursor.execute(sql,params)
#cursor.execute("""create database python """)
#recount = cursor.execute('select * from UserInfo')
data = cursor.fetchall()      #获取查询的数据

#MySQL 创建的自增列，在序列号自增时，如果原来 12345 有第五列被删除，新建的列序号会从6开始


#关闭连接，释放资源
cursor.close();
conn.close()
'''

import MySQLdb
#建立和数据库系统的连接
conn = MySQLdb.connect(host='localhost',user='root',passwd='123',db='08day5')


#获取操作游标
cursor = conn.cursor()
#执行SQL,创建一个数据库.
cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)           #这种方式拿出cursor拿出的数据是一个字典
sql = "insert into UserInfo (name,address) value(%s,%s)"
#sql = "delete from UserInfo where id = %s"    #删除操作
#params = ('1',)   # 这里加不加逗号都是一样的 加逗号说明是一个序列
#sql = "update UserInfo set name = %s where id =7"  #更新操作
#params = ('sb',)
params = ('alex_1','usa')
reCount = cursor.execute(sql,params)

#MySQL 创建的自增列，在序列号自增时，如果原来 12345 有第五列被删除，新建的列序号会从6开始
conn.rollback()

conn.commit
#关闭连接，释放资源
cursor.close();
conn.close()

print reCount      #在这输出   这时候是数据库是还没有数据的

data = cursor.fetchone()   #比如说拿第一行
print cur.fetchone()  #第一次执行，拿出第一次操作的数据，第二次执行拿出第二次的数据
data = cursor.fetchone()     #拿第二行
print cur.fetchone()
#cursor.scroll(0,mode='absolute')     #这时候会在执行一条第二条数据，因为上一次后现在的位置是3，回退1，是2
cursor.scroll(-1,mode='relative')      #绝对定位到第一行数据  这时候这会多输出一行数据

#指针的两个模式
cursor.scroll(-1,mode='relative')   #相对定位 往回走一条
cursor.scroll(0,mode='absolute')   #绝对定位


#循环插入的例子
'''
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1234',db='07day05db')
cur = conn.cursor()

li =[                     #插入一条数据的时候是一个元组，需要插入多条时就是多个元组组成的列表
     ('alex','usa'),
     ('sb','usa'), 
]
reCount = cur.executemany('insert into UserInfo(Name,Address) values(%s,%s)',li)

conn.commit()
cur.close()
conn.close()

print reCount
'''


'''
sql = "insert into media(address) value(%s)"
params = ('/usr/bin/a.txt',
print cursor.lastrowid        #这种方式可以获取最后一行ID 在ID自增时返回很有用，即返回自增ID
'''
