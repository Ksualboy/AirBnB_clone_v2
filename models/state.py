#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship('City', backref="state",
                              cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            mycities = []
            for city in storage.all(City).values():
                if (city.state_id == self.id):
                        mycities.append(city)
            return mycities
