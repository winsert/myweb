# myweb

run.py      #主程序

cb.db       #数据库

APP/
    __init__.py     #初始化文件

    views.py        #FLASK视图模块

    cx_cpu.py       #用于查询cpu温度

    cx_cx.py        #用于查询可转债三线数据

    cx_ex.py        #用于查询交换债本线数据

    cx_index.py     #用于查询证券指数

    cx_jj.py        #用于查询基金数据

    cx_sp.py        #用于查询商品数据

    cx_tk.py        #用于查询可转债、交换债条款

    cx_wh.py        #用于查询外汇

    qcx_cx.py       #用于查询全部可转债数据

    qcx_ex.py       #用于查询全部交换债数据

static/             #用于保存静态文件

templates/
    index.html

    base.html

    cb.html         #显示全部可转债、交换债数据的页面

    tk.html         #显示全部可转债、交换债条款查询结果的页面
