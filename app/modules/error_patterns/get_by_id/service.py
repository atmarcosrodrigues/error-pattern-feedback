
import sys
sys.path.append(".") 

from app.models import ErrorPattern
from app.exceptions.InvalidId import InvalidId
from app.exceptions.ErrorPatternNotFound import ErrorPatternNotFound
from uuid import UUID

   
def get_by_id(id):
    """ Get by id Errorpattern Api Service  """    
    
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    errorpattern = ErrorPattern.query.filter_by(id=id).first()        
    if (not errorpattern):
        raise ErrorPatternNotFound('ErrorPattern not found.')
    
    response =  {
        'id': errorpattern.id,
        'title': errorpattern.title,
        'description': errorpattern.description,
        'additional_content': errorpattern.additional_content,
    }
    
    return response