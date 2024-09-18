import unittest
from unittest import mock
from src.reactify_django.bundler_configurator import configure_bundling


class TestConfigureBundling(unittest.TestCase):

    @mock.patch("src.reactify_django.bundler_configurator.update_package_json_scripts")
    @mock.patch("src.reactify_django.bundler_configurator.create_babel_config")
    @mock.patch("src.reactify_django.bundler_configurator.create_webpack_config")
    def test_configure_bundling(
        self,
        mock_create_webpack_config,
        mock_create_babel_config,
        mock_update_package_json_scripts,
    ):
        # Test setup
        app_name = "test_app"
        use_typescript = True

        # Call the function
        configure_bundling(app_name, use_typescript)

        # Check that create_webpack_config was called with the correct arguments
        mock_create_webpack_config.assert_called_once_with(app_name, use_typescript)

        # Check that create_babel_config was called with the correct argument
        mock_create_babel_config.assert_called_once_with(use_typescript)

        # Check that update_package_json_scripts was called once
        mock_update_package_json_scripts.assert_called_once()


if __name__ == "__main__":
    unittest.main()
