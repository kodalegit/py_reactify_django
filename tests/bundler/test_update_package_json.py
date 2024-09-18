import unittest
from unittest.mock import mock_open, patch
import json
from src.reactify_django.bundler.update_package_json import update_package_json_scripts


class TestUpdatePackageJsonScripts(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"scripts": {}}')
    @patch("os.path.isfile", return_value=True)
    def test_successful_update(self, mock_isfile, mock_open_file):
        # Call the function
        update_package_json_scripts()

        # Expected data after the update
        expected_data = {
            "scripts": {
                "start": "webpack serve",
                "build": "webpack --mode production",
            }
        }
        expected_json = json.dumps(expected_data, indent=2)

        # Check that the file was opened twice (once for reading, once for writing)
        mock_open_file.assert_any_call("package.json", "r")
        mock_open_file.assert_any_call("package.json", "w")

        # Get the handle used for writing
        handle = mock_open_file()
        # Read all calls to the write method
        written_data = "".join(call[0][0] for call in handle.write.call_args_list)

        # Assert that the data written matches the expected JSON
        self.assertEqual(written_data, expected_json)

    @patch("os.path.isfile", return_value=False)
    def test_file_not_found(self, mock_isfile):
        # Ensure the function raises a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            update_package_json_scripts()

    @patch("builtins.open", new_callable=mock_open, read_data="invalid json")
    @patch("os.path.isfile", return_value=True)
    def test_json_decode_error(self, mock_isfile, mock_open_file):
        # Ensure the function raises a JSONDecodeError
        with self.assertRaises(json.JSONDecodeError):
            update_package_json_scripts()

    @patch("builtins.open", side_effect=IOError("IO error occurred"))
    @patch("os.path.isfile", return_value=True)
    def test_io_error(self, mock_isfile, mock_open_file):
        # Ensure the function raises an IOError
        with self.assertRaises(IOError):
            update_package_json_scripts()


if __name__ == "__main__":
    unittest.main()
