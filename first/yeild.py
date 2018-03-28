
#_*_ coding:utf-8 _*_
'''
print range(10)
print xrange(10)             #xrange 表示它只有在被遍历的时候才会被生成，没被遍历只是一个生成器，与readlines  和xreadlines 类似，只有在for
                              #循环才执行一次，输出一个值
for item in xrange(10):
    print item
'''


def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
'''
re = foo()
print re
for item in re:
    print item
'''

def Areadlines():
    seek = 0
    while True:
        with open(r'C:\work\temp.txt','r') as f :      #利用with进行open的时候，会自动把文件close掉，不用手动f.close
            f.seek(seek)                                   #前面加r  路径是字符串，里面包含了个\t，是个转义符号，所以文件路径有问题。win下路径分隔符用的是反斜杠导致了这个问题。
                                                           #你改成这样 f = open(r'F:\Dropbox\python\test.txt', 'r') 。在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return                              #return 之后整个函数都退出
print Areadlines()                         #这样执行只是一个生成器    用于延迟生成，以后可能会用到非阻塞，多进程的异步编程
for item in Areadlines():                  #迭代输出文件的内容
    print item



#yeild 做 x relase  做延迟，保存当前在函数内执行的状态，下次再执行时接着执行
