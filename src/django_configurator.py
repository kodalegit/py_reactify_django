import os
import subprocess
from .install_npm_packages import install_npm_packages
from .webpack_configurator import create_webpack_config
from .template_tag_creator import create_template_tag


def configure_django_react_project(project_name, app_name, use_typescript=False):
    # Create Django project
    subprocess.run(["django-admin", "startproject", project_name])

    # Navigate into the project directory
    os.chdir(project_name)

    # Create the Django app
    subprocess.run(["python", "manage.py", "startapp", app_name])

    # Navigate to app directory
    os.chdir(app_name)

    # Initialize npm and install packages
    install_npm_packages(use_typescript)

    # Create Webpack configuration
    create_webpack_config(typescript=use_typescript)

    # Create React entry point
    os.makedirs("src", exist_ok=True)
    entry_file = "index.tsx" if use_typescript else "index.jsx"
    with open(f"src/{entry_file}", "w") as f:
        f.write(
            "import React from 'react';\nimport ReactDOM from 'react-dom';\nReactDOM.render(<h1>Hello, React!</h1>, document.getElementById('root'));"
        )

    # Modify Django settings and templates if needed
    # Add custom react root template tag
    create_template_tag()


if __name__ == "__main__":
    configure_django_react_project("myproject", use_typescript=True)
