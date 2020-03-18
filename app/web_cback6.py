#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于为CBond6.X提供数据服务

__author__ = 'winsert@163.com'

import sqlite3

# 主程序
def getCBack6():

    sh_list = []
    sz_list = []
    cb_list = []
    cbs_list = []
    
    try:
        conn = sqlite3.connect('cb.db')
        curs = conn.cursor()
        #sql = "select Alias, name, Prefix, Code, zgcode, position, AVG, HPrice, LPrice, jian, jia, zhong, Note, zgqsr, zgj, hsqsr, hsj, dqr, shj, ll, zgjxt, qzsh, hs, ce from cb"
        sql = "select name, Prefix, Code, zgcode, position, AVG, HPrice, LPrice, jian, jia, zhong, Note, zgqsr, zgj, hsqsr, hsj, dqr, shj, ll, zgjxt, qzsh, hs, zgdm, yjd, aqd, jp from cb0"
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()

        for cb in tmp:
            cb_list = []
            for i in cb:
                cb_list.append(i)
            cbs_list.append(cb_list)

            name = cb[0] #名称
            prefix = cb[1] #前缀
            
            if prefix == 'sh':
                sh_list.append(name)

            if prefix == 'sz':
                sz_list.append(name)

        sh = '|'.join(sh_list)
        sz = '|'.join(sz_list)
        team = sh + '#' + sz

        for cb in cbs_list:
            cc = '|'.join('%s' % id for id in cb) #将int转为str的整形处理
            team = team + '#' + cc

        return team

    except Exception, e:
        print 'CBack Error is :', e

if __name__ == '__main__':
    msgs = getCBack6()
    print msgs