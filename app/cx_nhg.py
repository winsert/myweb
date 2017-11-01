#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 查询逆回购的模块

__author__ = 'winsert@163.com'

import urllib2

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore')
    return html

# 用于查询逆回购的价格
def getNHG():

    nhg_dict = {'sh204001':8.00, 'sz131810':8.00} #预警价
    nhg_list = []
    nhg_msg = ''

    try:
        for key in nhg_dict:
            value = nhg_dict[key]
            #print key
            #print nhg_dict[key]
            url = "http://hq.sinajs.cn/list="+key #生成用于查询的URL
            resp = bsObjForm(url)
            tmp_list = resp.split(',')
            #print tmp_list
            #nhg_name = tmp_list[0][-4:] #逆回购名称
            new_price = float(tmp_list[3]) #获取逆回购最新价格
            zr_price = float(tmp_list[2]) #获取基金昨日价格
            #print zr_price
            #zdf = round((new_price/zr_price - 1)*100, 3) #计算涨跌
            if new_price == 0.0:
                nhg_list.append(zr_price)
            else:
                nhg_list.append(new_price)
                
        return nhg_list

    except Exception, e:
        print 'getWH ERROR :', e
        nhg_list.append(e)
        return nhg_list

if __name__ == '__main__':
    msg_list = getNHG()
    print msg_list
