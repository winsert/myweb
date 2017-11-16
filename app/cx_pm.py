#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 查询PM2.5数据的模块。

__author__ = 'Andy'

import requests
from bs4 import BeautifulSoup

# 用于解析URL页面:
def getSoup(url):
    soup_url = url 
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    content = requests.get(soup_url, headers=headers) 
    soup = BeautifulSoup(content.text, 'html.parser')
    return soup

# 获取PM2.5数据：
def getPM():

    msg_list = []

    try:
        tmp = []
        url = 'http://www.pm25.in/rank'
        soup = getSoup(url)
        #print soup
        result = soup.find('tbody').find_all('tr')
        #print result[2].contents

        for x in result:
            #print x.contents[3].string
            if x.contents[3].string == u'济南':
                for y in x.contents:
                    if y.string != '\n':
                        tmp.append(y.string)
        #print tmp
        msg = u'全国排名: '+tmp[0]
        msg_list.append(msg)
        msg = u'空气质量: '+tmp[3]
        msg_list.append(msg)
        msg = 'AQI     : '+tmp[2]
        msg_list.append(msg)
        msg = 'PM2.5   : '+tmp[5]
        msg_list.append(msg)
        msg = 'PM10    : '+tmp[6]
        msg_list.append(msg)
        msg = u'一氧化碳: '+tmp[7]
        msg_list.append(msg)
        msg = u'二氧化氮: '+tmp[8]
        msg_list.append(msg)
        msg = u'二氧化硫: '+tmp[11]
        msg_list.append(msg)
        msg = u'臭氧1小时平均:'+tmp[9]
        msg_list.append(msg)
        msg = u'臭氧8小时平均: '+tmp[10]
        msg_list.append(msg)

        return msg_list

    except Exception, e:
        print e
        msg_list.append(e)
        return msg_list

if __name__ == '__main__':
    msg_list = getPM()
    for msg in msg_list:
        print msg
