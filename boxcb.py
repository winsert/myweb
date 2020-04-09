#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于修改转债数据
__author__ = 'winsert@163.com'

import Tkinter as tk
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 查询指定转债的数据
def getcb(alias):
    cblist = []
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        #sql = "select name, code, zzcode, jian, jia, zhong, note, position, AVG, zgj, ll, HPrice, LPrice, aqd, pj, tmp from cb where Alias = '%s'" %alias
        sql = "select * from cb where Alias = '%s'" %alias
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()

        print
        name = tmp[0][3] #转债名称
        print u'名  称：', name
        cblist.append(['名   称：', ['name', name]])

        code = tmp[0][2] #特征码
        print u'特征码：', code
        cblist.append(['特征码：', ['code', code]])

        position = tmp[0][8] #持仓
        print u'持  仓：', position
        cblist.append(['持   仓：', ['position', position]])

        hprice = tmp[0][10] #新高价
        print u'新高价：', hprice
        cblist.append(['新高价：', ['hprice', hprice]])

        lprice = tmp[0][11] #新低价
        print u'新低价：', lprice
        cblist.append(['新低价：', ['lprice', lprice]])

        jian = tmp[0][12] #建仓价
        print u'建仓价：', jian
        cblist.append(['建仓价：', ['jian', jian]])

        jia = tmp[0][13] #加仓价
        print u'加仓价：', jia
        cblist.append(['加仓价：', ['jia', jia]])

        zhong = tmp[0][14] #重仓价
        print u'重仓价：', zhong
        cblist.append(['重仓价：', ['zhong', zhong]])

        note = tmp[0][15] #说明
        print u'说  明：', note
        cblist.append(['说   明：', ['note', note]])
        
        zgj = tmp[0][17] #转股价
        print u'转股价：', zgj
        cblist.append(['转股价：', ['zgj', zgj]])

        ll = tmp[0][24] #利率
        print u'利  率：', ll
        cblist.append(['利   率：', ['ll', ll]])

        qs = tmp[0][25] #已强赎天数
        print u'强赎天：', qs
        cblist.append(['强赎天：', ['qs', qs]])

        qss = tmp[0][26] #剩余天数
        print u'剩余天：', qss
        cblist.append(['剩余天：', ['qss', qss]])

        aqd = tmp[0][28] #安全度
        print u'安全度：', aqd
        cblist.append(['安全度：', ['aqd', aqd]])

        pj = tmp[0][30] #评级
        print u'评  级：', pj
        cblist.append(['评   级：', ['pj', pj]])

        tmp = tmp[0][31] #涨跌幅
        print u'涨跌幅：', tmp
        cblist.append(['涨跌幅：', ['tmp', tmp]])
        print
        #print cblist
        return cblist

    except Exception, e :
        print 'getcb() Error:', e
        sys.exit()

#update
def UpDate(alias, k, kk, v):
    #print alias, k, kk, v
    #sql = "UPDATE cb SET " + kk +"= ? WHERE Alias = ?"
    #print sql
    
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "UPDATE cb SET " + kk +"= ? WHERE Alias = ?"
        curs.execute(sql, (v, alias))
        conn.commit()
        curs.close()
        conn.close()

        print "  " + k + u"已修改为 ", v

    except Exception, e:
        print 'UpDate() ERROR :', e
        sys.exit()

def lab_show(cblist):
    for i in range(len(cblist)):
        for j in range(2):
            if j == 0:
                tk.Label(frame1, text=cblist[i][0], font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
            else:
                v2 = tk.StringVar(value=cblist[i][1][1])
                tk.Entry(frame1, textvariable=v2, font=('Arial', 18)).grid(row=i, column=j)

def but_alias():
    alias = v1.get()
    cblist = getcb(alias)
    lab_show(cblist)

def but_update():
    print 'update'

if  __name__ == '__main__': 

    window = tk.Tk()
    window.title("upcbBox")
    #window.geometry("300x800")

    frame0 = tk.Frame(window)
    frame0.pack(padx=10, pady=10)
    
    frame1 = tk.Frame(window)
    frame1.pack(padx=10, pady=10)

    tk.Button(frame0, text="更新", font=('Arial', 16), command=but_update).grid(row=0, column=0, pady=5)
    
    #v1 = tk.StringVar(value='输入转债Alias')
    v1 = tk.StringVar()
    tk.Entry(frame0, width=15, textvariable=v1, font=('Arial', 18)).grid(row=0, column=1)
        
    tk.Button(frame0, text="查询", font=('Arial', 16), command=but_alias).grid(row=0, column=2, pady=5)

    window.mainloop()