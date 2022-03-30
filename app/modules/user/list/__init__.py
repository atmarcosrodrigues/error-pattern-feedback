# coding: utf-8

from flask import jsonify, Blueprint
import sys
sys.path.append(".") 

from app.modules.user.list.service import get_all_users

""" List users Api """
listuser_api = Blueprint('listuser_api', __name__)

@listuser_api.route('/users')
@listuser_api.route('/users/', methods=['GET'])
def list_users():

    try:        
        response = jsonify(get_all_users())
        response.status_code = 200
    except Exception as error:
        response = jsonify(error.message)
        response.status_code = error.status_code
    return response
