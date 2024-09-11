import unittest
from unittest import mock
from src.tailwind_configurator import configure_tailwind


class TestConfigureTailwind(unittest.TestCase):

    @mock.patch("src.tailwind_configurator.write_tailwind_css")
    @mock.patch("src.tailwind_configurator.create_postcss_config")
    @mock.patch("src.tailwind_configurator.create_tailwind_config")
    def test_configure_tailwind(
        self,
        mock_create_tailwind_config,
        mock_create_postcss_config,
        mock_write_tailwind_css,
    ):
        use_typescript = True  # or False, depending on what you want to test

        # Call the function
        configure_tailwind(use_typescript)

        # Check that create_tailwind_config is called with the correct argument
        mock_create_tailwind_config.assert_called_once_with(use_typescript)

        # Check that create_postcss_config is called once
        mock_create_postcss_config.assert_called_once()

        # Check that write_tailwind_css is called once
        mock_write_tailwind_css.assert_called_once()


if __name__ == "__main__":
    unittest.main()
