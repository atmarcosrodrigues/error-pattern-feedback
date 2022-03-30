# coding: utf-8

from flask import jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.SubmissionNotFound import SubmissionNotFound
from app.modules.submission.get_by_id.service import get_by_id
from app.exceptions.InvalidId import InvalidId

""" Get by id Submission Api """
get_submission_api = Blueprint('get_submission_api', __name__)

@get_submission_api.route('/submissions/<string:id>', methods=['GET'])
def get_by_id_submission(id):
    
    try:            
        response = jsonify(get_by_id(id))
        response.status_code = 200
    except (InvalidId, SubmissionNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
