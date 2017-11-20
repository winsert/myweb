#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于对已建仓的可转债、可交换债进行占比分析

__author__ = 'winsert@163.com'

import sqlite3, urllib2
from datetime import datetime

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore')
    return html

# 用于查询转债的价格
def getZZ(zzCode):
    key = zzCode
    url = "http://hq.sinajs.cn/list="+key #生成用于查询的URL
    resp = bsObjForm(url)
    tmp_list = resp.split(',')
    zz_price = float(tmp_list[3]) #获取转债实时价格
    if zz_price == 0:
        zz_price = float(tmp_list[2]) #获取转债昨日收盘价
        return zz_price
    else:
        return zz_price

# 主程序
def getZB():
    
    ccList = []
    zbList = []
    
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select name, Prefix, Code, position from cb ORDER BY Code"
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        #print tmp

        for cc in tmp:
            if cc[1] != 'QS' and cc[3] != 0: #已建仓
                cList = []
                name = cc[0] #名称
                cList.append(name)
                code = cc[2] #代码
                cList.append(code)
                zzcode = cc[1]+cc[2]
                zz = float(getZZ(zzcode)) #查询转债价格
                cList.append(zz)
                position = cc[3] #已购买的张数
                cList.append(position)
                subtotal = round((zz * position), 2) #计算转债价格X持仓数量
                cList.append(subtotal)
                ccList.append(cList)

        total = 0.0
        for x in ccList: #计算总市值
            total = total + x[4]

        for y in ccList: #计算占比
            zb = round((y[4] / total)*100, 2)
            y.append(zb)
            zbList.append(y)

        return zbList

    except Exception, e :
        #ccList.append(name)
        error_msg = u'zb.py的主程序报错：'+str(e)
        ccList.append(e)
        return ccList

if __name__ == '__main__':
    mcx = getZB()
    for msg in mcx:
        print msg
