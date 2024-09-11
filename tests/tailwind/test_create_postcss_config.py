import unittest
from unittest import mock
from src.tailwind.postcss_config import create_postcss_config


class TestCreatePostCSSConfig(unittest.TestCase):

    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_create_postcss_config(self, mock_open):
        # Call the function
        create_postcss_config()

        # Define the expected content to be written to the file
        expected_content = """
export default {
plugins: {
tailwindcss: {},
autoprefixer: {},
},
}

"""

        # Check that open was called with the correct parameters
        mock_open.assert_called_once_with("postcss.config.js", "w")

        # Check that the file write method was called with the correct content
        mock_open().write.assert_called_once_with(expected_content)


if __name__ == "__main__":
    unittest.main()
