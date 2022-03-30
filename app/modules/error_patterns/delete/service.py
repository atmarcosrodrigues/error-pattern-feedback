
import sys
import re
sys.path.append(".") 

from app.exceptions.InvalidId import InvalidId
from app.exceptions.ErrorPatternNotFound import ErrorPatternNotFound
from app.models import ErrorPattern
from uuid import UUID


def delete(id):
    """ Delete Errorpattern Api Service  """    
    
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    error_pattern = ErrorPattern.query.filter_by(id=id).first()        
    if (not error_pattern):
        raise ErrorPatternNotFound('ErrorPattern not found.')
    
    error_pattern.delete()
    response =  {
        'message': 'ErrorPattern deleted successfully.'
    }
    
    return response
