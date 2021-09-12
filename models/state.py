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

    if (getenv("HBNB_TYPE_STORAGE") == "file"):
        @property
        def cities(self):
            from models.city import City
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if self.id == city.state_id:
                    cities_list.append(city)
            return cities_list
