#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于修改jian, jia, zhong, note, position, zgj数据

__author__ = 'winsert@163.com'

import sqlite3

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 查询指定转债的数据
def CX(alias):
    
    cx = alias
    clist = []
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select name, code, jian, jia, zhong, note, position, AVG, zgj, ll, LPrice, HPrice from cb where Alias = '%s'" %cx
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()

        name = tmp[0][0] #转债名称
        clist.append(name)
        code = tmp[0][1] #代码
        clist.append(code)
        jian = tmp[0][2] #建仓价
        clist.append(jian)
        jia = tmp[0][3] #加仓价
        clist.append(jia)
        zhong = tmp[0][4] #重仓价
        clist.append(zhong)
        note = tmp[0][5] #说明
        clist.append(note)
        position = tmp[0][6] #持仓
        clist.append(position)
        avg = tmp[0][7] #平均成本价
        clist.append(avg)
        zgj = tmp[0][8] #转股价
        clist.append(zgj)
        ll = tmp[0][9] #利率
        clist.append(ll)
        lprice = tmp[0][10] #新低价
        clist.append(lprice)
        hprice = tmp[0][11] #新高价
        clist.append(hprice)

        print
        print u'名  称：', name
        print u'代  码：', code
        print u'建仓价：', jian
        print u'加仓价：', jia
        print u'重仓价：', zhong
        print u'说  明：', note
        print u'持  仓：', position
        print u'平均价：', avg
        print u'转股价：', zgj
        print u'利  率：', ll
        print u'新低价：', lprice
        print u'新高价：', hprice
        print
        return clist

    except Exception, e :
        print 'CX() Error:', e
        sys.exit()

#对指定转债的'名称'进行修改
def Name(alias, name):
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        conn.text_factory = str #解决字符问题
        sql = "UPDATE cb SET Name = ? WHERE Alias = ?"
        curs.execute(sql, (name, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'名称 已修改为：', name

    except Exception, e:
        print 'Name() ERROR :', e
        sys.exit()

#对指定转债的'建仓价'进行修改
def Jian(alias, jian):
    alias = alias
    jian = float(jian)

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET jian = ? WHERE Alias = ?"
        curs.execute(sql, (jian, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'建仓价 已修改为：', str(jian)

    except Exception, e:
        print 'Jian() ERROR :', e
        sys.exit()

#对指定转债的'加仓价'进行修改
def Jia(alias, jia):
    alias = alias
    jia = float(jia)

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET jia = ? WHERE Alias = ?"
        curs.execute(sql, (jia, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'加仓价 已修改为：', str(jia)

    except Exception, e:
        print 'Jia() ERROR :', e
        sys.exit()

#对指定转债的'重仓价'进行修改
def Zhong(alias, zhong):
    alias = alias
    zhong = float(zhong)

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET zhong = ? WHERE Alias = ?"
        curs.execute(sql, (zhong, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'重仓价 已修改为：', str(zhong)

    except Exception, e:
        print 'Zhong() ERROR :', e
        sys.exit()

#对指定转债的‘说明’进行修改
def Note(alias, note):
    alias = alias
    note = note

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET note = ? WHERE Alias = ?"
        curs.execute(sql, (note, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'说明 已修改为：', str(note)

    except Exception, e:
        print 'Note() ERROR :', e
        sys.exit()

#对指定转债的'持仓'进行修改
def Position(alias, position):
    alias = alias
    position = int(position)

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET position = ? WHERE Alias = ?"
        curs.execute(sql, (position, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'持仓 已修改为：', str(position)

    except Exception, e:
        print 'Position() ERROR :', e
        sys.exit()

#对指定转债的'平均价'进行修改
def AVG(alias, avg):
    alias = alias
    avg = float(avg)

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET AVG = ? WHERE Alias = ?"
        curs.execute(sql, (avg, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'平均价 已修改为：', str(avg)

    except Exception, e:
        print 'AVG() ERROR :', e
        sys.exit()

#对指定转债的'转股价'进行修改
def ZGJ(alias, zgj):
    alias = alias
    zgj = float(zgj)

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET zgj = ? WHERE Alias = ?"
        curs.execute(sql, (zgj, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'转股价 已修改为：', str(zgj)

    except Exception, e:
        print 'ZGJ() ERROR :', e
        sys.exit()

#对指定转债的'利率'进行修改
def LL(alias, ll):
    alias = alias
    ll = ll

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET ll = ? WHERE Alias = ?"
        curs.execute(sql, (ll, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'利  率 已修改为：', str(ll)

    except Exception, e:
        print 'LL() ERROR :', e
        sys.exit()

#对指定转债的'新低价'进行修改
def Lprice(alias, lprice):
    alias = alias
    lprice = float(lprice)

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET LPrice = ? WHERE Alias = ?"
        curs.execute(sql, (lprice, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'新低价 已修改为：', str(lprice)

    except Exception, e:
        print 'Lprice() ERROR :', e
        sys.exit()

#对指定转债的'新高价'进行修改
def Hprice(alias, hprice):
    alias = alias
    hprice = float(hprice)

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET HPrice = ? WHERE Alias = ?"
        curs.execute(sql, (hprice, alias))
        conn.commit()
        curs.close()
        conn.close()

        print u'新高价 已修改为：', str(hprice)

    except Exception, e:
        print 'Hprice() ERROR :', e
        sys.exit()

if  __name__ == '__main__': 

    msg = u"""
    本程序用于修改：
    - 名  称 Name
    - 建仓价 jian
    - 加仓价 jia
    - 重仓价 zhong
    - 说  明 note
    - 新低价 LPrice
    - 持  仓 position
    - 平均价 avg
    - 转股价 zgj
    - 利  率 ll
    - 新低价 Lprice
    - 新高价 Hprice
    """
    print
    print msg
    alias = raw_input(u'输入可转债的简称缩写：')
    cx = CX(alias)
    yn = raw_input(u'是否要修改(y/n)？')
    if yn == 'n':
        sys.exit()
    #print cx
    
    print
    print u'原 名称：', str(cx[0])
    name = str(raw_input(u"请输入新 名称："))
    print name
    if name != '':
        Name(alias, name)
    else:
        print u'名称 没有修改！'

    print 
    print u'原 建仓价：', str(cx[2])
    jian = raw_input(u"请输入新 建仓价：")
    if jian != '':
        Jian(alias, jian)
    else:
        print u'建仓价 没有修改！'

    print
    print u'原 加仓价：', str(cx[3])
    jia = raw_input(u"请输入新 加仓价：")
    if jia != '':
        Jia(alias, jia)
    else:
        print u'加仓价 没有修改！'

    print
    print u'原 重仓价：', str(cx[4])
    zhong = raw_input(u"请输入新 重仓价：")
    if zhong != '':
        Zhong(alias, zhong)
    else:
        print u'重仓价 没有修改！'

    print
    print u'原 说明：', str(cx[5])
    note = unicode(raw_input(u"请输入新 说明："))
    if note != '':
        Note(alias, note)
    else:
        print u'说明 没有修改！'

    print
    print u'原 持仓：', str(cx[6])
    position = raw_input(u"请输入新 持仓：")
    if position != '':
        Position(alias, position)
    else:
        print u'持仓 没有修改！'

    print
    print u'原 平均价：', str(cx[7])
    avg = raw_input(u"请输入新 平均价：")
    if avg !='':
        AVG(alias, avg)
    else:
        print u'平均价 没有修改！'

    print
    print u'原 转股价：', str(cx[8])
    zgj = raw_input(u"请输入新 转股价：")
    if zgj != '':
        ZGJ(alias, zgj)
    else:
        print u'转股价 没有修改！'

    print
    print u'原 利  率：', str(cx[9])
    ll = raw_input(u"请输入新 利  率：")
    if ll != '':
        LL(alias, ll)
    else:
        print u'转股价 没有修改！'

    print
    print u'原 新低价：', str(cx[10])
    lprice = raw_input(u"请输入新 最低价：")
    if lprice != '':
        Lprice(alias, lprice)
    else:
        print u'新低价 没有修改！'

    print
    print u'原 新高价：', str(cx[11])
    hprice = raw_input(u"请输入新 最高价：")
    if hprice != '':
        Hprice(alias, hprice)
    else:
        print u'新高价 没有修改！'

    print
    print u'全部修改结果如下：'
    cx = CX(alias)