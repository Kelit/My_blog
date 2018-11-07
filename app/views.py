from app import app
from flask import render_template, flash, url_for
from flask import redirect

from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login_user():
    form = LoginForm
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)