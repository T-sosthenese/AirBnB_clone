#!/usr/bin/python3
"""
This is the suite for City class of the module; City module
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
