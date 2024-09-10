def create_gitignore():
    # Define the content of the .gitignore file
    gitignore_content = """# Python
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

    # Write the content to the .gitignore file
    with open(".gitignore", "w") as file:
        file.write(gitignore_content)
