# -*- coding:utf-8 -*-
__author__ = '504'
__date__ = '2017/8/7 15:03'

from flask import Blueprint

admin  = Blueprint("admin",__name__)

import app.admin.views
