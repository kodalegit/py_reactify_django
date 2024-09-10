import click
from .django_configurator import configure_django
from .react_configurator import configure_react
from .bundler_configurator import configure_bundling
from .typescript_configurator import configure_typescript
from .tailwind_configurator import configure_tailwind


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
@click.option(
    "--tailwind",
    is_flag=True,
    help="Use Tailwind CSS in your project.",
)
def setup_django_react(project_name, app_name, use_typescript, use_tailwind):
    configure_django(project_name, app_name, use_typescript)
    configure_react(app_name, use_typescript, use_tailwind)
    configure_bundling(use_typescript)
    configure_typescript(use_typescript)

    if use_tailwind:
        configure_tailwind(use_typescript, app_name)

    print(f"Django project '{project_name}' configured with React and Webpack.")


if __name__ == "__main__":
    setup_django_react()
