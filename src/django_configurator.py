import os
import subprocess
import sys
from .django.template_tag_creator import create_template_tag
from .django.modify_django_settings import add_app_django_settings
from .django.check_and_install_django import check_and_install_django


def configure_django(project_name, app_name):
    # Check if django exists and install if not
    check_and_install_django()

    try:
        # Create Django project
        subprocess.run(["django-admin", "startproject", project_name], check=True)
    except FileNotFoundError:
        # Handle "command not found" error
        print("Error: 'django-admin' command not found.")
        print("Ensure Django is installed and added to your system's PATH.")
        print("You can try running 'python -m django' instead.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        # Handle other errors in running django-admin (permissions, etc.)
        if "permission denied" in str(e):
            print("Error: Permission denied while trying to run 'django-admin'.")
            print("On macOS or Unix-based systems, you might need to run:")
            print("  sudo chmod +x $(which django-admin)")
        else:
            print(f"An error occurred while creating the Django project: {e}")
        sys.exit(1)

    # Navigate into the project directory
    os.chdir(project_name)

    try:
        # Create Django app
        subprocess.run(["django-admin", "startapp", app_name], check=True)
    except FileNotFoundError:
        print("Error: 'django-admin' command not found.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the Django app: {e}")
        sys.exit(1)

    # Modify Django settings to include app name
    add_app_django_settings(project_name, app_name)

    # Add custom react root template tag
    create_template_tag()
