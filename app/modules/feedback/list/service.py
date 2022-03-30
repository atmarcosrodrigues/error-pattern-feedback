
import sys
sys.path.append(".") 

from app.models import Feedback

def get_all():
    """ List Feedback Api Service"""
    feedbacks = Feedback.get_all()
    results = []

    for item in feedbacks:
        obj = {
            'id': item.id,
            'title': item.title,
            'message': item.message,
            'author_id': item.author_id,
            'submission_id': item.submission_id,
        }
        results.append(obj)    
    
    return results
