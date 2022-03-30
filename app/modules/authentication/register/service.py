from flask import request, make_response, jsonify
from flask.views import MethodView
import os

import sys
sys.path.append(".") 

from app.models import User
from app.modules.authentication import token
from app.modules.user.create.service import create

# load secret key to generate token
SECRET_KEY = os.getenv("SECRET_KEY")
       

""" Auth Register Api Service"""  

class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def post(self):
        user_data = {
            'username' : str(request.data.get('username', '')),
            'email' : str(request.data.get('email', '')),
            'name' : str(request.data.get('name', '')),
            'info_description' : str(request.data.get('info_description', '')),
            'password' : str(request.data.get('password', '')),
            'user_type' : str(request.data.get('user_type', ''))
        }
        user = User.query.filter_by(email=user_data['email']).first()
        if not user:
            try:
                # register the user
                registered_user = create(**user_data)

                # generate the auth token
                auth_token = token.encode(str(registered_user['id']), SECRET_KEY)

                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token.decode() 
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202
