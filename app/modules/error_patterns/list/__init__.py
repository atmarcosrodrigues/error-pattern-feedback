# coding: utf-8

from flask import jsonify, Blueprint

import sys
sys.path.append(".") 

from app.exceptions.InvalidValue import InvalidValue
from app.modules.error_patterns.list.service import get_all

""" List Errorpattern Api Service  """       
list_errorpattern_api = Blueprint('list_errorpattern_api', __name__)

@list_errorpattern_api.route('/errorpatterns')
@list_errorpattern_api.route('/errorpatterns/', methods=['GET'])
def list_errorpattern():

    try:        
        response = jsonify(get_all())
        response.status_code = 200
    except InvalidValue as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
