# -*- coding:utf-8 -*-
__author__ = '504'
__date__ = '2017/8/7 15:03'

from flask  import Blueprint

home = Blueprint("home",__name__)

import app.home.views
