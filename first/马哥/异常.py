# _*_ coding:utf-8 _*_
try:
	while True:
		d1 = raw_input("An int:")
		if d1 == "quit": break
		d2 = raw_input("Another integer:")            # raw_input 输入全为字符
		print int(d1) / int(d2)
except 	ZeroDivisionError, e :
	print "被除数不能为 0"
except 	ValueError,e:
	print "Not string"

