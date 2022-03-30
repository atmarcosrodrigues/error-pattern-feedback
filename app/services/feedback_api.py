## Import feedback api
import sys
sys.path.append(".") 

from app.modules.feedback.create import create_feedback_api
from app.modules.feedback.delete import delete_feedback_api
from app.modules.feedback.list import list_feedback_api
from app.modules.feedback.get_by_id import get_feedback_api
# from app.modules.feedback.edit import edit_feedback_api
from app.modules.feedback.reportederros import reportederros_feedback_api

def register_feedback_api(app):
    app.register_blueprint(create_feedback_api)
    app.register_blueprint(delete_feedback_api)
    app.register_blueprint(list_feedback_api)
    app.register_blueprint(get_feedback_api)
    # app.register_blueprint(edit_feedback_api)
    app.register_blueprint(reportederros_feedback_api)
