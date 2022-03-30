# -*- coding: utf-8 -*-

import sys
from app.exceptions.InvalidId import InvalidId
from app.exceptions.UserNotFound import UserNotFound
sys.path.append(".") 

from app.models import User, Professor, Monitor, Student
from uuid import UUID

def get_user_by_id(id):
    """ Get by id user Api Service"""

    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    user = User.query.filter_by(id=id).first()        
    if (not user):
        raise UserNotFound('User not found.')
    
    response =  {
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'info_description': user.info_description,
        'email': user.email,
        'date_created': user.date_created
    }
    
    return response
