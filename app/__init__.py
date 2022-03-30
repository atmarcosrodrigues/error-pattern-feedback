# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

# ## Import modules apis
from app.services.user_api import *
from app.services.errorpattern_api import *
from app.services.question_api import *
from app.services.submission_api import *
from app.services.feedback_api import *
from app.services.auth_api import *

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # register modules apis
    register_user_api(app)
    register_errorpattern_api(app)
    register_question_api(app)
    register_submission_api(app)
    register_feedback_api(app)
    register_auth_api(app)

    db.init_app(app)

    return app