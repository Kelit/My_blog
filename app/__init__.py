from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Flask server
app = Flask(__name__)
app.config.from_object(Config)
# For file BD
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# For LoginManager
login = LoginManager(app)
login.login_view = 'login_p'

from app import views, models