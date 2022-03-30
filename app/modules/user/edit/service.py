import sys
sys.path.append(".") 
from app.exceptions.InvalidId import InvalidId
from app.exceptions.UserNotFound import UserNotFound

from app.models import User
from uuid import UUID

def edit_user(id, username, email, name, info_description, password):
    """ Edit user Api Service"""
    
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    user = User.query.filter_by(id=id).first()

    if (not user):
        raise UserNotFound('User not found.')

    if (username != ''):
        user.username = username
    if (email != ''):
        user.email = email
    if (name != ''):
        user.name = name
    if (info_description != ''):
        user.info_description = info_description
    if (password != ''):
        user.password = password
    user.save()

    response =  {
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'info_description': user.info_description,
        'email': user.email,
        'date_created': user.date_created
    }
    
    return response
