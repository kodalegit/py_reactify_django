import typer
from rich.console import Console
from rich.panel import Panel
from tqdm import tqdm
import time
import questionary

from .django_configurator import configure_django
from .react_configurator import configure_react
from .bundler_configurator import configure_bundling
from .typescript_configurator import configure_typescript
from .tailwind_configurator import configure_tailwind
from .eslint_configurator import configure_eslint

app = typer.Typer()
console = Console()


def run_with_spinner(func, *args, **kwargs):
    try:
        with console.status("[bold green]Working...", spinner="dots") as status:
            result = func(*args, **kwargs)
            time.sleep(max(0, 1 - (time.time() - status.start_time)))
        return result
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        raise


@app.command()
def setup_django_react():
    console.print(Panel.fit("🚀 Setting up Django with React", style="bold magenta"))

    # Use questionary for interactive prompts
    project_name = questionary.text("Enter the Django project name:").ask() or "project"
    app_name = questionary.text("Enter the Django app name:").ask() or "app"
    use_typescript = questionary.confirm(
        "Do you want to use TypeScript for React?"
    ).ask()
    use_tailwind = questionary.confirm(
        "Do you want to use Tailwind CSS in your project?"
    ).ask()

    steps = [
        (
            "Configuring Django",
            lambda: configure_django(project_name, app_name, use_typescript),
        ),
        (
            "Setting up React",
            lambda: configure_react(app_name, use_typescript, use_tailwind),
        ),
        ("Configuring ESLint", lambda: configure_eslint(use_typescript)),
        ("Setting up bundling", lambda: configure_bundling(app_name, use_typescript)),
    ]

    if use_typescript:
        steps.append(
            ("Configuring TypeScript", lambda: configure_typescript(use_typescript))
        )

    if use_tailwind:
        steps.append(
            ("Setting up Tailwind CSS", lambda: configure_tailwind(use_typescript))
        )

    for step_name, step_func in tqdm(steps, desc="Overall Progress", color="green"):
        console.print(f"[bold blue]{step_name}[/bold blue]")
        run_with_spinner(step_func)

    console.print(
        Panel.fit(
            f"✅ Django project '{project_name}' configured with React and Webpack!",
            style="bold green",
        )
    )


if __name__ == "__main__":
    typer.run(setup_django_react)
