from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.models import Post, Tag
from flask_login import login_required
from .forms import PostForm
from app import db

posts = Blueprint('posts', __name__, template_folder='templates')

#blog/create
@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Что-то не так')

        return redirect(url_for('posts.index'))
    form = PostForm()
    return render_template('posts/create_post.html', form=form)

#blog/create
@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        #populate_obj заполняет аттрибуты переденного объекта, title и body
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit.html', post=post, form=form)

@posts.route('/')
@login_required
def index():
    active7 = True
    q = request.args.get('q')

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page=1

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))#.all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=3)

    return render_template('posts/list.html', active7=active7, pages=pages)

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