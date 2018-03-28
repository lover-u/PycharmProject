# _*_ coding:utf-8 _*_
from __future__ import division
def  jia(x,y):
	return x+y
def jian(x,y):
	return x-y
def cheng(x,y):
	return x*y
def chu(x,y):
	return x/y

#oprerator = {"+":jia,"-":jian,"*":cheng,"/":chu }              # python中不加引号的都是对象，这里chui报错，是因为没有定义，要不报错需要加双引号
oprerator = {"+":jia,"-":jian,"*":cheng,"/":"chui" }
print jia(3,2)
print oprerator["+"](3,2)
#print oprerator["/"](3,2)       #可以看出这执行的也是一个函数  NameError: name 'chui' is not defined
#print oprerator["%"](3,2)

def f(x,o,y):
	print oprerator.get(o)(3,2)

f(3,"+",2)                                  #这里会实现switch 的功能会自动判断 o 的情况，比如是加减乘除



