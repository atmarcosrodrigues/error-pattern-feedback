import sys


sys.path.append(".") 

from app.models.Manager import Manager

from app import db
from sqlalchemy.dialects.postgresql import UUID


class Monitor(Manager):
    """This class represents the monitor table."""

    __tablename__ = 'monitor'
    id = db.Column(UUID(as_uuid=True), db.ForeignKey('manager.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'monitor',
    }
    def __repr__(self):
        return "<Monitor: {}>".format(self.name)
