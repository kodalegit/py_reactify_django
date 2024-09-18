import unittest
import os
import tempfile
from unittest.mock import patch, mock_open
from src.reactify_django.bundler.babel_configurator import create_babel_config


class TestCreateBabelConfig(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.temp_dir)

    def tearDown(self):
        os.chdir(self.original_cwd)
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    def test_create_babel_config_without_typescript(self):
        create_babel_config()
        self.assertTrue(os.path.exists("babel.config.js"))
        with open("babel.config.js", "r") as f:
            content = f.read()
        self.assertNotIn("@babel/preset-typescript", content)

    def test_create_babel_config_with_typescript(self):
        create_babel_config(use_typescript=True)
        self.assertTrue(os.path.exists("babel.config.js"))
        with open("babel.config.js", "r") as f:
            content = f.read()
        self.assertIn("@babel/preset-typescript", content)

    @patch("os.access")
    def test_permission_error(self, mock_access):
        mock_access.return_value = False
        with self.assertRaises(PermissionError):
            create_babel_config()

    @patch("builtins.open", new_callable=mock_open)
    def test_io_error(self, mock_file):
        mock_file.side_effect = IOError("Mocked IOError")
        with self.assertRaises(OSError):
            create_babel_config()

    @patch("builtins.open", new_callable=mock_open)
    def test_unexpected_error(self, mock_file):
        mock_file.side_effect = Exception("Unexpected error")
        with self.assertRaises(Exception):
            create_babel_config()


if __name__ == "__main__":
    unittest.main()
