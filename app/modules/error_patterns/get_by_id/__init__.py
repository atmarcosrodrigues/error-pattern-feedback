# coding: utf-8

from flask import jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.ErrorPatternNotFound import ErrorPatternNotFound
from app.modules.error_patterns.get_by_id.service import get_by_id
from app.exceptions.InvalidId import InvalidId

""" Get by id Errorpattern Api Service  """        
get_errorpattern_api = Blueprint('get_errorpattern_api', __name__)

@get_errorpattern_api.route('/errorpatterns/<string:id>', methods=['GET'])
def get_by_id_errorpattern(id):
    try:        
        response = jsonify(get_by_id(id))
        response.status_code = 200
    except (InvalidId, ErrorPatternNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
