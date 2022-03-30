
import sys
sys.path.append(".") 

from app.models import Feedback
from app.exceptions.InvalidValue import InvalidValue
from app.exceptions.InvalidId import InvalidId
from uuid import UUID


def create(title, message, author_id, submission_id):
    """ Create Feedback Api Service"""    
    try:
        UUID(author_id, version=4)
        UUID(submission_id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')
    
     # Invalid Parameters Validation
    if (title.replace(' ', '') == ''):
        raise InvalidValue('Invalid Title.')
    
    feedback_data = {
        'title': title,
        'message': message,
        'author_id': author_id,
        'submission_id': submission_id,
    }

    feedback = Feedback(**feedback_data)
    feedback.save()

    response = {
        'id': feedback.id,
        'title': feedback.title,
        'message': feedback.message,
        'author_id': feedback.author_id,
        'submission_id': feedback.submission_id,
    }

    return response