from .tailwind.postcss_config import create_postcss_config
from .tailwind.tailwind_config import create_tailwind_config
from .tailwind.styles_css import write_tailwind_css


def configure_tailwind(use_typescript, app_name):
    create_tailwind_config(use_typescript)
    create_postcss_config()
    write_tailwind_css(app_name)

    print(
        f"Tailwind CSS has been configured with {'TypeScript' if use_typescript else 'JavaScript'} support."
    )
