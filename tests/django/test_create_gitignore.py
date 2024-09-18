import unittest
from unittest import mock
from src.reactify_django.django.create_gitignore import create_gitignore


class TestCreateGitignore(unittest.TestCase):

    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_create_gitignore(self, mock_open):
        create_gitignore()

        # Define the expected content of the .gitignore file
        expected_content = """# Python
*.pyc
*.pyo
*.pyd
__pycache__/
*.db
*.sqlite3

# Django
*.log
local_settings.py
db.sqlite3
media/
staticfiles/

# React
node_modules/
dist/
*.log

# Environment variables
.env

# IDEs and Editors
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# OS-specific files
.DS_Store
Thumbs.db

# Python virtual environment
venv/
.env/
.venv/
.virtualenv/
"""

        # Verify that the open function was called with the correct parameters
        mock_open.assert_called_once_with(".gitignore", "w")

        # Retrieve the handle to the file
        handle = mock_open()

        # Verify that the correct content was written to the file
        handle.write.assert_called_once_with(expected_content)


if __name__ == "__main__":
    unittest.main()
