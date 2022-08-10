#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, storageType
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models

if storageType == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
    A place to stay
    """
    if storageType == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            backref="place_amenities",
            viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            The reviews function is a helper function that returns all the reviews of a place

            :param self: Access variables that belongs to the class
            :return: The number of reviews for a given movie
            :doc-author: Trelent
            """

            return [review for review in models.storage.all(Review).value() if review.place_id == self.id]

        @property
        def amenities(self):
            """
            The amenities function is a method that returns the amenities of each place.
            It is called in the Place class and takes self as an argument. It then uses 
            the relationship to call on all of the amenities for each place.

            :param self: Access variables that belongs to the class
            :return: A dictionary of the amenities that are available at a given listing
            :doc-author: Trelent
            """

            return [amenities for amenities in models.storage.all(Amenity).values() if amenities.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """
            The amenities function is a helper function that returns the amenities of
            a given place. It is used in the Place class.

            :param self: Access variables that belong to the class
            :param obj: Access the amenity object
            :return: The amenities of the object
            :doc-author: Trelent
            """

            if type(obj) == Amenity:
                self.amenities_ids.append(obj.id)