#encoding:utf-8
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .models import User
from flask_login import LoginManager  
from flask_login import login_user, login_required  

@app.route('/index')
def index():
    user ={'lonel':'ioan'}
    return render_template('index.html',title='home',user=user)
    #return 'flask Web framework'

@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=='POST':
        if not form.validate_on_submit():
            print(form.errors)
            return render_template('login.html',form=form)

        user = User.query.filter(User.name == form.name.data,User.password == form.password.data).first()
        if user:
            login_user(user)
            return render_template('index.html')

    return  render_template('login.html',form=form)
    
