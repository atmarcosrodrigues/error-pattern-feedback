# coding: utf-8
from flask import request, jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.InvalidId import InvalidId
from app.exceptions.FeedbackNotFound import FeedbackNotFound
from app.exceptions.InvalidValue import InvalidValue
from app.modules.feedback.edit.service import edit

""" Edit Feedback Api """
edit_feedback_api = Blueprint('edit_feedback_api', __name__)

@edit_feedback_api.route('/feedbacks/<string:id>', methods=['PUT'])
def edit_feedback(id):
    feedback_data = {
        'id': id,
        'title' : str(request.data.get('title', '')),
        'message' : str(request.data.get('message', ''))
    }
    try:        
        response = jsonify(edit(**feedback_data))
        response.status_code = 200
    except (InvalidId, FeedbackNotFound, InvalidValue) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
