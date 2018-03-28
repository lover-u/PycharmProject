#_*_coding:utf-8 _*_

from utility.sql_helper import MySQLHelper

class Admin(object):                          #model层定义了index能使用的各种功能，方法，并去helper里的内容
    def __init__(self):
        self.__helper = MySQLHelper()

    def Get_One(self,id):
        sql = "select * from UserInfo where id=%s"
        params = (id,)
        return self.__helper.Get_One(sql,params)

    def Checkvalidata(self,username,password):
        sql = "select * from UserInfo where name=%s and password=%s"
        params =(username,password,)
        return self.__helper.GetOne(sql,params)