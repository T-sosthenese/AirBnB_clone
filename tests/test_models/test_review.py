#!/usr/bin/python3
"""
This is the Test Suite for the review class of the model
"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_inheritance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
