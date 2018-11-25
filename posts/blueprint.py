from flask import Blueprint
from flask import render_template
from app.models import Post, Tag
from flask_login import login_required

posts = Blueprint('posts',__name__,template_folder='templates')


@posts.route('/')
@login_required
def index():
    posts = Post.query.all()
    return render_template('posts/list.html', posts=posts)

# /blog/post
@posts.route('/<slug>')
@login_required
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)

#/blog/tag/code
@posts.route('/tag/<slug>')
@login_required
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)