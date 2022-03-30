
import sys
import re
sys.path.append(".") 

from app.models import Question

def get_all():
    """ List Question Api Service  """
    questions = Question.get_all()
    results = []

    for item in questions:
        obj = {
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'content': item.content
        }
        results.append(obj)    
    
    return results
