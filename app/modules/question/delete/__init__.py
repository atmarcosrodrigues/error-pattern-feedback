# coding: utf-8

from flask import request, jsonify, Blueprint
import sys
sys.path.append(".") 

from app.exceptions.QuestionNotFound import QuestionNotFound
from app.modules.question.delete.service import delete

""" Delete Question Api """    
delete_question_api = Blueprint('delete_question_api', __name__)

@delete_question_api.route('/questions/<string:id>', methods=['DELETE'])
def delete_question(id):
    
    try:        
        response = jsonify(delete(id))
        response.status_code = 200
    except QuestionNotFound as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
