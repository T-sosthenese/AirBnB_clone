#!/usr/bin/python3
""" Class City module implementation """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City which inherits from class BaseModel."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization of instance attributes """
        super().__init__(*args, **kwargs)
