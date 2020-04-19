#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于查询,计算指定转债的溢价率
__author__ = 'winsert@163.com'

import sqlite3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#查询计算平均溢价率
def getYJL(zz_code):
    try:
        conn = sqlite3.connect('dd.db')
        curs = conn.cursor()
        sql = "select * from %s " %zz_code 
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        print u"共有"+str(len(tmp))+u"天交易数据。"

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
        print u'\n转债名称：', name

        zzcode = tmp[0][5] #转债代码
        #print u'转债代码：', zzcode
        return 'c'+zzcode

    except Exception, e:
        print 'getcb(alias)_error is: ', e

if __name__ == '__main__':
    alias = raw_input(u'输入可转债的简称缩写：')
    zz_code = getcb(alias) #查询转债的前缀+代码
    getYJL(zz_code) #查询计算溢价率