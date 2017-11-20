# myweb

run.py      #主程序

cb.db       #数据库

APP/
    __init__.py     #初始化文件

    views.py        #FLASK视图模块

    cx_cpu.py       #用于查询cpu温度

    cx_cx.py        #用于查询可转债三线数据

    cxcx.py         #查询指定转债，便于查错使用

    cx_ex.py        #用于查询交换债本线数据

    cx_index.py     #用于查询证券指数

    cx_jj.py        #用于查询基金数据

    cx_nhg.py       #用于查询逆回购数据

    cx_pm.py         #用于查询PM数据

    cx_sp.py        #用于查询商品数据

    cx_tk.py        #用于查询可转债、交换债条款

    cx_weather.py   #用于查询天气实况

    cx_wh.py        #用于查询外汇

    mcx_cx.py       #用于mobile.html页面显示转债三线数据

    mcx_ex.py       #用于mobile.html页面显示交换债三线数据

    qcx_cx.py       #用于查询全部可转债数据

    qcx_ex.py       #用于查询全部交换债数据

    zb.py           #用于转债值占比分析

static/             #用于保存静态文件

templates/
    index.html

    base.html

    cb.html         #显示全部可转债、交换债数据的页面

    mobile.html     #移动端显示三线数据

    tk.html         #显示全部可转债、交换债条款查询结果的页面

    weather.html    #显示天气实况信息

    zb.html         #显示转债市值占比分析的页面
