#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        storage.reset()

    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_id = mock_stdout.getvalue().strip()
            self.assertIsNotNone(storage.all().get(f"BaseModel.{created_id}"))

    def test_show_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"show BaseModel {created_id}")
            output = mock_stdout.getvalue().strip()
            self.assertIn(created_id, output)

    def test_destroy_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {created_id}")
            self.assertIsNone(storage.all().get(f"BaseModel.{created_id}"))

    def test_all_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertIn("User", output)

    def test_count_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("count BaseModel")
            count_output = int(mock_stdout.getvalue().strip())
            self.assertEqual(count_output, 2)

    def test_update_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"update BaseModel {created_id} name 'new_name'")
            obj = storage.all().get(f"BaseModel.{created_id}")
            self.assertEqual(obj.name, 'new_name')

    def test_quit_command(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF_command(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_emptyline_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("\n")
            self.assertEqual(mock_stdout.getvalue(), '')

if __name__ == '__main__':
    unittest.main()
