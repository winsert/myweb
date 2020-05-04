#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序通过tk模块显示满足三线、复式的转债信息
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
def getCBlists():
    cblists = []
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select * from cb where code>1"
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        #print tmp

        for cb in tmp:
            cblist = []
            code = cb[2] #特征码            

            zz_code = cb[7]+cb[5] #前缀+转债代码
            zz = getZZ(zz_code) #获取转债的交易价格数据
            zz_price = float(zz[2])
            zz_zdf = float(zz[5])

            jian = cb[12] #建仓价
            #print cb[3], zz_price, jian

            #转债现价<=建仓价 or (>=130.0 and 持仓(特征码＝3)>0)
            if zz_price <= jian or (zz_price >=130.0 and code == 3):
                dqr = cb[19] #到期日
                synx = getSYNX(dqr) #计算剩余年限
                shj = cb[20] #赎回价
                ll = cb[24] #每年的利率
                dqjz = getDQJZ(synx, shj, ll) #计算到期价值
                dqsyl = round((dqjz/zz_price - 1) * 100, 2) #计算到期收益率
                dqnh = round(dqsyl/synx, 2) #计算到期年化收益率
                cblist.append(dqnh) #+年化收益率
                cblist.append(synx) #+剩余年限
                cblist.append(dqjz) #+到期价值
        
                name = cb[3] #名称
                cblist.append(name)

                cblist.append(zz_price) #＋转债最新价
                cblist.append(zz_zdf) #＋转债最新价

                zg_code = cb[7]+cb[6] #前缀+正股代码
                zg = getZG(zg_code) #获取正股的交易价格数据
                cblist.append(zg[2]) #＋正股最新价
                cblist.append(zg[5]) #＋正股涨跌幅

                zgj = cb[17] #转股价
                cblist.append(round(zgj*1.3, 2)) #+强赎价
                zgjz = (100/zgj)*zg[2] #转股价值
                yjl = round((zz[2]/zgjz - 1) * 100, 2)
                cblist.append(yjl) #＋溢价率

                cblist.append(cb[28]) #+安全度
                cblist.append(cb[30]) #+评级

                #print cblist
                cblists.append(cblist)
        
        cblists.sort()
        words = ['年化', '年限', '到期价值', '名称', '最新价', '涨跌幅', '正股价', '涨跌幅', '强赎价', '溢价率', '安全度', '评级']
        cblists.insert(0, words)
        #print cblists
        return cblists

    except Exception, e :
        print 'getCBlists() is error!'
        print e

#用于grid 放置方法显示转债信息
def show(cblists):
    
    for i in range(len(cblists)):
        for j in range(12):
            if i>0 and j==4 and (cblists[i][4] > 130.0):
                tk.Label(window, text=cblists[i][j], fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
            elif i>0 and j==5 and (cblists[i][5] > 3.0 or cblists[i][5] < -3.0):
                tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
            elif i>0 and j==7 and (cblists[i][7] > 3.0 or cblists[i][7] < -3.0):
                tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
            elif i>0 and j==9 and cblists[i][9] < 0.0:
                tk.Label(window, text=cblists[i][j], bg='green', fg='red', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)
            else:
                tk.Label(window, text=cblists[i][j], bg='white', font=('Arial', 18)).grid(row=i, column=j, padx=3, pady=3, ipadx=3, ipady=3)

if  __name__ == '__main__': 

    print u"\n正在查询中......\n"
    #得到自选转债完整数据
    cblists = getCBlists()

    window = tk.Tk()
    window.title("DAO")
    window.geometry("930x500")

    show(cblists) #用于grid 放置方法显示转债信息
    
    window.mainloop()