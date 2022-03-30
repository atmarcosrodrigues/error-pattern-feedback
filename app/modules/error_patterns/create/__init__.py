# coding: utf-8

from flask import request, jsonify, Blueprint
from app.exceptions.InvalidValue import InvalidValue
from app.modules.error_patterns.create.service import create

import sys
sys.path.append(".") 

""" Create Errorpattern Api """

create_errorpattern_api = Blueprint('create_errorpattern_api', __name__)

@create_errorpattern_api.route('/errorpatterns')
@create_errorpattern_api.route('/errorpatterns/', methods=['POST'])
def create_errorpattern():

    errorpattern_data = {
        'title' : str(request.data.get('title', '')),
        'description' : str(request.data.get('description', '')),
        'additional_content' : str(request.data.get('additional_content', '')),
    }

    try:        
        response = jsonify(create(**errorpattern_data))
        response.status_code = 201
    except InvalidValue as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
