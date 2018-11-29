from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class PostForm(FlaskForm):
    title = StringField('Заголовок')
    body = TextAreaField('Текст')

