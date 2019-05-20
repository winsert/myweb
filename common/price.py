#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 查询股票、指数、可转债、可交换债的今开价、昨收价、最新价、最高价、最低价等数据

__author__ = 'winsert@163.com'

import urllib2

# 用于解析URL页面
def getHTML(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore')
    return html

# 用于查询指定证券的价格
def getPrice(key):
    plist = []
    url = "http://hq.sinajs.cn/list="+key #生成用于查询的URL
    try:
        resp = getHTML(url)
        tmp_list = resp.split(',')
        #print tmp_list
        name = tmp_list[0][-4:]
        print name
        plist.append(name)
        start_price = float(tmp_list[1]) #今日开盘价
        plist.append(start_price)
        yestday_end_price = float(tmp_list[2]) #昨日收盘价
        plist.append(yestday_end_price)
        new_price = float(tmp_list[3]) #最新价
        plist.append(new_price)
        high_price = float(tmp_list[4]) #今日最高价
        plist.append(high_price)
        low_price = float(tmp_list[5]) #今日最低价
        plist.append(low_price)
        print plist
        return plist
    except Exception, e:
        print 'getPrice ERROR :', e

if __name__ == '__main__':

    sci = ['sh601006', 'sh113021', 'sh132018', 'sz399006']

    for key in sci:
        getPrice(key)
