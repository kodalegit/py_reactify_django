import unittest
from unittest import mock
import os
from src.django_configurator import add_app_django_settings


class TestAddAppDjangoSettings(unittest.TestCase):

    @mock.patch("os.path.isfile")
    @mock.patch(
        "builtins.open",
        new_callable=mock.mock_open,
        read_data="INSTALLED_APPS = [\n]\n",
    )
    def test_add_app_to_installed_apps(self, mock_open, mock_isfile):
        # Setup mocks
        mock_isfile.return_value = True

        # Call the function
        add_app_django_settings("test_project", "test_app")

        # Check that the file was opened for reading
        mock_open.assert_any_call(os.path.join("test_project", "settings.py"), "r")

        # Check that the file was opened for writing
        mock_open.assert_any_call(os.path.join("test_project", "settings.py"), "w")

        # Check that the correct content was written
        handle = mock_open()
        written_content = handle.write.call_args_list
        expected_content = [
            mock.call("INSTALLED_APPS = [\n"),
            mock.call("    'test_app',\n"),
            mock.call("]\n"),
        ]
        self.assertEqual(written_content, expected_content)

    @mock.patch("os.path.isfile")
    def test_file_not_found(self, mock_isfile):
        # Setup mock to simulate file not found
        mock_isfile.return_value = False

        # Check for FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            add_app_django_settings("test_project", "test_app")

    @mock.patch("os.path.isfile")
    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_io_error(self, mock_open, mock_isfile):
        # Setup mocks
        mock_isfile.return_value = True
        mock_open.side_effect = IOError("Mock IO Error")

        # Check for IOError
        with self.assertRaises(IOError):
            add_app_django_settings("test_project", "test_app")


if __name__ == "__main__":
    unittest.main()
