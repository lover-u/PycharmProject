#_*_ coding:utf-8 _*_

def  f1(seq1,seq2):
	if not seq1 or not seq2:
		raise ValueError, "seq must not be empty"                 # ValueError是一个对象 所以不用加引号
	print [ (x,y) for x in seq1 for y in seq2 ]                   # 这种叫列表解析，前面是一个表达式 后面是跟循环

l1 = [1,2,3]
l2 = ['a','b','c']
f1(l1,l2)                                                         #这种是嵌套输出  还有一种zip
l3 = []
f1(l1,l3)