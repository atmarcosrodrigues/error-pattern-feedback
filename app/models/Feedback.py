from email import message
import sys
sys.path.append(".") 

from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

class Feedback(db.Model):
    """This class represents the feedback table."""

    __tablename__ = 'feedback'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255))
    message = db.Column(db.Text())    
    author_id = db.Column(db.ForeignKey('manager.id'))
    submission_id = db.Column(db.ForeignKey('submission.id'))
    author =  relationship("Manager", back_populates="feedbacks_sent")
    submission = relationship("Submission", back_populates="feedbacks")
    reported_erros = relationship("ReportedError", back_populates="feedback")

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, title, message, author_id, submission_id):
        """initialize with parameters"""
        self.title = title
        self.message = message
        self.author_id = author_id
        self.submission_id = submission_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Feedback.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Feedback: {}>".format(self.title)
