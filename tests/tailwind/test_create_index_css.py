import unittest
from unittest import mock
import os
from src.tailwind.index_css import write_tailwind_css


class TestWriteTailwindCSS(unittest.TestCase):

    @mock.patch("builtins.open", new_callable=mock.mock_open)
    @mock.patch(
        "os.path.join", return_value="src/index.css"
    )  # Mock os.path.join to avoid path issues
    def test_write_tailwind_css(self, mock_path_join, mock_open):
        # Call the function
        write_tailwind_css()

        # Define the expected content to be written to the file
        expected_content = """@tailwind base;
@tailwind components;
@tailwind utilities;
"""

        # Check that open was called with the correct parameters
        mock_open.assert_called_once_with("src/index.css", "w")

        # Check that the file write method was called with the correct content
        mock_open().write.assert_called_once_with(expected_content)


if __name__ == "__main__":
    unittest.main()
