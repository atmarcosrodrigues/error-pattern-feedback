# coding: utf-8

from flask import jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.FeedbackNotFound import FeedbackNotFound
from app.modules.feedback.get_by_id.service import get_by_id
from app.exceptions.InvalidId import InvalidId

""" Get by id Feedback Api """
get_feedback_api = Blueprint('get_feedback_api', __name__)

@get_feedback_api.route('/feedbacks/<string:id>', methods=['GET'])
def get_by_id_feedback(id):
    
    try:            
        response = jsonify(get_by_id(id))
        response.status_code = 200
    except (InvalidId, FeedbackNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
