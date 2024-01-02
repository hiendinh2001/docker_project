from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
import cloudinary
from flask_login import LoginManager
from flask_babelex import Babel
import os


app = Flask(__name__)
app.secret_key = '12#^&*+_%&*)(*(&(*^&^$%$#((*65t87676'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'root'),
    os.getenv('DB_PASSWORD', '123456'),
    os.getenv('DB_HOST', 'mysql-docker-project-container'),
    os.getenv('DB_NAME', 'db_telemedicine_docker')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 6
app.config['COMMENT_SIZE'] = 3
app.config['MY_CART'] = 'cart'

db = SQLAlchemy(app=app)
babel = Babel(app=app)

cloudinary.config(
    cloud_name='dnnjwr3bl',
    api_key='537858359784695',
    api_secret='MTiq2hbjq2WyHYUwgX-hJaplU6k',
)

login = LoginManager(app=app)

@babel.localeselector
def load_locale():
    return 'en'

#from app import models
from app import index
