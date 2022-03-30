# coding: utf-8

from flask import request, jsonify, Blueprint
from app.exceptions.InvalidId import InvalidId
from app.exceptions.InvalidValue import InvalidValue
from app.modules.submission.create.service import create

import sys
sys.path.append(".") 

""" Create Submission Api """
create_submission_api = Blueprint('create_submission_api', __name__)

@create_submission_api.route('/submissions')
@create_submission_api.route('/submissions/', methods=['POST'])
def create_submission():

    submission_data = {
        'student_id' : str(request.data.get('student_id', '')),
        'question_id' : str(request.data.get('question_id', '')),
        'title' : str(request.data.get('title', '')),
        'answer' : str(request.data.get('answer', '')),
    }

    try:        
        response = jsonify(create(**submission_data))
        response.status_code = 201
    except (InvalidId, InvalidValue) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
