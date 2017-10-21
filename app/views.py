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

@app.route('/')
@app.route('/index')
def index():
    cpu = get_cpu_temp()
    index_list = getIndex()
    jj = getJJ()
    wh = getWH()
    sp = getSP()
    cx = getCX()
    ex = getEX()
    return render_template("index.html", cpu=cpu, index_list=index_list, jj=jj, wh_list=wh, sp_list=sp, cx=cx, ex=ex)

@app.route('/cb')
def cb():
    qcx = getQCX()
    qex = getQEX()
    return render_template("cb.html", cx=qcx, ex=qex)
