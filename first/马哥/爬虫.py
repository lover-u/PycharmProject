# -*- coding:utf-8 -*-
import re
import urllib
def GetHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def GetImg(html):
	res = r"src=".+\.jpg" width"
	imgre = re.compile(res,)
	imglist = re.findall(imgre,html)

GetImg()
