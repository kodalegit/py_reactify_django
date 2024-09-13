import unittest
from unittest.mock import mock_open, patch, call
import json
from src.bundler.update_package_json import update_package_json_scripts


class TestUpdatePackageJsonScripts(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    @patch("os.path.isfile", return_value=True)
    def test_update_package_json_scripts_success(self, mock_isfile, mock_open):
        # Simulate the package.json file being correctly updated
        update_package_json_scripts()

        # Check if the file was opened in write mode
        mock_open.assert_called_with("package.json", "w")

        # Define the expected series of write calls for the pretty-printed JSON
        expected_calls = [
            call("{"),
            call("\n  "),
            call('"scripts"'),
            call(": "),
            call("{"),
            call("\n    "),
            call('"start"'),
            call(": "),
            call('"webpack serve"'),
            call(",\n    "),
            call('"build"'),
            call(": "),
            call('"webpack --mode production"'),
            call("\n  "),
            call("}"),
            call("\n"),
            call("}"),
        ]
        mock_open().write.assert_has_calls(expected_calls, any_order=False)

    @patch("os.path.isfile", return_value=False)
    def test_file_not_found(self, mock_isfile):
        with self.assertRaises(FileNotFoundError):
            update_package_json_scripts()

    @patch("builtins.open", new_callable=mock_open, read_data="{invalid_json")
    @patch("os.path.isfile", return_value=True)
    def test_json_decode_error(self, mock_isfile, mock_open):
        with self.assertRaises(json.JSONDecodeError):
            update_package_json_scripts()

    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", side_effect=IOError("File I/O error"))
    def test_io_error(self, mock_open_side_effect, mock_isfile):
        with self.assertRaises(IOError):
            update_package_json_scripts()


if __name__ == "__main__":
    unittest.main()
