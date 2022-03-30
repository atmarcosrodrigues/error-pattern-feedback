
import sys
import re
sys.path.append(".") 

from app.exceptions.InvalidId import InvalidId
from app.exceptions.QuestionNotFound import QuestionNotFound
from app.models import Question
from uuid import UUID


def delete(id):
    """ Delete Question Api Service  """    
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    question = Question.query.filter_by(id=id).first()        
    if (not question):
        raise QuestionNotFound('Question not found.')
    
    question.delete()
    response =  {
        'message': 'Question deleted successfully.'
    }
    
    return response
