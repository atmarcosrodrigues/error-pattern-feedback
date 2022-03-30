
import sys
import re
from app import feedback_api
sys.path.append(".") 

from app.models import Feedback
from app.exceptions.InvalidValue import InvalidValue
from app.exceptions.InvalidId import InvalidId
from app.exceptions.FeedbackNotFound import FeedbackNotFound
from uuid import UUID


def edit(id, title, message):
    """ Edit Feedback Api Service """
    try:
        UUID(id, version=4)
    except Exception as error:
        raise InvalidId('The id value is not valid.')

    # Invalid Parameters Validation
    if (title.replace(' ', '') == ''):
        raise InvalidValue('Invalid Title.')
    if (message.replace(' ', '') == ''):
        raise InvalidValue('Invalid Message.')

    feedback = Feedback.query.filter_by(id=id).first()

    if (not feedback):
        raise FeedbackNotFound('Feedback not found.')

    if (title != ''):
        feedback.title = title
    if (message != ''):
        feedback.message = message
    feedback.save()

    response = {
        'id': feedback.id,
        'title': feedback.title,
        'message': feedback.message,
        'author_id': feedback.author_id,
        'submission_id': feedback.submission_id,
    }
    return response