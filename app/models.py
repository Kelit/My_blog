from app import db
from app import login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

class User(UserMixin,db.Model): #USer
    id = db.Column(db.Integer,  primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.column(db.String(140))
    slug = db.column(db.String(140))
    body = db.Column(db.Text)
    created = db.column(db.DateTime)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
