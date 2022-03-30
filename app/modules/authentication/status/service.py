

from flask import request, make_response, jsonify
from flask.views import MethodView

import os
import sys
sys.path.append(".") 

from app.models import User
from app.modules.authentication import token

# load secret key to generate token
SECRET_KEY = os.getenv("SECRET_KEY")


""" Auth User Status Api Service"""  


class UserStatusAPI(MethodView):
    """
    User Status Api Resource
    """
    def get(self):
        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''
        if auth_token:

            token_decode = token.decode(auth_token, SECRET_KEY)
            
            if token_decode['status'] == 'success':
                user = User.query.filter_by(id=token_decode['user_id']).first()
                responseObject = {
                    'status': 'success',
                    'data': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'admin': user.admin,
                    }
                }
                return make_response(jsonify(responseObject)), 200
            responseObject = {
                'status': 'fail',
                'message': token_decode['message']
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 401

