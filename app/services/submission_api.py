## Import submission api
import sys
sys.path.append(".") 

from app.modules.submission.create import create_submission_api
from app.modules.submission.delete import delete_submission_api
from app.modules.submission.list import list_submission_api
from app.modules.submission.get_by_id import get_submission_api

def register_submission_api(app):
    app.register_blueprint(create_submission_api)
    app.register_blueprint(delete_submission_api)
    app.register_blueprint(list_submission_api)
    app.register_blueprint(get_submission_api)
