# -*- coding: utf-8 -*-

from flask import jsonify, Blueprint
from app.exceptions.InvalidId import InvalidId
from app.exceptions.UserNotFound import UserNotFound
from app.modules.user.get_by_id.service import get_user_by_id
import sys
sys.path.append(".") 

""" Get by id user Api"""
getbyid_api = Blueprint('getbyid_api', __name__)

@getbyid_api.route('/users/<string:id>', methods=['GET'])
def get_by_id(id):

    try:        
        response = jsonify(get_user_by_id(id))
        response.status_code = 200
    except (NameError, InvalidId, UserNotFound) as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
