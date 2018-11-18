from flask import Blueprint
from flask import render_template

from app.models import Post

posts = Blueprint('posts',__name__,template_folder='templates')

@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/list.html', posts=posts)