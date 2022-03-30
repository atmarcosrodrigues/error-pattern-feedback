
import sys
sys.path.append(".") 

from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

class Submission(db.Model):
    """This class represents the submission table."""

    __tablename__ = 'submission'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255))
    answer = db.Column(db.Text())
    student_id = db.Column(db.ForeignKey('student.id'))
    question_id = db.Column(db.ForeignKey('question.id'))
    student = relationship("Student", back_populates="submissions")
    question = relationship("Question", back_populates="submissions")
    feedbacks = relationship("Feedback", back_populates="submission")
    
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, student_id, question_id, title, answer):
        """initialize with parameters"""
        self.student_id = student_id
        self.question_id = question_id
        self.title = title
        self.answer = answer

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Submission.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Submission: {}>".format(self.title)

