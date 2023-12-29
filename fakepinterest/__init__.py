from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from segredos import SECRET_KEY
import os


app = Flask(__name__)
if os.getenv("DATABASE_URL"):
    link_banco = os.getenv("DATABASE_URL")
else:
    link_banco = "sqlite:///comunidade.db"
app.config["SQLALCHEMY_DATABASE_URI"] = link_banco
app.config["SECRET_KEY"] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from fakepinterest import routes