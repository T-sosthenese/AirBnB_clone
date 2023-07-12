#!/usr/bin/python3
"""
Model for the state class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Class State that inherits from BaseModel Class."""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization of class State."""
        super().__init__(*args, **kwargs)
