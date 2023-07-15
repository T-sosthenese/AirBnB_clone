#!/usr/bin/python3
"""
This is the Test suite for the State class of the model
"""


import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")
