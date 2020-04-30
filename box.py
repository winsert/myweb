#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于自选转债
__author__ = 'winsert@163.com'

import Tkinter as tk
import sys, sqlite3, time
reload(sys)
sys.setdefaultencoding("utf-8")

from cbond.sina import getZZ #获取转债的价格数据
from cbond.sina import getZG #获取正股的价格数据

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

        name = tmp[0][3] #转债名称
        cblist.append(name)
        
        zz_code = tmp[0][7]+tmp[0][5] #前缀+转债代码
        cblist.append(zz_code)
        cblist.append(0.0) #＋最新价
        cblist.append(0.0) #＋涨跌幅

        zg_code = tmp[0][7]+tmp[0][6] #前缀+正股代码
        cblist.append(zg_code)
        cblist.append(0.0) #＋最新价
        cblist.append(0.0) #＋涨跌幅

        zgj = tmp[0][17] #转股价
        cblist.append(zgj)
        cblist.append(0.0) #＋溢价率

        #print cblist
        cblists.append(cblist)
    
    words = ['名称', '转债代码', '最新价', '涨跌幅', '正股代码', '正股价', '涨跌幅', '转股价', '溢价率']
    cblists.insert(0, words)
    #print cblists
    return cblists

def uplist(cblists):
    for cblist in cblists:
        zz = getZZ(cblist[1]) #获取转债的交易价格数据
        cblist[2] = zz[2] #转债最新成交价
        cblist[3] = zz[5] #涨跌幅
        zg = getZG(cblist[4]) #获取正股的交易价格数据
        cblist[5] = zg[2] #正股最新成交价
        cblist[6] = zg[5] #涨跌幅
        zgjz = (100/cblist[7])*zg[2] #转股价值
        yjl = round((zz[2]/zgjz - 1) * 100, 2)
        cblist[8] = yjl

    words = ['名称', '转债代码', '最新价', '涨跌幅', '正股代码', '正股价', '涨跌幅', '转股价', '溢价率']
    cblists.insert(0, words)
    return cblists

if  __name__ == '__main__': 

    #自选转债
    cbs = [127015, 128092, 123025, 110056, 110031, 128029, 128045, 127011]

    #得到自选转债完整数据
    cblists = getCBlists(cbs)
    
    window = tk.Tk()
    window.title("cbBox")
    window.geometry("700x400")

    while 1:
        print time.asctime(time.localtime(time.time())) #显示查询时间

        #grid 放置方法
        for i in range(len(cblists)):
           for j in range(9):
                #tk.Label(window, text=cblists[i][j], font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
                if i>0 and j==3 and (cblists[i][3] > 3.0 or cblists[i][3] < -3.0):
                    tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
                elif i>0 and j==6 and (cblists[i][6] > 3.0 or cblists[i][6] < -3.0):
                    tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
                elif i>0 and j==8 and cblists[i][8] < 0.0:
                    tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
                else:
                    tk.Label(window, text=cblists[i][j], bg='white', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)

        cblists.pop(0)
        cblists = uplist(cblists)
        window.update()
        time.sleep(30)  # 延时查询的秒数,120即延时2分钟查询一次。
    window.mainloop()