
import sys
sys.path.append(".") 

from app.models import Feedback, ReportedError, ErrorPattern
from app.exceptions.FeedbackNotFound import FeedbackNotFound
from app.exceptions.ReportedErrorNotFound import ReportedErrorNotFound
from app.exceptions.InvalidValue import InvalidValue
from app.exceptions.InvalidId import InvalidId
from uuid import UUID

""" Feedback Reported Erros Api Service"""

def insert(feedback_id, errorpattern_id):
    """ Function insert reported error """    
    try:
        UUID(feedback_id, version=4)
        UUID(errorpattern_id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')
    
    feedback = Feedback.query.filter_by(id=feedback_id).first()        
    if (not feedback):
        raise FeedbackNotFound('Feedback not found.')
    
    reported_error_data = {
        'feedback_id': feedback_id,
        'errorpattern_id' : errorpattern_id,
    }

    reported_error = ReportedError(**reported_error_data)
    reported_error.save()

    response = {
        'id': reported_error.id,
        'feedback_id': reported_error.feedback_id,
        'errorpattern_id' : reported_error.errorpattern_id,
    }

    return response

def remove(feedback_id, report_id):
    """ Function remove reported error """    
    try:
        UUID(feedback_id, version=4)
        UUID(report_id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    feedback = Feedback.query.filter_by(id=feedback_id).first()        
    if (not feedback):
        raise FeedbackNotFound('Feedback not found.')     
  
    reported_error = ReportedError.query.filter_by(id=report_id).first()        
    if (not reported_error):
        raise ReportedErrorNotFound('ReportedError not found.')
    
    reported_error.delete()
    response =  {
        'message': 'Reported Error deleted successfully.'
    }
    
    return response

def list_all(feedback_id):
    """ Function list all reported errors """    
    try:
        UUID(feedback_id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    feedback = Feedback.query.filter_by(id=feedback_id).first()        
    if (not feedback):
        raise FeedbackNotFound('Feedback not found.')     
  
    reported_errors_list = []

    for reported_error in feedback.reported_erros:
        errorpattern_id = reported_error.errorpattern_id
        # print ('ERRORREPORT:', errorpattern_id)
        error_pattern = ErrorPattern.query.filter_by(id=errorpattern_id).first()     
        reported_errors_list.append({
            'report_id': reported_error.id,
            'errorpattern_id': error_pattern.id,
            'title': error_pattern.title})

    return reported_errors_list