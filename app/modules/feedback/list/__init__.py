# coding: utf-8

from flask import jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.InvalidValue import InvalidValue
from app.modules.feedback.list.service import get_all

""" List Feedback Api """
list_feedback_api = Blueprint('list_feedback_api', __name__)

@list_feedback_api.route('/feedbacks')
@list_feedback_api.route('/feedbacks/', methods=['GET'])
def list_feedback():

    try:        
        response = jsonify(get_all())
        response.status_code = 200
    except InvalidValue as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
