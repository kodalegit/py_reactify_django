import unittest
from unittest import mock
import subprocess
from src.react_configurator import install_npm_packages


class TestInstallNpmPackages(unittest.TestCase):

    @mock.patch("subprocess.run")
    def test_install_npm_packages(self, mock_subprocess_run):
        # Setup mocks
        mock_subprocess_run.return_value = mock.Mock(returncode=0)

        # Call the function with use_typescript and use_tailwind set to True
        install_npm_packages(use_typescript=True, use_tailwind=True)

        # Check that subprocess.run was called with the correct commands
        calls = [
            mock.call(["npm", "init", "-y"], check=True),
            mock.call(["npm", "install", "react", "react-dom"], check=True),
            mock.call(
                [
                    "npm",
                    "install",
                    "--save-dev",
                    "webpack",
                    "webpack-cli",
                    "webpack-dev-server",
                    "babel-loader",
                    "@babel/core",
                    "@babel/preset-env",
                    "@babel/preset-react",
                    "@pmmmwh/react-refresh-webpack-plugin",
                    "react-refresh",
                    "style-loader",
                    "css-loader",
                    "postcss-loader",
                    "typescript",
                    "@types/react",
                    "@types/react-dom",
                    "ts-loader",
                    "@babel/preset-typescript",
                    "tailwindcss",
                    "postcss",
                    "autoprefixer",
                ],
                check=True,
            ),
        ]

        mock_subprocess_run.assert_has_calls(calls)

    @mock.patch("subprocess.run")
    def test_install_npm_packages_failure(self, mock_subprocess_run):
        mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, "npm")

        # Test the case where subprocess.run raises CalledProcessError
        with self.assertRaises(subprocess.CalledProcessError):
            install_npm_packages(use_typescript=False, use_tailwind=False)

    @mock.patch("subprocess.run")
    def test_install_npm_packages_without_typescript_or_tailwind(
        self, mock_subprocess_run
    ):
        # Setup mocks
        mock_subprocess_run.return_value = mock.Mock(returncode=0)

        # Call the function with use_typescript and use_tailwind set to False
        install_npm_packages(use_typescript=False, use_tailwind=False)

        # Check that subprocess.run was called with the correct commands
        calls = [
            mock.call(["npm", "init", "-y"], check=True),
            mock.call(["npm", "install", "react", "react-dom"], check=True),
            mock.call(
                [
                    "npm",
                    "install",
                    "--save-dev",
                    "webpack",
                    "webpack-cli",
                    "webpack-dev-server",
                    "babel-loader",
                    "@babel/core",
                    "@babel/preset-env",
                    "@babel/preset-react",
                    "@pmmmwh/react-refresh-webpack-plugin",
                    "react-refresh",
                    "style-loader",
                    "css-loader",
                    "postcss-loader",
                ],
                check=True,
            ),
        ]

        mock_subprocess_run.assert_has_calls(calls)


if __name__ == "__main__":
    unittest.main()
