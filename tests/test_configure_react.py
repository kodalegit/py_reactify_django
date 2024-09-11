import unittest
from unittest import mock
import os
from src.react_configurator import configure_react


class TestConfigureReact(unittest.TestCase):

    @mock.patch("src.react_configurator.install_npm_packages")
    @mock.patch("os.makedirs")
    @mock.patch("builtins.open", new_callable=mock.mock_open)
    @mock.patch("os.chdir")
    def test_configure_react_javascript(
        self, mock_chdir, mock_open, mock_makedirs, mock_install_npm_packages
    ):
        # Test configuration for JavaScript (not TypeScript)
        app_name = "test_app"
        use_typescript = False
        use_tailwind = False

        # Call the function
        configure_react(app_name, use_typescript, use_tailwind)

        # Check that os.chdir was called with the correct app_name
        mock_chdir.assert_called_once_with(app_name)

        # Check that npm packages were installed
        mock_install_npm_packages.assert_called_once_with(use_typescript, use_tailwind)

        # Check that os.makedirs was called for the src directory
        mock_makedirs.assert_called_once_with("src", exist_ok=True)

        # Check that the entry point file (index.jsx) was created
        mock_open.assert_called_once_with("src/index.jsx", "w")
        mock_open().write.assert_called_once_with(
            "import React from 'react';\nimport ReactDOM from 'react-dom';\nimport './index.css';\nReactDOM.render(<h1>Hello, React!</h1>, document.getElementById('root'));"
        )

    @mock.patch("src.react_configurator.install_npm_packages")
    @mock.patch("os.makedirs")
    @mock.patch("builtins.open", new_callable=mock.mock_open)
    @mock.patch("os.chdir")
    def test_configure_react_typescript(
        self, mock_chdir, mock_open, mock_makedirs, mock_install_npm_packages
    ):
        # Test configuration for TypeScript
        app_name = "test_app"
        use_typescript = True
        use_tailwind = True

        # Call the function
        configure_react(app_name, use_typescript, use_tailwind)

        # Check that os.chdir was called with the correct app_name
        mock_chdir.assert_called_once_with(app_name)

        # Check that npm packages were installed
        mock_install_npm_packages.assert_called_once_with(use_typescript, use_tailwind)

        # Check that os.makedirs was called for the src directory
        mock_makedirs.assert_called_once_with("src", exist_ok=True)

        # Check that the entry point file (index.tsx) was created
        mock_open.assert_called_once_with("src/index.tsx", "w")
        mock_open().write.assert_called_once_with(
            "import React from 'react';\nimport ReactDOM from 'react-dom';\nimport './index.css';\nReactDOM.render(<h1>Hello, React!</h1>, document.getElementById('root'));"
        )


if __name__ == "__main__":
    unittest.main()
