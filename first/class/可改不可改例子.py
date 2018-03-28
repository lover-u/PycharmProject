#_*_coding:utf-8 _*_

class test1:
    def __init__(self):
        self.__pravite = 'test1'

    @property
    def show(self):
        return self.__pravite


class test2:
    def __init__(self):
        self.__pravite = 'test2'

    @property
    def show(self):
        return self.__pravite
    @show.setter
    def show(self,value):
        self.__pravite = value

t1 = test1()
print t1.show
t1.show =  'change 1'
print t1.show


t2 = test2()
print t2.show
t2.show =  'change 2'
print t2.show