#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于获取可转债、可交换债的条款等数据

__author__ = 'winsert@163.com'

import sqlite3

# 主程序
def getTK():
    
    ccList = []

    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        sql = "select name, Code, zgqsr, zgj, hsqsr, hsj, dqr, shj, zgjxt, qzsh, hs from cb ORDER BY Code"
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        #print tmp

        for cc in tmp:
            cList = []
            if cc[3] != 'QS':
                name = cc[0] #名称
                cList.append(name)
                code = cc[1] #代码
                cList.append(code)
                zgqsr = cc[2] #转股起始日
                cList.append(zgqsr)
                zgj = cc[3] #转股价
                cList.append(zgj)
                hsqsr = cc[4] #回售起始日
                cList.append(hsqsr)
                hsj = cc[5] #回售价
                cList.append(hsj)
                dqr = cc[6] #到期日
                cList.append(dqr)
                shj = cc[7] #赎回价
                cList.append(shj)
                zgjxt = cc[8] #转股价下调条款
                cList.append(zgjxt)
                qzsh = cc[9] #强制赎回条款
                cList.append(qzsh)
                hs = cc[10] #回售条款
                cList.append(hs)
                ccList.append(cList)

        #print ccList
        return ccList

    except Exception, e :
        ccList.append(e)
        return ccList

if __name__ == '__main__':
    tk = getTK()
    print tk
