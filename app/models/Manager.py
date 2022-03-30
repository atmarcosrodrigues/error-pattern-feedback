import sys

sys.path.append(".") 

from app.models.User import User

from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

class Manager(User):
    """This class represents the manager table."""

    __tablename__ = 'manager'
    id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key=True)
    created_questions = relationship("Question", back_populates="author")
    feedbacks_sent = relationship("Feedback", back_populates="author")

    __mapper_args__ = {
        'polymorphic_identity':'manager',
    
    }
    def __repr__(self):
        return "<Manager: {}>".format(self.name)
