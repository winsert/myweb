#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template, request
from app import app
from cx_cpu import get_cpu_temp #查询CPU温度
from cx_index import getIndex #查询证券指数
from cx_jj import getJJ #查询基金
from cx_wh import getWH #查询外汇
from cx_sp import getSP #查询商品
from cx_cx import getCX #查询可转债数据
from cx_ex import getEX #查询交换债数据
from mcx_cx import getMCX #mobile查询可转债数据
from wxcx import getWXCX #WX查询可转债数据
from wxdqjz import WXDQJZ #查询最新价<到期价值(重仓价>80)的转债
from jian_4 import JIAN_4 #当前价>建仓价 and <＝建仓价＋4.0元的可转债
from cx_nhg import getNHG #查询逆回购数据
from web_cb import webCB #查询指定转债的基本数据
from web_cback6 import getCBack6 #用于汇总转债名称等数据，上传至cbond网络数据库，为CBond6.x服务

@app.route('/')
@app.route('/index')
def index():
    cpu = get_cpu_temp()
    index_list = getIndex()
    nhg = getNHG()
    jj = getJJ()
    wh = getWH()
    sp = getSP()
    cx = getCX()
    ex = getEX()
    return render_template("index.html", cpu=cpu, index_list=index_list, nhg_list=nhg, jj=jj, wh_list=wh, sp_list=sp, cx=cx, ex=ex)

@app.route('/mobile')
def mobi():
    cpu = get_cpu_temp()
    index_list = getIndex()
    mcx = getMCX()
    return render_template("mobile.html", cpu =cpu, index_list=index_list, cx=mcx)

@app.route('/weixin')
def weixin():
    wxcx_list = getWXCX()
    #wxex_list = getWXEX()
    return render_template("weixin.html", wxcx=wxcx_list)

@app.route('/dqjz')
def dqjz():
    dqjz_list = WXDQJZ()
    return render_template("dqjz.html", wxdqjz=dqjz_list)

@app.route('/jian_4')
def jian_4():
    jian_4_list = JIAN_4()
    return render_template("jian_4.html", jian_4=jian_4_list)

@app.route('/webCBCX', methods = ['GET'])
def webCBCX():
    if request.method == "GET":
        print "Get CB msg : "
        lab = request.args.get('lab')
        print lab
        value = webCB(lab)
        print value
        print
        return value

@app.route('/webCBack6', methods = ['GET'])
def webCBack6():
    if request.method == "GET":
        value = getCBack6()
        print value
        print
        return value