## Import auth api
import sys
sys.path.append(".") 

from app.modules.authentication.register import auth_register_api
from app.modules.authentication.login import auth_login_api
from app.modules.authentication.status import auth_userstatus_api
from app.modules.authentication.logout import auth_logout_api

def register_auth_api(app):
    app.register_blueprint(auth_register_api)
    app.register_blueprint(auth_login_api)
    app.register_blueprint(auth_userstatus_api)    
    app.register_blueprint(auth_logout_api)
