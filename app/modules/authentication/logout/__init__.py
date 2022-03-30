# coding: utf-8

from flask import Blueprint
from app.modules.authentication.logout.service import LogoutAPI

import sys
sys.path.append(".") 


""" Auth Logout Api """  

# define the API resources
auth_logout_api = Blueprint('auth_logout_api', __name__)
logout_view = LogoutAPI.as_view('logout_api')

# add Rules for API Endpoints
auth_logout_api.add_url_rule(
    '/auth/logout',
    view_func=logout_view,
    methods=['POST']
)
