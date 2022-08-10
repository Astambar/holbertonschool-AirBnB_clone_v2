#!/usr/bin/python3.8
"""module for database storage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """This class defines the DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """
        The __init__ function is called every time a new object is created.
        The first argument to __init__ should always be 'self'
        -- this refers to the object being created.
        The remaining arguments are those passed to the class when it is instantiated.


        :param self: Reference the attributes and methods of the class in which it is used
        :return: None
        :doc-author: Trelent
        """

        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}/{database}", pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        The all function is used to return a dictionary of all objects in the
        database. It takes one argument, cls, which is optional. If no argument is
        passed it will return a dictionary of all objects in the database. If an
        argument is passed it must be either a string or class object that exists in 
        the database and will return only those instances.

        :param self: Refer to the object that is being created
        :param cls=None: Determine whether to return all the objects in the database or only those of a specific class
        :return: A dictionary of all the objects in the database
        :doc-author: Trelent
        """

        clsDict = {}
        typeOfObjects = {"City": City, "State": State, "User": User,
                         "Place": Place, "Review": Review, "Amenity": Amenity}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            for instance in self.__session.query(cls).all():
                key = f"{instance.__class__.__name__}.{instance.id}"
                clsDict[key] = instance
        else:
            for obj in typeOfObjects.values():
                for instance in self.__session.query(obj).all():
                    key = f'{instance.__class__.__name__}.{instance.id}'
                    clsDict[key] = instance
        return clsDict

    def new(self, obj):
        """
        The new function creates a new instance of the class passed as an argument.
        It then calls the save function on that instance to store it in the database.

        :param self: Refer to the object itself
        :param obj: Pass in the object that is being called
        :return: The same as the old function
        :doc-author: Trelent
        """
        self.__session.add(obj)

    def save(self):
        """
        The save function is used to save the data in the database.
        It is called by a class method of Base and it takes no arguments.
        The function first creates an engine using create_engine, which is then passed to 
        the sessionmaker function, which returns a Session object. The Session object 
        is then passed into scoped_session, which returns a new Session() instance bound 
        to our database file.

        :param self: Access variables that belongs to the class
        :return: A dictionary of the class attributes and their values
        :doc-author: Trelent
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        The delete function deletes an object from the database.
           Args:
                obj (object): The object to be deleted.

            Returns:
                None

        :param self: Refer to the object that is calling the function
        :param obj=None: Delete the object that is passed in as an argument
        :return: The value of the object that was deleted
        :doc-author: Trelent
        """
        
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        The reload function creates the database and its tables.

        :param self: Reference the class instance itself
        :return: A session factory
        :doc-author: Trelent
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        self.__session.remove()