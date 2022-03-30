# coding: utf-8

from flask import request, jsonify, Blueprint
from app.exceptions.InvalidId import InvalidId
from app.exceptions.UserNotFound import UserNotFound
from app.modules.user.edit.service import edit_user
import sys
sys.path.append(".") 

""" Edit users Api """
edituser_api = Blueprint('edituser_api', __name__)

@edituser_api.route('/users/<string:id>', methods=['PUT'])
def edit(id):

    user_update = {
        'username' : str(request.data.get('username', '')),
        'email' : str(request.data.get('email', '')),
        'name' : str(request.data.get('name', '')),
        'info_description' : str(request.data.get('info_description', '')),
        'password' : str(request.data.get('password', ''))
    }

    try:        
        response = jsonify(edit_user(id, **user_update))
        response.status_code = 200
    except (NameError, InvalidId, UserNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
