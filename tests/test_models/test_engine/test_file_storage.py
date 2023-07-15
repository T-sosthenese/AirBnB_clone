#!/usr/bin/python3
"""
This is the test suite for the FileStorage class of the model
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 0)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, all_objects)

    def test_save(self):
        all_objects = self.storage.all()
        initial_length = len(all_objects)

        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), initial_length + 1)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, all_objects)

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, all_objects)

    def test_reload_file_not_found(self):
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 0)
        self.assertEqual(FileStorage.__FileStorage__objects, {})


if __name__ == '__main__':
    unittest.main()
