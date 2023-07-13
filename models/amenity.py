#!/usr/bin/python3
""" Class amenity module implementation."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity inheriting from Class BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization of the class."""
        super().__init__(*args, **kwargs)
