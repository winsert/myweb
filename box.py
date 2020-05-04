#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序通过tk模块显示指定转债的信息
__author__ = 'winsert@163.com'

import Tkinter as tk
import sys, sqlite3
reload(sys)
sys.setdefaultencoding("utf-8")

from cbond.sina import getZZ #获取转债的价格数据
from cbond.sina import getZG #获取正股的价格数据
from dqjz import getSYNX #计算转债剩余年限
from dqjz import getDQJZ #计算转债到期价值

#查询转债信息
def getCBlists(cbs):
    cblists = []
    for cb in cbs:
        cblist = []
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select * from cb where zzcode = '%s'" %cb
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()

        dqr = tmp[0][19] #到期日
        synx = getSYNX(dqr) #计算剩余年限
        cblist.append(str(synx))
        shj = tmp[0][20] #赎回价
        ll = tmp[0][24] #每年的利率
        dqjz = getDQJZ(synx, shj, ll) #计算到期价值
        cblist.append(str(dqjz))
        
        name = tmp[0][3] #转债名称
        cblist.append(name)

        zz_code = tmp[0][7]+tmp[0][5] #前缀+转债代码
        zz = getZZ(zz_code) #获取转债的交易价格数据
        cblist.append(zz[2]) #＋转债最新价
        cblist.append(zz[5]) #＋转债涨跌幅

        zg_code = tmp[0][7]+tmp[0][6] #前缀+正股代码
        zg = getZG(zg_code) #获取正股的交易价格数据
        cblist.append(zg[2]) #＋正股最新价
        cblist.append(zg[5]) #＋正股涨跌幅

        zgj = tmp[0][17] #转股价
        cblist.append(round(zgj*1.3, 2)) #+强赎价
        zgjz = (100/zgj)*zg[2] #转股价值
        yjl = round((zz[2]/zgjz - 1) * 100, 2)
        cblist.append(yjl) #＋溢价率

        #print cblist
        cblists.append(cblist)
    
    words = ['年限', '到期价值', '名称', '最新价', '涨跌幅', '正股价', '涨跌幅', '强赎价', '溢价率']
    cblists.insert(0, words)
    #print cblists
    return cblists

#用于grid 放置方法显示转债信息
def show(cblists):
    
    for i in range(len(cblists)):
        for j in range(9):
            if i>0 and j==4 and (cblists[i][4] > 3.0 or cblists[i][4] < -3.0):
                tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
            elif i>0 and j==6 and (cblists[i][6] > 3.0 or cblists[i][6] < -3.0):
                tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
            elif i>0 and j==8 and cblists[i][8] < 0.0:
                tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
            else:
                tk.Label(window, text=cblists[i][j], bg='white', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)

def ex():
    sys.exit()
    print 'ok'

if  __name__ == '__main__': 

    #自选转债
    cbs = [127015, 128092, 123025, 110056, 110031, 128029, 128045, 127011]

    #得到自选转债完整数据
    cblists = getCBlists(cbs)

    window = tk.Tk()
    window.title("cbBox")
    window.geometry("700x400")

    show(cblists) #用于grid 放置方法显示转债信息
    
    window.mainloop()