#!/usr/bin/python3
"""Data base storage"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import scoped_session


class DBStorage():
    """Class DBStorage to run a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor """
        engine = 'mysql+mysqldb://' + getenv('HBNB_MYSQL_USER') + ':'
        engine += getenv('HBNB_MYSQL_PWD') + '@' + getenv('HBNB_MYSQL_HOST')
        engine += '/' + getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(engine, pool_pre_ping=True)
        if (getenv("HBNB_ENV") == "test"):
            meta = MetaData(self.__engine)
            meta.reflect()
            meta.drop_all()
        Session = sessionmaker(self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """query on the current the database a specific class"""
        if (cls):
            classes = [cls]
        else:
            classes = [State, City, User, Place, Review, Amenity]
        dic = {}
        for clas in classes:
            for row in self.__session.query(clas).all():
                dic.update({row.to_dict()['__class__'] + "." + row.id: row})

        return (dic)

    def new(self, obj):
        """Adds an object to the current database session"""
        if (obj):
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj"""
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        """Reload"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
    
    def classes(self):
        """Returns a dictionary of classes."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def close(self):
        ''' call remove() method on the private session attribute '''
        self.__session.close()
