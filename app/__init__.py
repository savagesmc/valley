from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from config import config

bootstrap = Bootstrap(app)
moment = Moment(app)

def create_app(config_name):

   app = Flask(__name__)
   app.config.from_object(config[config_name])
   config[config_name].init_app(app)

   bootstrap.init_app(app)
   moment.init_app(app)

   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)

   from .songApp import song as song_blueprint
   app.register_blueprint(song_blueprint, url_prefix='/valley')
   app.register_blueprint(song_blueprint, url_prefix='/waldorf')

   return app
