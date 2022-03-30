# coding: utf-8

from flask import jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.QuestionNotFound import QuestionNotFound
from app.modules.question.get_by_id.service import get_by_id
from app.exceptions.InvalidId import InvalidId

""" Get by id Question Api """    
get_question_api = Blueprint('get_question_api', __name__)

@get_question_api.route('/questions/<string:id>', methods=['GET'])
def get_by_id_question(id):
    
    try:            
        response = jsonify(get_by_id(id))
        response.status_code = 200
    except (InvalidId, QuestionNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
