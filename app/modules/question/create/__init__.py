# coding: utf-8

from flask import request, jsonify, Blueprint
from app.exceptions.InvalidId import InvalidId
from app.exceptions.InvalidValue import InvalidValue
from app.modules.question.create.service import create

import sys
sys.path.append(".") 

""" Create Question Api """    
create_question_api = Blueprint('create_question_api', __name__)

@create_question_api.route('/questions')
@create_question_api.route('/questions/', methods=['POST'])
def create_question():

    question_data = {
        'author_id' : str(request.data.get('author_id', '')),
        'title' : str(request.data.get('title', '')),
        'description' : str(request.data.get('description', '')),
        'content' : str(request.data.get('content', '')),
    }

    try:        
        response = jsonify(create(**question_data))
        response.status_code = 201
    except (InvalidId, InvalidValue) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
