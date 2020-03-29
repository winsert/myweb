#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于在weixin页面中显示可转债、可交换债的最新价，三线价格，回售价等数据
__author__ = 'winsert@163.com'

import sqlite3, urllib2
from datetime import datetime

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore')
    return html

# 用于查询正股的价格
def getZG(zgCode):
    key = zgCode
    url = "http://hq.sinajs.cn/list="+key #生成用于查询的URL
    try:
        resp = bsObjForm(url)
        tmp_list = resp.split(',')
        zg_name = tmp_list[0][-4:]
        zgzr_price = float(tmp_list[2]) #获取正股昨日收盘价
        zg_price = float(tmp_list[3]) #获取正股最新价格
        if zg_price != 0:
            zg_zdf = round((zg_price/zgzr_price)*100, 2) -100 
            return zg_name, zg_price, zg_zdf
        else:
            zg_price = 0.0
            zg_zdf = 0.0
            return zg_name, zg_price, zg_zdf
    except Exception, e:
        zg_name = 'ERROR'
        zg_price = e
        zg_zdf = 0.0
        return zg_name, zg_price, zg_zdf

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
    else:
        y = inty

    l = mnlv.split(',') #转成列表
    for i in range (len(l)-y, len(l)-1):
        dqjz = dqjz +round(float(l[i])*0.8, 2)

    dqjz = dqjz + j
    return dqjz

# 主程序
def getWXCX():
    cbLists = []
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select * from cb where code>0"
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        #print tmp

        for cb in tmp:
            cbList = []
            name = cb[3] #名称
            cbList.append(name)
            zzcode = cb[7]+cb[5]
            zz = float(getZZ(zzcode)) #查询转债价格
            cbList.append(zz)

            zg_code = cb[7]+cb[6] #前缀+正股代码
            zg_name, zg_price, zg_zdf = getZG(zg_code) #查询正股价格, 涨跌幅
            zgcode = cb[6] #正股代码
            zg_zdf = round(zg_zdf, 2)

            jian = cb[12] #建仓价
            cbList.append(jian)
            jia = cb[13] #加仓价
            cbList.append(jia)
            zhong = cb[14] #重仓价
            cbList.append(zhong)
            note = cb[15] #说明
            cbList.append(note)

            zgqsr = cb[16] #转股起始日
            #cbList.append(zgqsr)
            zgj = float(cb[17]) #转股价
            #cbList.append(zgj)

            if zg_price != 0:
                zgjz = round((100/zgj)*zg_price, 2) #计算转股价值
                #cbList.append(zgjz)
                yjl = round((zz-zgjz)/zgjz*100, 2) #计算溢价率
                #cbList.append(yjl)
                #qsj = round((zgj * 1.3), 2) #计算强赎价
                #qsl = round((zg/zgj -1)*100, 2) #计算强赎率
            else:
                yjl = u"停牌"
                #cbList.append(yjl)
                #cbList[5] = u"停牌"

            dqr = cb[19] #到期日
            #cbList.append(dqr)
            synx = getSYNX(dqr) #计算剩余年限
            cbList.append(synx)
        
            shj = cb[20] #赎回价
            ll = cb[24] #每年的利率
            dqjz = getDQJZ(synx, shj, ll) #计算到期价值
            cbList.append(dqjz)
            dqsyl = round((dqjz/zz - 1) * 100, 2) #计算到期收益率
            #cbList.append(dqsyl)
            dqnh = round(dqsyl/synx, 2) #计算到期年化收益率
            cbList.insert(0, dqnh)
        
            qs = cb[25] #强赎计数

            if cbList[2] <= jian : #转债现价<=建仓价
                cbLists.append(cbList)

        cbLists.sort()
        #print ccList
        return cbLists

    except Exception, e :
        print name
        error_msg = u'getWXCX报错：'+str(e)
        print error_msg
        cbLists.append(e)
        return cbLists

if __name__ == '__main__':
    cbLists = getWXCX()
    
    for msgs in cbLists:
        print
        for msg in msgs:
            print msg