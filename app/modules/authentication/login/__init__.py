# coding: utf-8

from flask import Blueprint
from app.modules.authentication.login.service import LoginAPI

import sys
sys.path.append(".") 

""" Auth Login Api """  

# define the API resources
auth_login_api = Blueprint('auth_login_api', __name__)
login_view = LoginAPI.as_view('login_api')

# add Rules for API Endpoints
auth_login_api.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)
