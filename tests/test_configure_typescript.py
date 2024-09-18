import unittest
from unittest import mock
from src.reactify_django.typescript_configurator import configure_typescript


class TestConfigureTypescript(unittest.TestCase):

    @mock.patch("src.reactify_django.typescript_configurator.generate_tsconfig")
    def test_configure_typescript_called(self, mock_generate_tsconfig):
        # Test when use_typescript is True
        use_typescript = True

        # Call the function
        configure_typescript(use_typescript)

        # Check that generate_tsconfig is called once
        mock_generate_tsconfig.assert_called_once()

    @mock.patch("src.reactify_django.typescript_configurator.generate_tsconfig")
    def test_configure_typescript_not_called(self, mock_generate_tsconfig):
        # Test when use_typescript is False
        use_typescript = False

        # Call the function
        configure_typescript(use_typescript)

        # Check that generate_tsconfig is not called
        mock_generate_tsconfig.assert_not_called()


if __name__ == "__main__":
    unittest.main()
