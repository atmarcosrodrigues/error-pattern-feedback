import sys
sys.path.append(".") 

from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid



class ErrorPattern(db.Model):
    """This class represents the errorpattern table."""

    __tablename__ = 'errorpattern'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255))
    description = db.Column(db.Text())
    additional_content = db.Column(db.Text())
    reported_erro = relationship("ReportedError", back_populates="errorpattern")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


    def __init__(self, title, description, additional_content):
        """initialize with parameters"""
        self.title = title
        self.description = description
        self.additional_content = additional_content

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return ErrorPattern.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<ErrorPattern: {}>".format(self.title)
