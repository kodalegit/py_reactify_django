import unittest
import os
import tempfile
from unittest.mock import patch
from io import StringIO
from src.reactify_django.bundler.webpack_configurator import create_webpack_config


class TestCreateWebpackConfig(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Clean up the temporary directory
        os.chdir(os.path.dirname(self.test_dir))
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_create_webpack_config_js(self):
        create_webpack_config("test_app", use_typescript=False)
        self.assertTrue(os.path.exists("webpack.config.js"))
        with open("webpack.config.js", "r") as f:
            content = f.read()
            self.assertIn("entry: './src/index.jsx'", content)
            self.assertIn("static/test_app/js", content)
            self.assertNotIn("test: /\.tsx?$/", content)
            self.assertNotIn("'.ts', '.tsx'", content)

    def test_create_webpack_config_ts(self):
        create_webpack_config("test_app", use_typescript=True)
        self.assertTrue(os.path.exists("webpack.config.js"))
        with open("webpack.config.js", "r") as f:
            content = f.read()
            self.assertIn("entry: './src/index.tsx'", content)
            self.assertIn("static/test_app/js", content)
            self.assertIn("test: /\.tsx?$/", content)
            self.assertIn("'.ts', '.tsx'", content)

    @patch("sys.stdout", new_callable=StringIO)
    def test_successful_creation_message(self, mock_stdout):
        create_webpack_config("test_app", use_typescript=False)
        self.assertEqual(
            mock_stdout.getvalue().strip(), "Successfully created webpack.config.js"
        )

    @patch("os.access")
    def test_permission_error(self, mock_access):
        mock_access.return_value = False
        with self.assertRaises(PermissionError):
            create_webpack_config("test_app", use_typescript=False)

    @patch("builtins.open")
    def test_unexpected_error(self, mock_open):
        mock_open.side_effect = Exception("Unexpected error")
        with self.assertRaises(Exception):
            create_webpack_config("test_app", use_typescript=False)


if __name__ == "__main__":
    unittest.main()
