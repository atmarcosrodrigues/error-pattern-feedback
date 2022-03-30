
import sys
sys.path.append(".") 

from app.models import ErrorPattern
from app.exceptions.InvalidValue import InvalidValue


def create(title, description, additional_content):
    """ Create Errorpattern Api Service  """    
    
     # Invalid Parameters Validation
    if (title.replace(' ', '') == ''):
        raise InvalidValue('Invalid Title.')
    if (description.replace(' ', '') == ''):
        raise InvalidValue('Invalid Description.')
    
    errorpartten_data = {
        'title': title,
        'description': description,
        'additional_content': additional_content
    }

    errorpattern = ErrorPattern(**errorpartten_data)
    errorpattern.save()

    response = {
        'id': errorpattern.id,
        'title': errorpattern.title,
        'description': errorpattern.description,
        'additional_content': errorpattern.additional_content
    }

    return response