import bcrypt
import sys
import re
sys.path.append(".") 

from app.models import Professor, Monitor, Student
from app.exceptions.UserExceptions import InvalidUser


def check_valid_email(email):
    """This function check if email parameter is a valid email address"""
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(regex, email))

def create(username, email, name, user_type, info_description, password):
    """ Create user Api Service"""
    
    """This function create a user object using the models (Professor, Monitor and User).
       The created object is stored on database """

    # Invalid Parameters Validation
    if (not username.replace('_', '').isalnum()):
        raise InvalidUser('Invalid Username: Use only letters, numbers or undescore(_).')
    if (not check_valid_email(email)):
        raise InvalidUser('Invalid Email Address.')
    if (user_type not in ['PROFESSOR', 'MONITOR', 'STUDENT']):
        raise InvalidUser('Invalid User Type')
    if (len(password.replace(' ', '')) < 6):
        raise InvalidUser('Invalid Password.')

    # Generate a hashed code password
    hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
    # Make the parameters: values mapping for user model creation
    user_data = {          
        'username' : username,
        'email' : email,
        'name' : name,
        'info_description' : info_description,
        'hash_password' : hash_password.decode('utf8'),
        'admin' : False
    }

    # Check the specif model (Professor, Monitor or Student) to be created 
    # Set the admin authorization atribute related with the user type
    if user_type == 'PROFESSOR':
        user_data['admin'] = True
        user = Professor(**user_data)
    elif user_type == 'MONITOR':
        user_data['admin'] = True
        user = Monitor(**user_data)
    else:
        user = Student(**user_data)

    user.save()
    
    response = {
        'id': user.id,
        'username': user.username,
        'enail': user.email,
        'name': user.name,
    }

    return response

