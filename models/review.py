#!/usr/bin/python3
""" Class Review module implementation."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review inheriting from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
