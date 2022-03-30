
import sys
sys.path.append(".") 

from app.models import Submission

def get_all():
    """ List Submission Api Service """
    submissions = Submission.get_all()
    results = []

    for item in submissions:
        obj = {
            'student_id': item.student_id,
            'question_id': item.question_id,
            'title': item.title,
            'answer': item.answer
        }
        results.append(obj)    
    
    return results
