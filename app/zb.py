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

# 计算剩余年限
def getSYNX(dqr):
    ymd = dqr #到期日
    y = ymd.split('-')
    d1 = datetime(int(y[0]), int(y[1]), int(y[2]), 0, 0)
    synx = round((d1 - datetime.now()).days / 365.00, 2)
    return synx

# 计算到期价值
def getDQJZ(synx, shj,  ll):
    y = synx #剩余年限
    j = float(shj) #赎回价
    mnlv = ll #每年的利率
    dqjz = 0.0

    inty = int(y)
    if y > inty: 
        y = inty + 1

    l = mnlv.split(',') #转成列表
    for i in range (len(l)-y, len(l)-1):
        dqjz = dqjz +round(float(l[i])*0.8, 2)

    dqjz = dqjz + j
    return dqjz

# 进行占比分析
def getZB():
    
    ccList = []
    zbList = []
    
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select name, Prefix, Code, position, dqr, shj, ll from cb ORDER BY Code"
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
                total1 = round((zz * position), 2) #计算转债价格X持仓数量
                cList.append(total1)

                dqr = cc[4] #到期日
                synx = getSYNX(dqr) #计算剩余年限
                shj = cc[5] #赎回价
                ll = cc[6] #每年的利率
                dqjz = getDQJZ(synx, shj, ll) #计算到期价值
                cList.append(dqjz)
                total2 = round((dqjz * position), 2) #到期价值X持仓数量
                cList.append(total2)
                ccList.append(cList)

        sztotal = 0.0 #按市价计算总市值
        for x in ccList:
            sztotal = sztotal + x[4]

        for y in ccList: #按市价计算占比
            zb = round((y[4] / sztotal)*100, 2)
            y.insert(5, zb)
            zbList.append(y)

        dqtotal = 0.0 #按到期价值计算总市值
        for z in zbList:
            dqtotal = dqtotal + z[7]

        diff = dqtotal - sztotal

        return zbList, sztotal, dqtotal, diff

    except Exception, e :
        #ccList.append(name)
        error_msg = u'zb.py的getZB()报错：'+str(e)
        ccList.append(e)
        return ccList

if __name__ == '__main__':
    zb, sztotal, dqtotal, diff = getZB()
    for msg in zb:
        print msg
    print u"按到期价值计算的总市值是="+str(dqtotal)+u"元，按市价计算的总市值="+str(sztotal)+u"元，差额="+str(diff)
