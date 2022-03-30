
import sys
import re
sys.path.append(".") 

from app.models import Question
from app.exceptions.InvalidId import InvalidId
from app.exceptions.QuestionNotFound import QuestionNotFound
from uuid import UUID

def get_by_id(id):
    """ Get by id Question Api Service  """    
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    question = Question.query.filter_by(id=id).first()        
    if (not question):
        raise QuestionNotFound('Question not found.')
    
    response =  {
        'id': question.id,
        'title': question.title,
        'description': question.description,
        'content': question.content,
    }
    
    return response