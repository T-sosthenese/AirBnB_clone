#!/usr/bin/python3
"""
This is the test suite for the console module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.user import User
from models.city import City
from models.state import State
from models.place import Place


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.console.storage.new(User())

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.assertFalse(self.console.emptyline())
        self.assertEqual(mock_stdout.getvalue(), '')

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.console.onecmd('quit'))
            self.assertEqual(mock_stdout.getvalue(), '')

    def test_create_command_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertFalse(self.console.onecmd('create'))
            self.assertIn("** class name missing **", mock_stdout.getvalue())

    def test_create_command_invalid_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd('create InvalidClass'))
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    def test_show_command_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertFalse(self.console.onecmd('show'))
            self.assertIn("** class name missing **", mock_stdout.getvalue())

    def test_show_command_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertFalse(self.console.onecmd('show InvalidClass'))
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('models.storage.all')
    def test_show__and_create_class(self, mock_storage_all):
        obj_id = 'test_id'
        mock_storage_all.return_value = {'User.{}'.format(obj_id): User()}
        with patch('uuid.uuid4', return_value=obj_id):
            self.assertTrue(self.console.onecmd('create User'))
            self.assertIn(
                    'User.{}'.format(obj_id), self.console.storage.all()
                    )

            mock_stdout = StringIO()

            self.assertTrue(
                    self.console.onecmd('show User {}'.format(obj_id))
                    )
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, str(User))

    def test_show_command_valid_class_with_user(self):
        user = User()
        self.console.storage.new(user)
        user_id = user.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertFalse(
                    self.console.onecmd('show User{}'.format(user_id))
                    )
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(user), output)


if __name__ == '__main__':
    unittest.main()
