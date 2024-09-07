from .bundler.webpack_configurator import create_webpack_config
from .bundler.babel_configurator import create_babel_config
from .bundler.update_package_json import update_package_json_scripts


def configure_bundling(use_typescript):
    create_webpack_config(use_typescript)
    create_babel_config(use_typescript)
    update_package_json_scripts()
