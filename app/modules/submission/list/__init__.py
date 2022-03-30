# coding: utf-8

from flask import  jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.InvalidValue import InvalidValue
from app.modules.submission.list.service import get_all

""" List Submission Api """
list_submission_api = Blueprint('list_submission_api', __name__)

@list_submission_api.route('/submissions')
@list_submission_api.route('/submissions/', methods=['GET'])
def list_submission():

    try:        
        response = jsonify(get_all())
        response.status_code = 200
    except InvalidValue as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
