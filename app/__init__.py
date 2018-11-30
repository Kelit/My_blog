from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



# Flask server
app = Flask(__name__)
app.config.from_object(Config)
# For file BD
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# For LoginManager
login = LoginManager(app)
login.login_view = 'login_p'

# admin with flask_admin
from app.models import *
admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Tag, db.session))
admin.add_view(ModelView(Post, db.session))

from app import views, models