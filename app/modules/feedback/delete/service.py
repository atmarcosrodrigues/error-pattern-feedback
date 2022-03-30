
import sys
sys.path.append(".") 

from app.exceptions.InvalidId import InvalidId
from app.exceptions.FeedbackNotFound import FeedbackNotFound
from app.models import Feedback
from uuid import UUID


def delete(id):
    """ Delete Feedback Api Service """    
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    feedback = Feedback.query.filter_by(id=id).first()        
    if (not feedback):
        raise FeedbackNotFound('Feedback not found.')
    
    feedback.delete()
    response =  {
        'message': 'Feedback deleted successfully.'
    }
    
    return response
