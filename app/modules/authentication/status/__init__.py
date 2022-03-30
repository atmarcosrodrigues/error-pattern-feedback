# coding: utf-8
from flask import Blueprint

import sys
sys.path.append(".") 

from app.modules.authentication.status.service import UserStatusAPI


""" Auth User Status Api """  


# define the API resources
auth_userstatus_api = Blueprint('auth_userstatus_api', __name__)
userstatus_view = UserStatusAPI.as_view('userstatus_api')

# add Rules for API Endpoints
auth_userstatus_api.add_url_rule(
    '/auth/status',
    view_func=userstatus_view,
    methods=['GET']
)
