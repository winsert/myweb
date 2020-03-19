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
from qcx_cx import getQCX #查询所有可转债数据
from qcx_ex import getQEX #查询所有交换债数据
from mcx_cx import getMCX #mobile查询可转债数据
from mcx_ex import getMEX #mobile查询交换债数据
from wxcx import getWXCX #WX查询可转债数据
from wxex import getWXEX #WX查询交换债数据
from wxdqjz import WXDQJZ #查询最新价<到期价值(重仓价>80)的转债
from wxdqjz0 import WXDQJZ0 #查询最新价<到期价值(建仓价>80)的转债
from jian_4 import JIAN_4 #当前价>建仓价 and <＝建仓价＋4.0元的可转债
from cx_tk import getTK #查询所有可转债，交换债的条款
from cx_nhg import getNHG #查询逆回购数据
from cx_weather import getWeather #查询天气实况
from cx_pm import getPM #查询空气质量
from zb import getZB #查询转债市值占比
from web_cb import webCB #查询指定转债的基本数据
from web_cback import getCBack #用于汇总转债名称等数据，上传至cbond网络数据库，为CBond5.0服务
from web_cback6 import getCBack6 #用于汇总转债名称等数据，上传至cbond网络数据库，为CBond6.x服务
from web_hp import getHP #检查高价折扣法的模块
from web_3line import get3line #检查三线条件的模块
from web_arrange import getArrange #整理所有转债的最高最低价

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

@app.route('/zb')
def zb():
    zb, sztotal, dqtotal, diff = getZB()
    return render_template("zb.html", zb_list=zb, sztotal=sztotal, dqtotal=dqtotal, diff=diff)

@app.route('/cb')
def cb():
    qcx = getQCX()
    qex = getQEX()
    return render_template("cb.html", cx=qcx, ex=qex)

@app.route('/tk')
def tk():
    tk = getTK()
    return render_template("tk.html", tk_list=tk)

@app.route('/mobile')
def mobi():
    cpu = get_cpu_temp()
    index_list = getIndex()
    mcx = getMCX()
    mex = getMEX()
    return render_template("mobile.html", cpu =cpu, index_list=index_list, cx=mcx, ex=mex)

@app.route('/weixin')
def weixin():
    wxcx_list = getWXCX()
    wxex_list = getWXEX()
    return render_template("weixin.html", wxcx=wxcx_list, wxex=wxex_list)

@app.route('/dqjz')
def dqjz():
    dqjz_list = WXDQJZ()
    return render_template("dqjz.html", wxdqjz=dqjz_list)

@app.route('/dqjz0')
def dqjz0():
    dqjz_list0 = WXDQJZ0()
    return render_template("dqjz0.html", wxdqjz0=dqjz_list0)

@app.route('/jian_4')
def jian_4():
    jian_4_list = JIAN_4()
    return render_template("jian_4.html", jian_4=jian_4_list)

@app.route('/weather')
def weather():
    weather_msg = getWeather()
    pm_msg = getPM()
    return render_template("weather.html", weather_list = weather_msg, pm_list = pm_msg)

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

@app.route('/webCBack', methods = ['GET'])
def webCBack():
    if request.method == "GET":
        value = getCBack()
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

@app.route('/webHP', methods = ['GET'])
def webHP():
    if request.method == "GET":
        value = getHP()
        print value
        print
        return value

@app.route('/web3line', methods = ['GET'])
def web3line():
    if request.method == "GET":
        value = get3line()
        print value
        print
        return value

@app.route('/webArrange', methods = ['GET'])
def webArrange():
    if request.method == "GET":
        value = getArrange()
        print value
        print
        return value