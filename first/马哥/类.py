#!/user/bin/python
#_*_coding:utf-8 _*_
class Bag:
    def __init__(self,x):
        self.data = []
    def add(self, x):
        self.data.append(x)
        return Add.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
Add = Bag('a')
l = Add.data.append('x')                #这里Add.data是一个完整的list  ，对应印象笔记 python知识点标签  列表文章名例子
print Add.data
print 'Add.data type is  %s ' %(type(Add.data))
print type(l)
print l   #输出None

#d = Bag.data
s =  Add.add('xc')

print s
print Add.addtwice('x')
#print d


'''
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
#['roll over']
e.tricks
#['play dead']
'''