# coding: utf-8

from flask import jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.InvalidValue import InvalidValue
from app.modules.question.list.service import get_all

""" List Question Api """
list_question_api = Blueprint('list_question_api', __name__)

@list_question_api.route('/questions')
@list_question_api.route('/questions/', methods=['GET'])
def list_question():

    try:        
        response = jsonify(get_all())
        response.status_code = 200
    except InvalidValue as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
