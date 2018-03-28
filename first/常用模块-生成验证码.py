#_*_ coding:utf-8 _*_
import random
print random.random()
#print help(random)
print random.randint(1,5)   #输出1到5之间的随机数
print random.randrange(1,3)  #输出大于1小于3的数
cha = random.randint(65,90)
print chr(cha),'测试'


code = []
for i in range(6):
    #print i
    if i == random.randint(1,5):
        print random.randint(1,5)
        code.append(str(random.randint(1,5)))
    else:
        cha = random.randint(65, 90)
        #print chr(cha)
        #code = chr(cha)
        code.append(chr(cha))
print code
print  ''.join(code)


#字符串拼接 +=  和join  的区别  join 效率高
