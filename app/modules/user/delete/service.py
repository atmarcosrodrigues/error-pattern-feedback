import sys
from app.exceptions.InvalidId import InvalidId
from app.exceptions.UserNotFound import UserNotFound
sys.path.append(".") 

from app.models import User, Professor, Monitor, Student
from uuid import UUID

def delete_user(id):
    """ Delete user Api Service"""
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    user = User.query.filter_by(id=id).first()        
    if (not user):
        raise UserNotFound('User not found.')
    
    user.delete()
    response =  {
        'message': 'User deleted successfully.'
    }
    
    return response
