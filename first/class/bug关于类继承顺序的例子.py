class A:
    def __init__(self):
        print 'this is A'
    def save(self):
        print 'save method from A'
class B(A):
    def __init__(self):
        print 'this is B'

class C(A):
    def __init__(self):
        print 'this is C'
    def save(self):
        print 'save method from --C--'
class D(B,C):
    def __init__(self):
        print 'this is D'


c = D()
c.save()

class A(object):
    def __init__(self):
        print 'this is A'
    def save(self):
        print 'save method from A'
class B(A):
    def __init__(self):
        print 'this is B'

class C(A):
    def __init__(self):
        print 'this is C'
    def save(self):
        print 'save method from --C--'
class D(B,C):
    def __init__(self):
        print 'this is D'


c = D()
c.save()


#应该是先搜b 再搜c 再搜a （广度优先），之前的顺序成了 先b 然后a (深度优先
