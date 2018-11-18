from flask import Blueprint
from flask import render_template
from app.models import Post
from flask_login import login_required

posts = Blueprint('posts',__name__,template_folder='templates')


@posts.route('/')
@login_required
def index():
    posts = Post.query.all()
    return render_template('posts/list.html', posts=posts)


@posts.route('/<slug>')
@login_required
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('posts/post_detail.html', post=post)