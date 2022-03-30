# coding: utf-8

from flask import request, jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.InvalidId import InvalidId
from app.exceptions.InvalidValue import InvalidValue
from app.modules.feedback.create.service import create


""" Create Feedback Api """
create_feedback_api = Blueprint('create_feedback_api', __name__)

@create_feedback_api.route('/feedbacks')
@create_feedback_api.route('/feedbacks/', methods=['POST'])
def create_feedback():

    feedback_data = {
        'title' : str(request.data.get('title', '')),
        'message' : str(request.data.get('message', '')),
        'author_id' : str(request.data.get('author_id', '')),
        'submission_id' : str(request.data.get('submission_id', '')),
    }

    try:        
        response = jsonify(create(**feedback_data))
        response.status_code = 201
    except (InvalidId, InvalidValue) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
