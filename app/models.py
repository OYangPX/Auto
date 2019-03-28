#encoding:utf-8

from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(25),unique = True,nullable=False)
    password = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),unique =True,nullable=False)
    is_admin = db.Column(db.Boolean,default = False,nullable=False)
    create_time = db.Column(db.DateTime,nullable=False)
    create_author = db.Column(db.String(20),default='sys',nullable=False)
    update_time = db.Column(db.DateTime,nullable=False)
    update_author = db.Column(db.String(20),default='sys',nullable=False)

    def __repr__(self):
        return '<User %r >' % (self.name)

