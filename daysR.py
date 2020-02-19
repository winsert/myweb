#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于查询每日收盘价超过到期价值的转债占比,并画出折线图

__author__ = 'winsert@163.com'

import sqlite3, urllib2, datetime
import matplotlib.pyplot as plt

# 生成今天日期
def getToday():
    now_time = datetime.datetime.now()
    year = str(now_time.year)
    month = now_time.month
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    day = now_time.day
    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)

    today = year+month+day
    #print today
    return today

def getRate(ndays):

    zb_lists = []

    try:
        conn = sqlite3.connect('dd.db')
        curs = conn.cursor()
        sql = "select date, csum, vsum from cbt ORDER BY date ASC"  #date日期，csum当天转债总数，vsum当天大于到期价值转债的数量，按正序查询
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        #print tmp    
            
        for cb in tmp[-ndays:]:
            zb_list = []
            #print cb[0], cb[1], cb[2],
            rate = round((float(cb[2])/float(cb[1])), 4) * 100
            #print rate
            print cb[0]+u'：共有 '+cb[1]+u' 只转债，其中 '+cb[2]+u' 只转债的收盘价 > 到期价值，占比：'+str(rate)+'%'

            zb_list.append(cb[0])
            zb_list.append(rate)
            zb_lists.append(zb_list)

        #print zb_lists
        return zb_lists

    except Exception, e:
        print 'getRate()', e

#画折线图
def getLine(zb_lists):
    n = len(zb_lists) #用于设定X,Y轴
    x = [] #日期
    y = [] #占比
    z = [] #60线
    
    x = list(range(0,n))
    
    for i in range(n):
        y.append(float(zb_lists[i][1]))
        z.append(60)
    #print z

    plt.title(str(n)+u" 天牛熊转换指标")
    plt.plot(x, y, linewidth=3, color='b')
    plt.scatter(x, z, s=3, edgecolor='none' ,color='r')
    plt.xlabel('Days')
    plt.ylabel('RATE')
    plt.axis([0,120,0,100]) #设置x,y轴的取值范围
    plt.show()

if __name__ == '__main__':
    
    ndays = 120 #查询Ｎ天前的数据

    today = getToday() #生成今天日期
    print u"\n今天是：" + today + "\n"
    print u"即将开始查询自 " + today + u" 起倒数 " + str(ndays) + u" 天的数据......\n"

    zb_lists = getRate(ndays) #计算收盘价>到期价值的转债占所有转债的比例
    #print zb_lists
    print u"\n显示 "+str(len(zb_lists))+u" 天牛熊转换指标。\n"

    getLine(zb_lists) #画折线图