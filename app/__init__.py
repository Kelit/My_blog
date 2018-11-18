from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

from posts.blueprint import posts

# Flask server
app = Flask(__name__)
app.config.from_object(Config)
# For file BD
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# For LoginManager
login = LoginManager(app)
login.login_view = 'login_p'

# blueprint app
app.register_blueprint(posts, url_prefix='/posts')

from app import views, models