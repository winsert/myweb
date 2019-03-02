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
from cx_tk import getTK #查询所有可转债，交换债的条款
from cx_nhg import getNHG #查询逆回购数据
from cx_weather import getWeather #查询天气实况
from cx_pm import getPM #查询空气质量
from zb import getZB #查询转债市值占比
#from mhome import MHSearch #从mhome.db中查询指定i品名lab的value值
#from mhome import MHModi #按指定品名lab修改value值
#from mhome import MHAS #按指定品名lab修改value中的数量值+-
#from mhome import MHBU #对使用TinyWebDB的mhome进行备份
from web_cb import webCB #查询指定转债的基本数据
from web_cback import getCBack #用于汇总转债名称等数据，上传至cbond网络数据库，为CBond4.0服务
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

@app.route('/weather')
def weather():
    weather_msg = getWeather()
    pm_msg = getPM()
    return render_template("weather.html", weather_list = weather_msg, pm_list = pm_msg)

@app.route('/mhSearch', methods = ['GET'])
def mhSerach():
    if request.method == "GET":
        print 'Search value : ',
        lab = request.args.get('lab')
        #print lab
        value = MHSearch(lab)
        print value
        print
        return value

@app.route('/mhModi', methods = ['GET'])
def mhModi():
    if request.method == "GET":
        print "Modi value : "
        lab = request.args.get('lab')
        print 'lab = ', lab
        value = MHModi(lab)
        print value
        print
        return value

@app.route('/mhAS', methods = ['GET'])
def mhAS():
    if request.method == "GET":
        print "Add/Subtract : "
        lab = request.args.get('lab')
        print 'lab = ', lab
        value = MHAS(lab)
        print value
        print
        return value

@app.route('/mhBackUp', methods = ['GET'])
def mhBackUp():
    if request.method == "GET":
        print "BackUp to mhome0.db "
        lab = request.args.get('lab')
        print 'lab = ', lab
        tmp = open('mhome.txt', mode='w')
        tmp.write(lab)
        tmp.close

        #value = MHABU(lab)
        #print value
        #print
        return lab

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