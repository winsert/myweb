#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 用于更新所有转债的最高价和最低价

__author__ = 'winsert@163.com'

import sqlite3, urllib2

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore')
    return html

# 用于查询指定证券的价格
def getZZ(zzCode):
    key = zzCode
    url = "http://hq.sinajs.cn/list="+key #生成用于查询的URL
    try:
        resp = bsObjForm(url)
        tmp_list = resp.split(',')
        zz_hp = float(tmp_list[4]) #获取证券当日最高价
        zz_lp = float(tmp_list[5]) #获取证券当日最低价
        return zz_hp, zz_lp
    except:
        zz_hp = 0
        zz_lp = 0
        return zz_hp, zz_lp

#对cb.db中HPrice的值进行修改
def getSQLiteHP(code, newHP):
    cc = code
    hp = newHP

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET HPrice = %r WHERE Code = %s" % (hp, cc) 
        curs.execute(sql)
        conn.commit()
        curs.close()
        conn.close()

    except Exception, e0:
        print 'getSQLiteHP ERROR :',e0

#对cb.db中LPrice的值进行修改
def getSQLiteLP(code, newLP):
    cc = code
    lp = newLP

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET LPrice = %r WHERE Code = %s" % (lp, cc) 
        curs.execute(sql)
        conn.commit()
        curs.close()
        conn.close()

    except Exception, e1:
        print 'getSQLiteLP ERROR :',e1

#从cb.db数据库中提取可转债数据进行"高价折扣法"分析
def getArrange():
    hpmsg_list = []
    hpmsg = ''
    lpmsg_list = []
    lpmsg = ''
    msg_list = []
    msg = ''

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select name, Code, Prefix, HPrice, LPrice from cb" 
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()

        for cc in tmp:
            name = cc[0] #转债名称
            code = cc[1] #转债代码
            zzcode = cc[2]+cc[1] #前缀+转债代码
            hp = float(cc[3]) #原最高价
            lp = float(cc[4]) #原最低价

            zz_hp, zz_lp = getZZ(zzcode) #查询转债当日最高价，最低价
            print name, hp, zz_hp, lp, zz_lp

            if zz_hp > 0: #排除停牌

                if zz_hp > hp: #比原最高价高
                    getSQLiteHP(code, zz_hp)
                    hpmsg = name+u' 前高价:'+str(hp)+u' 已更新为 新高价:'+str(zz_hp)
                    hpmsg_list.append(hpmsg)

                if zz_lp < lp: #比原最低价低
                    getSQLiteLP(code, zz_lp)
                    lpmsg = name+u' 前低价:'+str(lp)+u' 已更新为 新低价:'+str(zz_lp)
                    lpmsg_list.append(lpmsg)

    except Exception,e2:
        print 'getArrange ERROR :',e2

    #print hpmsg_list, lpmsg_list
    msg_list = hpmsg_list + lpmsg_list

    for i in msg_list:
        print i
    print

    if len(msg_list) == 0:
        msg = u'没有转债需要更新最高最低价！'
    else:
        msg = '|'.join(msg_list)

    return msg

if __name__ == '__main__':
    
    msg = getArrange()
    print msg
    print
