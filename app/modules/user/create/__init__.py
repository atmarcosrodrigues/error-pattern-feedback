# coding: utf-8
#from app import create_app, db

from flask import request, jsonify, Blueprint
from app.exceptions.UserExceptions import InvalidUser
from app.modules.user.create.service import create

import sys
sys.path.append(".") 

""" Create user Api Service"""
createuser_api = Blueprint('createuser_api', __name__)

@createuser_api.route('/users')
@createuser_api.route('/users/', methods=['POST'])
def create_user():
    user_data = {
        'username' : str(request.data.get('username', '')),
        'email' : str(request.data.get('email', '')),
        'name' : str(request.data.get('name', '')),
        'info_description' : str(request.data.get('info_description', '')),
        'password' : str(request.data.get('password', '')),
        'user_type' : str(request.data.get('user_type', ''))
    }
    try:        
        response = jsonify(create(**user_data))
        response.status_code = 201
    except InvalidUser as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
