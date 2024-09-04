import os
from .install_npm_packages import install_npm_packages
from .webpack_configurator import create_webpack_config


def configure_react(app_name, use_typescript):
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
