from app import app, db
from flask import render_template, flash, url_for
from flask import redirect,request
from flask_login import current_user, login_user, logout_user
from flask_login import login_required

from app.models import User
from app.forms import LoginForm
from werkzeug.urls import url_parse
from app.forms import RegistrationForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", active1="active",)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return  redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляем вы зарегистрированы!')
        return redirect(url_for('login_p'))
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_p():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Не правильный логин или пароль')
            return redirect(url_for('login_p'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # check whether the path is relative or not
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', active5="active", title='Регистрация', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login_p'))


@app.route('/about')
@login_required
def about():
    return render_template("about_me.html",active3="active", title='Об авторе')

