# -*- coding:utf-8 -*-
__author__ = '504'
__date__ = '2017/8/7 14:59'

from flask_redis import FlaskRedis
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import  os
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "76f6027d7f02494bbf87575d99d3f1c3"
app.config["REDIS_URL"] = "redis://localhost:6379/0"
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/users/")
db = SQLAlchemy(app)
rd = FlaskRedis(app)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin  as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"),404