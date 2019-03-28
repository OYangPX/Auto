#encoding: utf-8

from flask import Flask
#from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)

app.config.from_object('config')


#配置flask配置对象中键：SQLALCHEMY_DATABASE_URI
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:123456@192.16.10.140/test"
#配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动
SQLALCHEMY_COMMIT_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True


#获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy(app)

from app import views,models

