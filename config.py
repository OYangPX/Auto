#encoding:utf-8

import os

#激活跨站点请求伪造保护
CSRF_ENABLED = True
#CSRF激活 加密令牌
SECRET_KEY= 'alkdmflkasdmlgfmas878askdnfkASF'

#第三方登录
# OPENID_PROVIDERS = [
#     { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
#     { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#     { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#     { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#     { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

base_url = os.path.abspath(os.path.dirname(__file__))

#数据库路径
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.10.140/test?charset=utf8'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxxxx@localhost:3306/test?charset=utf8'
#数据文件存储
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')