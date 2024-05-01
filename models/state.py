#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel, Base):
    """ The state class, contains state name """
    if models.storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            with state_id equals to the current State.id"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
