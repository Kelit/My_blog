from app import app, db
from app.models import User, Post
from posts.blueprint import posts

# blueprint app
app.register_blueprint(posts, url_prefix='/posts')
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

# if __name__ == '__main__':
#     app.run(Debug=True)
