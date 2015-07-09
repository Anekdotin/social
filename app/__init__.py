from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import UPLOAD_FOLDER


app = Flask(__name__)
app.config.from_object('config')


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = 'login'
bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment()
moment.init_app(app)









from .main import main as main_blueprint
app.register_blueprint(main_blueprint)




from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

from .api_1_0 import api as api_1_0_blueprint
app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

from .main import views

from app import models






