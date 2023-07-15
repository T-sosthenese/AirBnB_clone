import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_save(self):
        base_model = BaseModel()
        previous_updated_at = base_model.updated_at
        base_model.save()
        current_updated_at = base_model.updated_at
        self.assertNotEqual(previous_updated_at, current_updated_at)

    def test_to_dict(self):
        base_model = BaseModel()
        base_model.name = "My First Model"
        base_model.my_number = 89

        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['name'], 'My First Model')
        self.assertEqual(base_model_dict['my_number'], 89)

    def test_str(self):
        base_model = BaseModel()
        string_representation = str(base_model)
        self.assertIn("[BaseModel]", string_representation)
        self.assertIn(base_model.id, string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)


if __name__ == '__main__':
    unittest.main()
