#_*_coding:utf-8 _*_
from Model.Admin import Admin


def main():
    user = raw_input('username:')
    pwd = raw_input("password:")
    admin = Admin()
    result = admin.Checkvalidata(user,pwd)
    print result
    if not result:
        print '用户名密码错误'
    else:
        print '进入后台界面'

if __name__ == '__main__':
    main()