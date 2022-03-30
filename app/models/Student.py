import sys

sys.path.append(".") 

from app.models.User import User

from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Student(User):
    """This class represents the student table."""

    __tablename__ = 'student'
    id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), primary_key=True)
    submissions = relationship("Submission", back_populates="student")

    __mapper_args__ = {
        'polymorphic_identity':'student',
    }
    def __repr__(self):
        return "<Student: {}>".format(self.name)
