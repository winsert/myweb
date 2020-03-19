#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于画出每日可交易转债成交金额的折线图

__author__ = 'winsert@163.com'

import sqlite3, random, datetime
import numpy as np
import matplotlib.pyplot as plt
#from datetime import datetime

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

# 生成开始日期
def getDate(N):
    n = N * -1
    now_time = datetime.datetime.now()
    start_time = now_time + datetime.timedelta(days=n)
    year = str(start_time.year)
    month = start_time.month
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    day = start_time.day
    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)

    start_date = year+month+day
    #print start_date
    return start_date
    
# 查询n天转债的成交金额
def getCbData(n):
    cjje_list = []
    #print 'n = ', n

    try:
        conn = sqlite3.connect('dd.db')
        curs = conn.cursor()
        sql = "select date, cjje from cbt ORDER BY date ASC"  #查询成交金额
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        #print tmp
            
            
        for cb in tmp[-n:]:
            #print cb[1]
            cjje_list.append(float(cb[1]))
            
        #print cjje_list
        return cjje_list
        
    except Exception, e:
        print e

def getAVG(avg_days, cjje_list):
    '''计算N天成交金额平均数'''
    a = 0
    avg_lists = []
    while (a + avg_days) <= len(cjje_list):
        #print 'a = ', a
        cj = 0
        avg_list = []
        for i in range(a, a + avg_days):
            cj = cj + cjje_list[i]
            b = cjje_list[i]
            #print b
        avg = round((cj / avg_days), 2)
        avg_list.append(b)
        avg_list.append(avg)
        avg_lists.append(avg_list)
        a = a + 1

    print u'\n日成交金额的 ' + str(avg_days) + u' 日平均数：'
    print avg_lists
    return avg_lists

#画折线图
def getBP(cjje_list, avg_lists, date_txt):
    n = len(cjje_list) #用于设定X轴
    #print u"\n将显示 " + str(n) + u" 天的查询结果......"
    x = [] #日期
    y1 = [] #日成交金额
    y2 = [] #平均成交金额

    for i in range(n):
        #x.append(round((float(i[0]) / 10), 2))
        x.append(i+1)
        y1.append(float(cjje_list[i]))
        #y.append(float(i[1]))
    
    for i in range(n):
        y2.append(float(avg_lists[i][1]))
    
    plt.figure(figsize=(16, 8))
    #plt.title(date_txt)
    plt.title(u'转债市场日成交总金额统计')
    plt.bar(x, y1)
    plt.plot(x, y2, linewidth=3, color='r')
    #plt.plot(x, y2, linewidth=5, color='r', marker='o', markerfacecolor='blue', markersize=5)
    
    plt.xlim(0, 42)
    plt.xlabel('DATE')
    plt.xticks(())  # ignore xticks
    plt.ylabel('AMO')
    plt.ylim(0, 900)
    #plt.yticks(())  # ignore yticks

    # 设置数字标签
    for a, b in zip(x, y1):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=20)

    plt.show()
    

if __name__ == '__main__':
    
    avg_days = 20 #计算avg_days天的平均数据
    N = 40 #查询Ｎ天前的数据
    days = avg_days + N #查询倒数N+avg_days天的数据

    today = getToday() #生成今天日期
    print u"\n今天是：" + today + "\n"
    print u"即将开始查询自 " + today + u" 起倒数 " + str(days) + u" 天的成交数据，并计算 " + str(avg_days) + u" 天的平均成交金额：\n"
    
    start_date = getDate(N)
    
    cjje_list = getCbData(days) #查询days天的成交金额
    
    avg_lists = getAVG(avg_days, cjje_list) #计算平均值
    
    cjje_list = cjje_list[(avg_days - 1):]
    print u'\n将显示以下 ' + str(len(cjje_list))+ u' 天数据：'
    print cjje_list
    
    date_txt = start_date + " --- " + today
    #print date_txt

    getBP(cjje_list, avg_lists, date_txt) #画折线图，X轴日期，Y轴成交金额
    
    print u"\n结束查询！"
