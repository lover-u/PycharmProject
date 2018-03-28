# -*- coding:utf-8 -*-
import os, sys, re


def lastline():
    global pos

    while True:
        pos = pos - 1
        try:
            f.seek(pos, 2)  # 从文件末尾开始读
            if f.read(1) == '\n':
                break
        except:  # 到达文件第一行，直接读取，退出
            f.seek(0, 0)
            print f.readline().strip()
            return

    print f.readline().strip()


if __name__ == "__main__":                #功能 获取文件倒数n行

    f = open('/var/log/accsess.log', 'rb')  # ‘r’的话会有两个\n\n
    pos = 0
    for line in range(2):  # 需要倒数多少行就循环多少次
        lastline()
    f.close()