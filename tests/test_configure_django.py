import unittest
from unittest import mock
import subprocess
from src.django_configurator import configure_django


class TestConfigureDjango(unittest.TestCase):

    @mock.patch("src.django_configurator.subprocess.run")
    @mock.patch("src.django_configurator.os.chdir")
    @mock.patch("src.django_configurator.add_app_django_settings")
    @mock.patch("src.django_configurator.create_template_tag")
    @mock.patch("src.django_configurator.create_gitignore")
    @mock.patch("src.django_configurator.check_and_install_django")
    def test_configure_django(
        self,
        mock_check_and_install_django,
        mock_create_gitignore,
        mock_create_template_tag,
        mock_add_app_django_settings,
        mock_os_chdir,
        mock_subprocess_run,
    ):
        # Simulate a successful run for subprocess.run
        mock_subprocess_run.return_value = mock.Mock(returncode=0)

        # Call the function
        configure_django("test_project", "test_app")

        # Assert the Django installation check is called
        mock_check_and_install_django.assert_called_once()

        # Assert subprocess.run was called to create the Django project and app
        mock_subprocess_run.assert_any_call(
            ["django-admin", "startproject", "test_project"], check=True
        )
        mock_subprocess_run.assert_any_call(
            ["django-admin", "startapp", "test_app"], check=True
        )

        # Assert os.chdir was called to navigate into the project directory
        mock_os_chdir.assert_called_once_with("test_project")

        # Assert the settings and other functions were called
        mock_add_app_django_settings.assert_called_once_with("test_project", "test_app")
        mock_create_template_tag.assert_called_once()
        mock_create_gitignore.assert_called_once()

    # @mock.patch(
    #     "src.django_configurator.subprocess.run",
    #     side_effect=subprocess.CalledProcessError(1, "django-admin"),
    # )
    # def test_django_admin_not_found(self, mock_subprocess_run):
    #     # Test when 'django-admin' command is not found
    #     with self.assertRaises(SystemExit):  # Expect the function to call sys.exit
    #         configure_django("test_project", "test_app")

    # @mock.patch(
    #     "src.django_configurator.subprocess.run",
    #     side_effect=subprocess.CalledProcessError(1, "django-admin"),
    # )
    # def test_permission_denied(self, mock_subprocess_run):
    #     # Simulate subprocess.CalledProcessError with 'permission denied'
    #     error = subprocess.CalledProcessError(1, "django-admin")
    #     error.output = b"permission denied"
    #     mock_subprocess_run.side_effect = error

    #     # Test for permission denied error
    #     with self.assertRaises(SystemExit):  # Expect the function to call sys.exit
    #         configure_django("test_project", "test_app")


if __name__ == "__main__":
    unittest.main()
