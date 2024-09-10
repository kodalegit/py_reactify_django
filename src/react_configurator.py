import os
from .react.install_npm_packages import install_npm_packages


def configure_react(app_name, use_typescript, use_tailwind):
    # Navigate to app directory
    os.chdir(app_name)

    # Initialize npm and install packages
    install_npm_packages(use_typescript, use_tailwind)

    # Create React entry point
    os.makedirs("src", exist_ok=True)
    entry_file = "index.tsx" if use_typescript else "index.jsx"
    with open(f"src/{entry_file}", "w") as f:
        f.write(
            "import React from 'react';\nimport ReactDOM from 'react-dom';\nimport './index.css';\nReactDOM.render(<h1>Hello, React!</h1>, document.getElementById('root'));"
        )
