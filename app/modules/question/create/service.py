
import sys
sys.path.append(".") 

from app.models import Question
from app.exceptions.InvalidValue import InvalidValue
from app.exceptions.InvalidId import InvalidId
from uuid import UUID


def create(author_id, title, description, content):
    """ Create Question Api Service  """    
    try:
        UUID(author_id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')
    
     # Invalid Parameters Validation
    if (title.replace(' ', '') == ''):
        raise InvalidValue('Invalid Title.')
    if (description.replace(' ', '') == ''):
        raise InvalidValue('Invalid Description.')
    
    question_data = {
        'author_id': author_id,
        'title': title,
        'description': description,
        'content': content
    }

    question = Question(**question_data)
    question.save()

    response = {
        'id': question.id,
        'title': question.title,
        'description': question.description
    }

    return response