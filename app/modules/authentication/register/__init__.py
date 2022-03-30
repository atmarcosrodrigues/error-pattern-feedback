# coding: utf-8
from flask import Blueprint

import sys
sys.path.append(".") 

from app.modules.authentication.register.service import RegisterAPI


""" Auth Register Api """  


# define the API resources
auth_register_api = Blueprint('auth_register_api', __name__)
registration_view = RegisterAPI.as_view('register_api')

# add Rules for API Endpoints
auth_register_api.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST']
)
