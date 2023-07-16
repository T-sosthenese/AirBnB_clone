#!/usr/bin/python3
"""
This is the test suite for the console module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        console = HBNBCommand()
        self.assertFalse(console.emptyline())
        self.assertEqual(mock_stdout.getvalue(), '')

    def test_quit_command(self):
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(console.onecmd('quit'))
            self.assertEqual(mock_stdout.getvalue(), '')

    def test_create_command(self):
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertFalse(console.onecmd('create'))
            self.assertIn("** class name missing **", mock_stdout.getvalue())

    def test_show_command(self):
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertFalse(console.onecmd('show'))
            self.assertIn("** class name missing **", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
