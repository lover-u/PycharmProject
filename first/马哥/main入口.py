# -*- coding:utf-8 -*-
x = 30
def printInfo():
	print x + 30

class MyClass():
	data = 'hello MyClass'
	def __init__(self,who):
		self.name = who
	def printName(self):
		print self.data,self.name

if __name__ ==  '__main__':                      #代表可以自我执行，不只是只能导入，__main__是程序入口
	printInfo()
	ins1 = MyClass('tom')
	print ins1.data,ins1.name



