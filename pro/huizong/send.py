#!/usr/bin/env python
#coding=utf-8
#auther wangziyin@le.com 2016-12-28

import requests
import json, logging
from logging.handlers import TimedRotatingFileHandler
import sys, os
from html import HTML
reload(sys)
sys.setdefaultencoding('utf-8')

LOG_PATH = "./tree_pare.log"
LOG_LEVEL = "DEBUG"

log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
formatter = logging.Formatter(log_fmt)
#创建TimedRotatingFileHandler对象
log_file_handler = TimedRotatingFileHandler(filename=LOG_PATH, when="M", interval=2, backupCount=2)
#log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
#log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
log_file_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
log.addHandler(log_file_handler)

class Sender():
    '''
    The API of send sms and email
    '''
    def __init__(self):
        self.base_url = "http://api.911.letv.cn/alarm"
        self.token = "a5da9abe8195f43974ad03756c4da9bc"

    @staticmethod
    def mobile_paser():

        result = {}
        CONN_FILE = "./user_con.txt"
        if not os.path.exists(CONN_FILE):
            return {}
        with open(CONN_FILE, "rb") as cf:
            mobiles = cf.readlines()
            for m in mobiles:
                if len(m.split(":")) > 2:
                    result[m.split(":")[1]] = m.split(":")[2].strip()
        return result

    @staticmethod
    def mobile_paser2():

        result = {}
        CONN_FILE = "./user_con.txt"
        if not os.path.exists(CONN_FILE):
            return {}
        with open(CONN_FILE, "rb") as cf:
            mobiles = cf.readlines()
            for m in mobiles:
                if len(m.split(":")) > 2:
                    result[m.split(":")[1].split("@")[0]] = m.split(":")[2].strip()
        return result

    @staticmethod
    def get_mobile(name):

        user_conns = Sender.mobile_paser()
        return user_conns.get(name)

    def SMS(self, mobile, message):

        url = self.base_url + "/sms"
        if isinstance(mobile, str) or isinstance(mobile, unicode):
            data = {
                "token"     : self.token,
                "mobile"    : mobile,
                "msg"       : message,
            }
        elif isinstance(mobile, list):
            data = {
                "token"     : self.token,
                "mobile"    : ",".join(mobile),
                "msg"       : message,
            }
        else:
            return False, "Parameter Error, mobile must be string or list"

        ret = requests.get(url=url, params=data)
        if ret.status_code != 200:
            return False, ret.reason
        if json.loads(ret.text)["status"] != 1:
            return False, json.loads(ret.text)["msg"]

        return True, "OK"

    def EMAIL(self, email, title, message):

        url = self.base_url + "/email"
        if isinstance(email, str) or isinstance(email, unicode):
            data = {
                "token": self.token,
                "email": email,
                "title": title,
                "msg": message,
            }
        elif isinstance(email, list):
            data = {
                "token" : self.token,
                "email": ",".join(email),
                "title": title,
                "msg": message,
            }
        else:
            return False, "Parameter Error, email must be string or list"
        ret = requests.post(url=url, data=json.dumps(data), headers={"Content-type": "application/json"})
        if ret.status_code != 200:
            logging.error(ret.text)
            return False, ret.reason
        if json.loads(ret.text)["status"] != 1:
            return False, json.loads(ret.text)["msg"]

        return True, "OK"


    def VOICE(self, mobile, message):

        url = self.base_url + "/voice"
        if isinstance(mobile, str) or isinstance(mobile, unicode):
            data = {
                "token"     : self.token,
                "mobile"    : mobile,
                "msg"       : message,
            }
        elif isinstance(mobile, list):
            data = {
                "token"     : self.token,
                "mobile"    : ",".join(mobile),
                "msg"       : message,
            }
        else:
            return False, "Parameter Error, mobile must be string or list"
        ret = requests.get(url=url, params=data)
        if ret.status_code != 200:
            return False, ret.reason
        if json.loads(ret.text)["status"] != 1:
            return False, json.loads(ret.text)["msg"]

        return True, "OK"

if __name__ == "__main__":
    base_url = "http://api.911.letv.cn/alarm"
    token = "a5da9abe8195f43974ad03756c4da9bc"
    base_dir = "/letv/servertree/no_tree/list/rsync"

    files = []

    mobiles = ["18511285745"]
    emails = ["wangziyin@le.com",
          ]

    messages = u"截止4月28日，您名下仍有设备未完成服务树梳理，这些设备将被回收并进入下线流程，详细请参看刚刚由“乐视云基础架构”发出的邮件，谢谢。"
    sender = Sender()
    sender.EMAIL(emails, 'TTTTTT', 'XXXXXX')