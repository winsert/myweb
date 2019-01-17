#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于"管家婆"

__author__ = 'winsert@163.com'

import sqlite3

# 用于修改+-库存中数量值
def MHAS(lab):
    print lab
    lab_list = lab.split(',')
    warehouse = lab_list[0].decode('utf-8')
    product = lab_list[1].decode('utf-8')
    num = int(lab_list[2].decode('utf-8'))

    if num > 0:
        msg1 = u" 新增入库"
    else:
        msg1 = u" 已经出库"
    print warehouse
    print product
    print num

    try:
        conn = sqlite3.connect('mhome.db')
        curs = conn.cursor()
        sql = "select value from mhome where lab = '%s'" %warehouse
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()

        print tmp
        tmp_list1 = tmp[0][0].split('|')
        print tmp_list1

        for i in tmp_list1:
            print i
            if i.split(',')[0] == product:
                tmp_list2 = i.split(',')
        
                print tmp_list2
                if int(tmp_list2[4]) > 1:
                    tmp_list2[4] =  str(int(tmp_list2[4]) + num)
                    print tmp_list2
                    tmp_list1[tmp_list1.index(i)] = ','.join(tmp_list2)
                    msg = msg1 + u"1件！ 库余 " + tmp_list2[4] + u"件！"
                else:
                    print tmp_list1
                    print i
                    tmp_list1.remove(i)
                    msg = u" 全部" + msg1 + "!"
        print tmp_list1
        
        value = '|'.join(tmp_list1)
        print value

        conn = sqlite3.connect('mhome.db')
        curs = conn.cursor()
        sql = "UPDATE mhome SET value = '%s' WHERE lab = '%s'" % (value, warehouse)
        curs.execute(sql)
        conn.commit()
        curs.close()
        conn.close()

        return product + msg
    except Exception, e:
        print e
        return e

# 用于新建入库存数据
def MHModi(lab):
    print lab
    lab_list = lab.split(',')
    warehouse = lab_list[0].decode('utf-8')
    product = lab_list[1].decode('utf-8')
    num = lab_list[5].decode('utf-8')
    print warehouse
    print product
    lab_list = lab_list[1:]
    lab = ','.join(lab_list).decode('utf-8')
    print lab

    try:
        conn = sqlite3.connect('mhome.db')
        curs = conn.cursor()
        sql = "select value from mhome where lab = '%s'" %warehouse
        curs.execute(sql)
        tmp = curs.fetchall()
        curs.close()
        conn.close()
        
        print tmp

        value = ''
        if tmp[0][0] == '':
            value = lab
            conn = sqlite3.connect('mhome.db')
            curs = conn.cursor()
            sql = "UPDATE mhome SET value = '%s' WHERE lab = '%s'" % (value, warehouse)
            curs.execute(sql)
            conn.commit()
            curs.close()
            conn.close()
            msg = product + num + u"件，已经入库：" + warehouse
        else:
            tmp_list1 = tmp[0][0].split('|')
            #print tmp_list1

            tmp_list2 = []
            for i in tmp_list1:
                tmp_list2.append(i.split(','))
            print tmp_list2

            tmp_list3 = []
            for j in tmp_list2:
                tmp_list3.append(j[0])
            print tmp_list3

            if product in tmp_list3:
                print product, " in tmp_list3:", tmp_list3.index(product)
                msg = product + u" 已存在！不能入库：" + warehouse
            else:
                value = tmp[0][0] + '|' + lab
                print value

                conn = sqlite3.connect('mhome.db')
                curs = conn.cursor()
                sql = "UPDATE mhome SET value = '%s' WHERE lab = '%s'" % (value, warehouse)
                curs.execute(sql)
                conn.commit()
                curs.close()
                conn.close()
                msg = product + num + u"件，已经入库：" + warehouse
        
        return msg

    except Exception, e:
        print e
        return e

# 用于查询
def MHSearch(lab):
    cx = lab
    value = ''
    try:
        conn = sqlite3.connect('mhome.db')
        curs = conn.cursor()
        sql = "select value from mhome where lab = '%s'" %cx
        curs.execute(sql)
        tmp = curs.fetchone()
        curs.close()
        conn.close()

        value = tmp[0]
        #print value

        return value

    except Exception, e:
        print e
        return e

if __name__ == '__main__':
    
    while 1:
        lab = raw_input('输入LAB：')
        #print MHSearch(lab)
        #print MHModi(lab)
        print MHAS(lab)
        print