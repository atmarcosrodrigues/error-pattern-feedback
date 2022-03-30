from flask import request, make_response, jsonify
from flask.views import MethodView
import os

import sys
sys.path.append(".") 

from app.modules.authentication import token

# load secret key to generate token
SECRET_KEY = os.getenv("SECRET_KEY")
       

""" Auth Logout Service """  

class LogoutAPI(MethodView):
    """    
    Logout Resource
    """
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''

        if auth_token:
            token_decode = token.decode(auth_token, SECRET_KEY)
            
            if token_decode['status'] == 'success':
                try:                
                    # mark the token as blacklisted
                    blacklist_token = token.add_to_blacklist(auth_token) 
                    
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged out.'
                    }
                    return make_response(jsonify(responseObject)), 200
                except Exception as e:
                    responseObject = {
                        'status': 'fail',
                        'message': e
                    }
                    return make_response(jsonify(responseObject)), 200
            else:
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
            return make_response(jsonify(responseObject)), 403

