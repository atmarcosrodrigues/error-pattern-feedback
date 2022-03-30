# coding: utf-8

from flask import jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.SubmissionNotFound import SubmissionNotFound
from app.modules.submission.delete.service import delete

""" Delete Submission Api """
delete_submission_api = Blueprint('delete_submission_api', __name__)

@delete_submission_api.route('/submissions/<string:id>', methods=['DELETE'])
def delete_submission(id):

    try:        
        response = jsonify(delete(id))
        response.status_code = 200
    except SubmissionNotFound as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
