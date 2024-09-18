import unittest
from unittest import mock
from src.reactify_django.tailwind.tailwind_config import create_tailwind_config


class TestCreateTailwindConfig(unittest.TestCase):

    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_create_tailwind_config_with_typescript(self, mock_open):
        # Test with TypeScript enabled
        create_tailwind_config(use_typescript=True)

        expected_content = """\
/** @type {import('tailwindcss').Config} */
module.exports = {
content: ["./src/**/*.{ts,tsx}"],
theme: {
    extend: {},
},
plugins: [],
};
"""
        # Check that open was called with the correct parameters
        mock_open.assert_called_once_with("tailwind.config.js", "w")

        # Check that the file write method was called with the correct content
        mock_open().write.assert_called_once_with(expected_content)

    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_create_tailwind_config_without_typescript(self, mock_open):
        # Test with TypeScript disabled
        create_tailwind_config(use_typescript=False)

        expected_content = """\
/** @type {import('tailwindcss').Config} */
module.exports = {
content: ["./src/**/*.{js,jsx}"],
theme: {
    extend: {},
},
plugins: [],
};
"""
        # Check that open was called with the correct parameters
        mock_open.assert_called_once_with("tailwind.config.js", "w")

        # Check that the file write method was called with the correct content
        mock_open().write.assert_called_once_with(expected_content)


if __name__ == "__main__":
    unittest.main()
