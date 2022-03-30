
import sys
sys.path.append(".") 

from app.models import ErrorPattern

def get_all():
    """ List Errorpattern Api Service  """    
    
    errorpatterns = ErrorPattern.get_all()
    results = []

    for item in errorpatterns:
        obj = {
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'additional_content': item.additional_content
        }
        results.append(obj)    
    
    return results
