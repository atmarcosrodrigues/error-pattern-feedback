## Import errorpattern api
import sys
sys.path.append(".") 

from app.modules.error_patterns.create import create_errorpattern_api
from app.modules.error_patterns.delete import delete_errorpattern_api
from app.modules.error_patterns.get_by_id import get_errorpattern_api
from app.modules.error_patterns.list import list_errorpattern_api

def register_errorpattern_api(app):
    app.register_blueprint(create_errorpattern_api)
    app.register_blueprint(delete_errorpattern_api)
    app.register_blueprint(get_errorpattern_api)
    app.register_blueprint(list_errorpattern_api)
