#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 获取可转债最新价，进行"三线"和"高价折扣法"分析，并通过邮件通知

__author__ = 'winsert@163.com'

import time
from sys import exit
from datetime import datetime

from cbond.cxcb import getCB #查询可转债,可交换债是否满足三线的模块
from cbond.cxhp import getHP #高价折扣模块
from common.sendmail import sendMail #邮件发送模块

if __name__ == '__main__':

    sysMsg = u'系统开始运行！'
    startMsg = u'开始查询！'
    newPriceMsg =  u"没有可转债满足 买入条件。"
    HPriceMsg =  u"没有可转债满足 高价折扣法。"

    now_time = datetime.now()
    today_year = now_time.year
    today_month = now_time.month
    today_day = now_time.day
    #print today_year, today_month, today_day

    start_time = datetime(today_year, today_month, today_day, 9, 29, 59) # 设定开始时间9:29:59。
    end_time = datetime(today_year, today_month, today_day, 14, 59, 59) # 设定结束时间到当天的14:59:59。
    #print end_time

    print sysMsg
    print
    sendMail(sysMsg, sysMsg, sysMsg) #系统开始运行，发送邮件通知

    while datetime.now() < end_time: 
    
        if datetime.now() > start_time and datetime.now() < end_time:

            print time.asctime(time.localtime(time.time())) #显示查询时间

            # 三线分析：
            msglist = getCB() #查询是否有CB满足三线买入条件
            if len(msglist) == 0: #没有满足条件的CB
                print newPriceMsg
            else:    
                for subject in msglist: #有满足条件的CB
                    print subject
                    mailtime = time.asctime(time.localtime(time.time()))
                    mailmsg = "SendMailTime：" + str(mailtime)
                    print
                    sendMail('3Line', subject, mailmsg)

            # 高价折扣法分析
            HPlist = getHP() #查询是否CB满足高价折扣法
            if len(HPlist) == 0: #没有满足高价折扣法的CB
                print HPriceMsg
                print
            else:
                for subject in HPlist: #有满足高价折扣法的CB
                    print subject
                    mailtime = time.asctime(time.localtime(time.time()))
                    mailmsg = "SendMailTime：" + str(mailtime)
                    print
                    sendMail('H.P.', subject, mailmsg)
        
        time.sleep(60)  # 延时查询的秒数,300即延时5分钟查询一次。
    exit()