
import sys
sys.path.append(".") 

from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

class Question(db.Model):
    """This class represents the question table."""

    __tablename__ = 'question'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255))
    description = db.Column(db.Text())
    content = db.Column(db.Text())
    author_id = db.Column(db.ForeignKey('manager.id'))
    author = relationship("Manager", back_populates="created_questions")
    submissions = relationship("Submission", back_populates="question")

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())



    def __init__(self, author_id, title, description, content):
        """initialize with parameters"""
        self.author_id = author_id
        self.title = title
        self.description = description
        self.content = content

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Question.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Question: {}>".format(self.title)
