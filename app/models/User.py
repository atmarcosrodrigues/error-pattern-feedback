# app/models/user.py

import sys
sys.path.append(".") 

from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model):
    """This class represents the user table."""

    __tablename__ = 'user'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    info_description = db.Column(db.String(255))
    hash_password = db.Column(db.String(255))
    type = db.Column(db.String(50))
    admin = db.Column(db.Boolean, unique=False, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    __mapper_args__ = {
            'polymorphic_identity':'user',
            'polymorphic_on':type
        }

    def __init__(self, username, email, name, info_description, hash_password, admin):
        """initialize with parameters"""
        self.username = username
        self.email = email
        self.name = name
        self.info_description = info_description
        self.hash_password = hash_password
        self.admin = admin

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.name)
