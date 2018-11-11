from app import app
from flask import render_template, flash, url_for
from flask import redirect

from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",active1="active")

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',active4="active", title='Регистрация', form=form)

@app.route('/about')
def about():
    return render_template("about_me.html",active3="active", title='Об авторе')