## Import user api
import sys
sys.path.append(".") 

from app.modules.user.create import createuser_api
from app.modules.user.list import listuser_api
from app.modules.user.get_by_id import getbyid_api
from app.modules.user.delete import delete_api
from app.modules.user.edit import edituser_api

def register_user_api(app):
    app.register_blueprint(createuser_api)
    app.register_blueprint(listuser_api)
    app.register_blueprint(getbyid_api)
    app.register_blueprint(delete_api)
    app.register_blueprint(edituser_api)
