
import sys
sys.path.append(".") 

from app.models import Submission
from app.exceptions.InvalidValue import InvalidValue
from app.exceptions.InvalidId import InvalidId
from uuid import UUID


def create(student_id, question_id, title, answer):
    """ Create Submission Api Service  """    
    try:
        UUID(student_id, version=4)
        UUID(question_id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')
    
     # Invalid Parameters Validation
    if (title.replace(' ', '') == ''):
        raise InvalidValue('Invalid Title.')
    
    submission_data = {
        'student_id': student_id,
        'question_id': question_id,
        'title': title,
        'answer': answer
    }

    submission = Submission(**submission_data)
    submission.save()

    response = {
        'id': submission.id,
        'student_id': submission.student_id,
        'question_id': submission.question_id,
        'title': submission.title,
        'answer': submission.answer
    }

    return response