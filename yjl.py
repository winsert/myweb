#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于查询,计算指定转债的溢价率
__author__ = 'winsert@163.com'

import sqlite3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from cbond.sina import getZZ #查询转债的交易数据
from cbond.sina import getZG #查询正股的交易数据

#查询计算平均溢价率
def getAvgYJL(zz_code):
    try:
        conn = sqlite3.connect('dd.db')
        curs = conn.cursor()
        sql = "select * from %s " %zz_code 
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        print u"\n共有"+str(len(tmp))+u"天交易数据"

        Q = 1
        while Q:
            yjl = 0.0
            days = int(raw_input(u"\n计算最近多少个交易日的平均溢价率？"))
            if days == 0:
                print u"\n结束查询！\n"
                sys.exit()
            elif days > len(tmp):
                print u"只能查询"+str(len(tmp))+u"个交易日的平均溢价率！"
            else:
                for i in range(1, days+1):
                    yjl = yjl + float(tmp[-i][11])
                print str(days)+u"个交易日的平均溢价率："+str(round(yjl/days, 2))+"%."
        
    except Exception, e:
        print 'getYJL()_error is: ', e

# 按alias查询转债的代码
def getcb(alias):
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select * from cb where Alias = '%s'" %alias
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()

        name = tmp[0][3] #转债名称
        print u'\n可转债名称：', name

        zzcode = tmp[0][5] #转债代码
        zgcode = tmp[0][6] #转债代码
        prefix = tmp[0][7] #前缀
        zgj = tmp[0][17] #转股价
        print u"转  股  价："+str(zgj)

        zg = getZG(prefix+zgcode) #查询正股交易数据
        print u"正股最新价："+str(zg[2])
        zz = getZZ(prefix+zzcode) #查询转债交易数据
        print u"转债最新价："+str(zz[2])
        
        yjl = round((zz[2]/((100/zgj)*zg[2])-1)*100, 2)
        print u"转债溢价率："+str(yjl)+"%"
        return 'c'+zzcode

    except Exception, e:
        print 'getcb(alias)_error is: ', e

if __name__ == '__main__':
    alias = raw_input(u'输入可转债的简称缩写：')
    zz_code = getcb(alias) #查询转债的前缀+代码
    getAvgYJL(zz_code) #查询计算平均溢价率