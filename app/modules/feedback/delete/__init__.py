# coding: utf-8

from flask import jsonify, Blueprint
import sys
sys.path.append(".") 

""" Delete Feedback Api """
from app.exceptions.FeedbackNotFound import FeedbackNotFound
from app.modules.feedback.delete.service import delete


delete_feedback_api = Blueprint('delete_feedback_api', __name__)

@delete_feedback_api.route('/feedbacks/<string:id>', methods=['DELETE'])
def delete_feedback(id):

    try:        
        response = jsonify(delete(id))
        response.status_code = 200
    except FeedbackNotFound as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
