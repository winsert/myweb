#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于在WX页面中显示"小于到期价值"的可转债、可交换债的最新价，三线价格，回售价等数据

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
def WXDQJZ0():
    
    ccList = []
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select name, Code, zgcode, Prefix, jian, jia, zhong, Note, zgj, hsqsr, hsj, dqr, position, shj, ll, ce, qs, qss, zgqsr, yjd, aqd, zgdm from cb0 ORDER BY Code"
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        #print tmp

        for cc in tmp:
            cList = []
            if cc[3] != 'QS' and cc[15] != 'e':
                name = cc[0] #名称
                cList.append(name)
                code = cc[1] #代码
                #cList.append(code)
                zzcode = cc[3]+cc[1]
                zz = float(getZZ(zzcode)) #查询转债价格
                cList.append(zz)

                zg_code = cc[3]+cc[2] #前缀+正股代码
                zg_name, zg_price, zg_zdf = getZG(zg_code) #查询正股价格, 涨跌幅
                #cList.append(zg_name)
                zgcode = cc[2] #正股代码
                #cList.append(zgcode)
                #cList.append(zg_price)
                zg_zdf = round(zg_zdf, 2)
                #cList.append(zg_zdf)

                jian = cc[4] #建仓价
                #cList.append(jian)
                jia = cc[5] #加仓价
                #cList.append(jia)
                zhong = cc[6] #重仓价
                #cList.append(zhong)
                note = cc[7] #说明
                #cList.append(note)

                zgj = float(cc[8]) #转股价
                #cList.append(zgj)
                #cList.insert(7, zgj)
                zgqsr = cc[18] #转股起始日
                #cList.append(zgqsr)

                if zg_price != 0:
                    zgjz = round((100/zgj)*zg_price, 2) #计算转股价值
                    #cList.append(zgjz)
                    yjl = round((zz-zgjz)/zgjz*100, 2) #计算溢价率
                    #cList.append(yjl)
                    #cList.insert(6, yjl)
                    #qsj = round((zgj * 1.3), 2) #计算强赎价
                    #qsl = round((zg/zgj -1)*100, 2) #计算强赎率
                else:
                    yjl = u"停牌"
                    #cList.insert(6, yjl)
                    #cList[5] = u"停牌"

                position = cc[12] #已购买的张数
                #cList.append(position)

                dqr = cc[11] #到期日
                #cList.append(dqr)
                synx = getSYNX(dqr) #计算剩余年限
                cList.append(synx)
        
                shj = cc[13] #赎回价
                ll = cc[14] #每年的利率
                dqjz = getDQJZ(synx, shj, ll) #计算到期价值
                cList.insert(2, dqjz)
                dqsyl = round((dqjz/zz - 1) * 100, 2) #计算到期收益率
                #cList.append(dqsyl)
                dqnh = round(dqsyl/synx, 2) #计算到期年化收益率
                cList.insert(0, dqnh)
    
                qs = cc[16] #已强赎天数
                #cList.append(qs)
                #qss = cc[17] #剩余天数
                #cList.append(qs)

                for i in range(1,5): #由到期收益率计算转债的价格
                    syl = 1 + (i * synx)/100
                    dhj = round((dqjz/syl), 3)
                    cList.append(dhj)

                yjd = cc[19] #研究度
                cList.append(yjd) #增加研究度
                aqd = cc[20] #安全度
                cList.append(aqd) #增加安全度
                zgdm = cc[21] #评级
                cList.append(zgdm) #增加评级

                cList.append(jian)
                cList.append(jia)
                cList.append(zhong)
                cList.append(note)

                if cList[2] <= dqjz and jian > 80.0 and qs <= 1: #转债现价<=到期价值 and 建仓价>70 and 还没有开始强赎
                    ccList.append(cList)
                    #print ccList

        ccList.sort()
        #print ccList
        return ccList

    except Exception, e :
        print name
        error_msg = u'主程序报错：'+str(e)
        print error_msg
        #ccList.append(name)
        ccList.append(e)
        return ccList

if __name__ == '__main__':
    wxdqjz = WXDQJZ0()
    #print wxdqjz
    for msgs in wxdqjz:
        print
        for msg in msgs:
            print msg