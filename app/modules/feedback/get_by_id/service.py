
import sys
sys.path.append(".") 

from app.models import Feedback
from app.exceptions.InvalidId import InvalidId
from app.exceptions.FeedbackNotFound import FeedbackNotFound
from uuid import UUID

def get_by_id(id):
    """ Get by id Feedback Api Service """
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    feedback = Feedback.query.filter_by(id=id).first()        
    if (not feedback):
        raise FeedbackNotFound('Feedback not found.')
    
    response =  {
            'id': feedback.id,
            'title': feedback.title,
            'message': feedback.message,
            'author_id': feedback.author_id,
            'submission_id': feedback.submission_id,
    }
    
    return response