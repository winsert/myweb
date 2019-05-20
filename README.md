# myweb

run.py      #web页面的主程序

adjust.py   #用于修改转债信息

an.py       #用微信发送三线、高价折扣通知

dayScat.py  #用于画转债溢价率的散点图
daysBP.py   #用于画转债成交量的直方图
daysRate.py #用于画牛熊转换指标图

dd.py       #用于记录转债日成交信息

exchange.py #用于记录转债的交易数据

jisilu.py   #用于从集思录下载转债信息

cb.db       #记录转债信息的数据库
dd.db       #记录转债日成交信息的数据库

SendMail.py #用邮件发送三线、高价折扣通知

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

    web_3line.py    #支持APP(CBond),用于查询满足三线条件的转债

    web_arrange.py  #支持APP(CBond),用于更新转债每日最高最低价

    web_cback.py    #支持APP(CBond),用于向公网数据库提供数据同步服务

    web_cb          #支持APP(CBond),用于查询可转债信息

    web_hp.py       #支持APP(CBond),用于查询满足高价折扣的转债

	web_weather.py	#用于APP查询济南市多地实时天气信息

    wxcx.py         #用于查询转债信息

    wxex.py         #用于查询交债信息

    zb.py           #用于转债值占比分析

static/             #用于保存静态文件

common              #用于保存通用功能模块

    price.py        #用于从http://hq.sinajs.cn/list=获取最新成交价格

    sendmail.py     #邮件发送模块

cond/               #用于保存转债相关的模块

    cxcb.py         #三线查询模块

    cxhp.py         #高价折扣查询模块

    cxindex.py      #指数查询模块

    cxqs.py         #强赎查询模块


templates/
    index.html

    base.html

    cb.html         #显示全部可转债、交换债数据的页面

    mobile.html     #移动端显示三线数据

    tk.html         #显示全部可转债、交换债条款查询结果的页面

    weather.html    #显示天气实况信息

    zb.html         #显示转债市值占比分析的页面
