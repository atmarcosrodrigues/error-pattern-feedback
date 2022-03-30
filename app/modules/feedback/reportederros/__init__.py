# coding: utf-8
from flask import request, jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.InvalidId import InvalidId
from app.exceptions.InvalidValue import InvalidValue
from app.exceptions.FeedbackNotFound import FeedbackNotFound
from app.exceptions.ReportedErrorNotFound import ReportedErrorNotFound
from app.modules.feedback.reportederros.service import insert, remove, list_all

""" Feedback Reported Erros Api """
reportederros_feedback_api = Blueprint('reportederros_feedback_api', __name__)

""" Routes and service call to add/insert feedback reported errors """
@reportederros_feedback_api.route('/feedbacks/<string:id>/reportederros')
@reportederros_feedback_api.route('/feedbacks/<string:id>/reportederros/', methods=['POST'])
def add_reportederror(id):
    reported_error_data = {
        'feedback_id': id,
        'errorpattern_id' : str(request.data.get('errorpattern_id', '')),
    }
    try:        
        response = jsonify(insert(**reported_error_data))
        response.status_code = 201
    except (InvalidId, InvalidValue) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response


""" Routes and service call to remove reported errors from feedback"""
@reportederros_feedback_api.route('/feedbacks/<string:id>/reportederros/<string:report_id>', methods=['DELETE'])
def delete_reportederrors(id, report_id):
    try:        
        response = jsonify(remove(feedback_id=id, report_id=report_id))
        response.status_code = 200
    except (InvalidId, InvalidValue, FeedbackNotFound, ReportedErrorNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response


""" Routes and funtion to list all feedback reported errors """
@reportederros_feedback_api.route('/feedbacks/<string:id>/reportederros')
@reportederros_feedback_api.route('/feedbacks/<string:id>/reportederros/', methods=['GET'])
def list_reportederrors(id):
    
    try:        
        response = jsonify(list_all(feedback_id=id))
        response.status_code = 200
    except (InvalidId, InvalidValue, FeedbackNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
