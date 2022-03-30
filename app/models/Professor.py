from multiprocessing import Manager
import sys

sys.path.append(".") 

from app.models.Manager import Manager

from app import db
from sqlalchemy.dialects.postgresql import UUID

class Professor(Manager):
    """This class represents the professor table."""

    __tablename__ = 'professor'
    id = db.Column(UUID(as_uuid=True), db.ForeignKey('manager.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'professor',
    
    }
    def __repr__(self):
        return "<Professor: {}>".format(self.name)
