
import sys
sys.path.append(".") 

from app.exceptions.InvalidId import InvalidId
from app.exceptions.SubmissionNotFound import SubmissionNotFound
from app.models import Submission
from uuid import UUID


def delete(id):
    """ Delete Submission Api Service  """    
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    submission = Submission.query.filter_by(id=id).first()        
    if (not submission):
        raise SubmissionNotFound('Submission not found.')
    
    submission.delete()
    response =  {
        'message': 'Submission deleted successfully.'
    }
    
    return response
