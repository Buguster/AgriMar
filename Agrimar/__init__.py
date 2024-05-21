from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '092b93416967f9fec0c22c76420ed834'
app.app_context()
host = "localhost"
user = "phpmyadmin"
password = "12345678"
database = "agrimar"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + \
    user + ':' + password + '@ ' + host + '/' + database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from AgriMar.Agrimar import routes