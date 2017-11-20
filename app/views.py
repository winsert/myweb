#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template
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
from cx_tk import getTK #查询所有可转债，交换债的条款
from cx_nhg import getNHG #查询逆回购数据
from cx_weather import getWeather #查询天气实况
from cx_pm import getPM #查询空气质量
from zb import getZB #查询转债市值占比

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
    zb = getZB()
    return render_template("zb.html", zb_list=zb)

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
    index_list = getIndex()
    mcx = getMCX()
    mex = getMEX()
    return render_template("mobile.html", index_list=index_list, cx=mcx, ex=mex)

@app.route('/weather')
def weather():
    weather_msg = getWeather()
    pm_msg = getPM()
    return render_template("weather.html", weather_list = weather_msg, pm_list = pm_msg)
