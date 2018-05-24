from flask import Flask
from instance.config import app_config
from app.common.mongo import Mongraph
from app.common.config import *


def create_app(config_name):

    from app.base_b.views import Base2

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # org
    app.add_url_rule('/base_2', view_func=Base2.as_view('base_2'), methods=['GET'])

    return app

