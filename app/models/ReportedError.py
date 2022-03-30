import sys
sys.path.append(".") 

from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

class ReportedError(db.Model):
    """This class represents the reportederror table."""

    __tablename__ = 'reportederror'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    feedback_id = db.Column(db.ForeignKey('feedback.id'))    
    feedback = relationship("Feedback", back_populates="reported_erros")
    errorpattern_id = db.Column(db.ForeignKey('errorpattern.id'))    
    errorpattern = relationship("ErrorPattern", back_populates="reported_erro")

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, feedback_id, errorpattern_id):
        """initialize with parameters"""
        self.feedback_id = feedback_id
        self.errorpattern_id = errorpattern_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return ReportedError.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<ReportedError: {}>".format(self.id)
