import unittest
from unittest.mock import patch, call
import subprocess
from src.django_configurator import configure_django


class TestConfigureDjango(unittest.TestCase):

    @patch("src.django_configurator.check_and_install_django")
    @patch("src.django_configurator.subprocess.run")
    @patch("src.django_configurator.os.chdir")
    @patch("src.django_configurator.add_app_django_settings")
    @patch("src.django_configurator.create_template_tag")
    @patch("src.django_configurator.create_gitignore")
    def test_configure_django_success(
        self,
        mock_create_gitignore,
        mock_create_template_tag,
        mock_add_app_django_settings,
        mock_chdir,
        mock_subprocess,
        mock_check_and_install_django,
    ):
        # Arrange
        mock_check_and_install_django.return_value = None
        mock_subprocess.return_value = None

        # Act
        configure_django("myproject", "myapp")

        # Assert
        mock_check_and_install_django.assert_called_once()
        mock_subprocess.assert_has_calls(
            [
                call(["django-admin", "startproject", "myproject"], check=True),
                call(["django-admin", "startapp", "myapp"], check=True),
            ]
        )
        mock_chdir.assert_called_once_with("myproject")
        mock_add_app_django_settings.assert_called_once_with("myproject", "myapp")
        mock_create_template_tag.assert_called_once_with("myapp")
        mock_create_gitignore.assert_called_once()

    @patch("src.django_configurator.check_and_install_django")
    @patch("src.django_configurator.subprocess.run")
    @patch("src.django_configurator.os.chdir")
    @patch("src.django_configurator.add_app_django_settings")
    @patch("src.django_configurator.create_template_tag")
    @patch("src.django_configurator.create_gitignore")
    def test_django_admin_not_found(
        self,
        mock_create_gitignore,
        mock_create_template_tag,
        mock_add_app_django_settings,
        mock_chdir,
        mock_subprocess,
        mock_check_and_install_django,
    ):
        mock_check_and_install_django.return_value = None
        mock_subprocess.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            configure_django("myproject", "myapp")

        mock_subprocess.assert_has_calls(
            [
                call(["django-admin", "startproject", "myproject"], check=True),
            ]
        )

    @patch("src.django_configurator.check_and_install_django")
    @patch("src.django_configurator.subprocess.run")
    @patch("src.django_configurator.os.chdir")
    @patch("src.django_configurator.add_app_django_settings")
    @patch("src.django_configurator.create_template_tag")
    @patch("src.django_configurator.create_gitignore")
    def test_subprocess_called_process_error(
        self,
        mock_create_gitignore,
        mock_create_template_tag,
        mock_add_app_django_settings,
        mock_chdir,
        mock_subprocess,
        mock_check_and_install_django,
    ):
        mock_check_and_install_django.return_value = None
        mock_subprocess.side_effect = subprocess.CalledProcessError(1, "command")

        with self.assertRaises(subprocess.CalledProcessError):
            configure_django("myproject", "myapp")

        mock_subprocess.assert_has_calls(
            [
                call(["django-admin", "startproject", "myproject"], check=True),
            ]
        )

    @patch("src.django_configurator.check_and_install_django")
    @patch("src.django_configurator.subprocess.run")
    @patch("src.django_configurator.os.chdir")
    @patch("src.django_configurator.add_app_django_settings")
    @patch("src.django_configurator.create_template_tag")
    @patch("src.django_configurator.create_gitignore")
    def test_permission_error(
        self,
        mock_create_gitignore,
        mock_create_template_tag,
        mock_add_app_django_settings,
        mock_chdir,
        mock_subprocess,
        mock_check_and_install_django,
    ):
        mock_check_and_install_django.return_value = None
        mock_subprocess.side_effect = subprocess.CalledProcessError(
            1, "permission denied"
        )

        with self.assertRaises(subprocess.CalledProcessError):
            configure_django("myproject", "myapp")

        mock_subprocess.assert_has_calls(
            [
                call(["django-admin", "startproject", "myproject"], check=True),
            ]
        )


if __name__ == "__main__":
    unittest.main()
