#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

__author__ = 'winsert@163.com'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from app import app
#app.run(host='0.0.0.0', debug=True, port=5000)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
