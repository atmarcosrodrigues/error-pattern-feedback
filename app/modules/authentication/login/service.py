from flask import request, make_response, jsonify
from flask.views import MethodView
import bcrypt

import os
import sys
sys.path.append(".") 

from app.models import User
from app.exceptions.FailedLoginException import FailedLoginException
from app.modules.authentication import token

# load secret key to generate token
SECRET_KEY = os.getenv("SECRET_KEY")

""" Auth Login Api Service"""  


def login(user):
    """
    Function login cheack if username/email:password are valid and match with registered data
    """

    if (user['username'] != ''):
        user_registered = User.query.filter_by(
            username=user['username']).first()
        error_message = 'The username or password are incorrect.'
    elif (user['email'] != ''):
        user_registered = User.query.filter_by(
            email=user['email']).first()
        error_message = 'The email or password are incorrect.'
    else:
        error_message = 'The username or password are incorrect.'
        raise FailedLoginException(error_message) 
    
    if user_registered:
        if bcrypt.checkpw(user['password'].encode('utf-8'), 
            bytes(user_registered.hash_password, 'utf-8')):
            return user_registered
    else: 
        raise FailedLoginException(error_message)    
    
        

class LoginAPI(MethodView):
    """
    User Login Api Resource
    """
    def post(self):
        
        # get the post data
        user_data = {
            'username' : str(request.data.get('username', '')),
            'email' : str(request.data.get('email', '')),
            'password' : str(request.data.get('password', ''))
        }
        
        try:            
            # call the login function
            user = login(user_data)
            
            # generate the auth token
            auth_token = token.encode(str(user.id), SECRET_KEY)
                
            # if tocken is valid return in a object response
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                }
                return make_response(jsonify(responseObject)), 200
            
        except (FailedLoginException, Exception) as error:
            
            responseObject = {
                'status': 'fail',
                'message': error.message
            }
            return make_response(jsonify(responseObject)), 401

