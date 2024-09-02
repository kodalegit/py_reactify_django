import click
import subprocess
import os
from .django_configurator import configure_django_react_project


@click.command()
@click.option(
    "--project-name",
    prompt="Enter the Django project name",
    help="The name of the Django project.",
)
@click.option(
    "--app-name",
    prompt="Enter the Django app name",
    help="The name of the Django app where React will be installed.",
)
@click.option(
    "--typescript",
    is_flag=True,
    help="Use TypeScript for React (default is JavaScript).",
)
def setup_django_react(project_name, app_name, use_typescript):
    configure_django_react_project(project_name, app_name, use_typescript)
    print(f"Django project '{project_name}' configured with React and Webpack.")


if __name__ == "__main__":
    setup_django_react()
