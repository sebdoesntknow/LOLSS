from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
#from flask.ext.mail import Mail
#from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from werkzeug.contrib.fixers import ProxyFix
from config import config

bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    # App body goes here
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    proxyfix = ProxyFix(app.wsgi_app)

    login_manager.init_app(app)
    bootstrap.init_app(app)
    #mail.init_app(app)
    #moment.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .champions import champions as champ_blueprint
    from .streams import streams as streams_blueprint
    from .api_search import api_search as api_search_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(champ_blueprint)
    app.register_blueprint(streams_blueprint)
    app.register_blueprint(api_search_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

