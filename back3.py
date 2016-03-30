#!/usr/bin/python
# -*- coding: UTF-8 -*-
#http://bj.xiaozhu.com/search-duanzufang-p1-0/
#http://bj.xiaozhu.com/search-duanzufang-p13-0/
#标题
#地址
#日租金
#第一张房源图片链接
#房东图片链接
#房东性别
#房东名字

import requests
from bs4 import BeautifulSoup

url = 'http://bj.xiaozhu.com/fangzi/1466098635.html'

#url = 'http://bj.xiaozhu.com/fangzi/1466098635.html'

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,14)]


def get_page_link():
    for each_number in range(1,14): # 每页24个链接,这里输入的是页码
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(each_number))
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        for link in soup.select('a.resule_img_a'): # 找到这个 class 样为resule_img_a 的 a 标签即可
            print page_link.append(link)
#print get_page_link()
#return soup  成功发送请求



def geturl(url,data=None):
	req = requests.get(url)
	soup = BeautifulSoup(req.text,'lxml')
	titles = soup.select('div.pho_info > h4')[0].text
	addresss = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')[0].text
	prices = soup.select('div.day_l > span')[0].text
	horse_images = soup.select('#curBigImage')[0].get('src')
	horsemanamges = soup.select('div.member_pic > a > img')[0].get('src')
	horsenames = soup.select('a.lorder_name')[0].text
	horsesexs = soup.select('div.member_pic > div')[0].get('class')[0]
	print u'标题：',titles
	print u'地址：',addresss
	print u'价格：',prices
	print u'房东性别：',
	if horsesexs == "member_ico1":
		print u'女'
	else:
		print u'男'
	print u'房东图片地址：',horsemanamges
	print u'房东姓名：',horsenames
	print u'房子图片地址：',horse_images
print geturl(url)
#print urls




#print urls


#for title,address,price,horsemanamge,horsename,horsesex in zip(titles,addresss,prices,horsemanamges,horsenames,horsesexs):
#data = {

#		'titles':titles,
#		'addresss':addresss,
#		'prices':prices,
#		'horsemanamges':horsemanamges,
#		'horsenames':horsenames,
#		'horsesexs':horsesexs
#	}
#print data
	#return titles    #get content
	#return addresss
#print horsesex
