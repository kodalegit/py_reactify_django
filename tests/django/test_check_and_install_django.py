import unittest
from unittest import mock
import subprocess
from src.reactify_django.django.check_and_install_django import check_and_install_django


class TestCheckAndInstallDjango(unittest.TestCase):

    @mock.patch("src.reactify_django.django.check_and_install_django.subprocess.run")
    def test_django_installed(self, mock_subprocess_run):
        # Simulate that Django is already installed
        mock_subprocess_run.return_value = mock.Mock(returncode=0)

        with mock.patch("builtins.print") as mocked_print:
            check_and_install_django()

            # Check that the correct message is printed when Django is installed
            mocked_print.assert_called_once_with("Django is already installed.")

    @mock.patch("src.reactify_django.django.check_and_install_django.subprocess.run")
    def test_django_not_installed(self, mock_subprocess_run):
        # Simulate that Django is not installed
        mock_subprocess_run.side_effect = [
            subprocess.CalledProcessError(1, "django"),
            None,
        ]

        with mock.patch("builtins.print") as mocked_print:
            check_and_install_django()

            # Check that the correct messages are printed when Django is not installed
            calls = [
                mock.call("Django is not installed. Installing Django..."),
                mock.call("Django has been installed successfully."),
            ]
            mocked_print.assert_has_calls(calls)


if __name__ == "__main__":
    unittest.main()
