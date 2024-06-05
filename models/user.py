#!/usr/bin/python3
"""
User Class from Models Module
"""

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """User class handles all application users"""
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        # __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place",
                              cascade="all, delete, delete-orphan",
                              backref="user")
        reviews = relationship("Review",
                               cascade="all, delete, delete-orphan",
                               backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
