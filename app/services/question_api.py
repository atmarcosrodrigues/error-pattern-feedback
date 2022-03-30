## Import question api
import sys
sys.path.append(".") 

from app.modules.question.create import create_question_api
from app.modules.question.delete import delete_question_api
from app.modules.question.list import list_question_api
from app.modules.question.get_by_id import get_question_api

def register_question_api(app):
    app.register_blueprint(create_question_api)
    app.register_blueprint(delete_question_api)
    app.register_blueprint(list_question_api)
    app.register_blueprint(get_question_api)
