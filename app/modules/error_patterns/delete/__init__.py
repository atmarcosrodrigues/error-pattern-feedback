# coding: utf-8

from flask import request, jsonify, Blueprint
import sys
sys.path.append(".") 

from app.exceptions.ErrorPatternNotFound import ErrorPatternNotFound
from app.modules.error_patterns.delete.service import delete

""" Delete Errorpattern Api """       
delete_errorpattern_api = Blueprint('delete_errorpattern_api', __name__)

@delete_errorpattern_api.route('/errorpatterns/<string:id>', methods=['DELETE'])
def delete_errorpattern(id):
    
    try:        
        response = jsonify(delete(id))
        response.status_code = 200
    except ErrorPatternNotFound as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
