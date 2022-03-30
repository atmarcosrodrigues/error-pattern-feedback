
import sys
sys.path.append(".") 

from app.models import User


def get_all_users():
    """ Get all users Api Service"""

    users = User.get_all()
    results = []

    for user in users:
        obj = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'date_created': user.date_created
        }
        results.append(obj)    
    
    return results
