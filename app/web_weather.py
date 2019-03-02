#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 查询济南市多地天气实况信息的模块,为APP服务。

__author__ = 'Andy'

import requests, os, sys
from bs4 import BeautifulSoup

# 用于解析URL页面:
def getSoup(url):
    soup_url = url 
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    content = requests.get(soup_url, headers=headers) 
    soup = BeautifulSoup(content.text, 'html.parser')
    return soup

# 获取天气实况:
def getWeather():

    weather_list = []

    weather_url = "http://jnqx.jinan.gov.cn/jnszfqxj/front/zdz/list.do?type=1"
    soup = getSoup(weather_url)
    result = soup.find('div', align="center").find_all('td')

    wlist = []
    for w in result:
        wlist.append(w.get_text())

    print len(wlist)
    j = 0
    msg = []
    for i in range(len(wlist)):
        if j < 8:
            msg.append(wlist[0].strip())
            wlist.pop(0)
            j = j + 1
        else:
            weather_list.append(msg)
            msg = []
            j = 0
    ''' 
    address_msg = u'地点：'+wlist[16].strip().strip('\n').strip('\t').strip('\r')
    weather_list.append(address_msg)
    time_msg = u'时间：'+wlist[17]
    weather_list.append(time_msg)
    tempture_msg = u'温度：'+wlist[18].strip().strip('.')+u'℃'
    weather_list.append(tempture_msg)
    wet_msg = u'湿度：'+wlist[19].strip()+u'％'
    weather_list.append(wet_msg)
    wind_msg = u'风向：'+wlist[20]
    weather_list.append(wind_msg)
    wind_speed_msg = u'风速：'+wlist[21].strip()+u'm/s'
    weather_list.append(wind_speed_msg)
    rain_msg = u'雨量：'+wlist[22].strip()+u'mm/h'
    weather_list.append(rain_msg)
    pressure_msg = u'气压：'+wlist[23].strip()+u'hPa'
    weather_list.append(pressure_msg)
    '''
    #print weather_list

    return weather_list

if __name__ == '__main__':
    weather_list = getWeather()

    for msgs in weather_list:
        for msg in msgs:
            print msg,
        print

    print len(weather_list)
    print weather_list[78]
    print weather_list[78][6]
    print type(weather_list[78][6])
    if weather_list[78][6] == u'':
        print 'OK'
