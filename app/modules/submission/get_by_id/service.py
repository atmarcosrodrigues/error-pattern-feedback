
import sys
sys.path.append(".") 

from app.models import Submission
from app.exceptions.InvalidId import InvalidId
from app.exceptions.SubmissionNotFound import SubmissionNotFound
from uuid import UUID

def get_by_id(id):
    """ Get by id Submission Api Service """
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    submission = Submission.query.filter_by(id=id).first()        
    if (not submission):
        raise SubmissionNotFound('Submission not found.')
    
    response =  {
        'id': submission.id,
        'student_id': submission.student_id,
        'question_id': submission.question_id,
        'title': submission.title,
        'answer': submission.answer,
    }
    
    return response