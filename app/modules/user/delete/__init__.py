# coding: utf-8

from flask import request, jsonify, Blueprint
from app.exceptions.InvalidId import InvalidId
from app.exceptions.UserNotFound import UserNotFound
from app.modules.user.delete.service import delete_user
import sys
sys.path.append(".") 

""" Delete user Api Resource"""
delete_api = Blueprint('delete_api', __name__)

@delete_api.route('/users/<string:id>', methods=['DELETE'])
def delete(id):

    try:        
        response = jsonify(delete_user(id))
        response.status_code = 200
    except (NameError, InvalidId, UserNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
