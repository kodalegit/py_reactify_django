import unittest
from unittest.mock import patch, call
from src.packages.install_npm_packages import install_npm_packages
import subprocess


class TestInstallNpmPackages(unittest.TestCase):

    @patch("subprocess.run")
    def test_install_npm_packages_typescript_tailwind(self, mock_run):
        install_npm_packages(use_typescript=True, use_tailwind=True)

        expected_calls = [
            call(["npm", "init", "-y"], check=True),
            call(["npm", "install", "react", "react-dom"], check=True),
            call(
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
                    "eslint",
                    "eslint-plugin-react",
                    "typescript",
                    "@types/react",
                    "@types/react-dom",
                    "ts-loader",
                    "@babel/preset-typescript",
                    "@typescript-eslint/eslint-plugin",
                    "@typescript-eslint/parser",
                    "tailwindcss",
                    "postcss",
                    "autoprefixer",
                ],
                check=True,
            ),
        ]

        mock_run.assert_has_calls(expected_calls, any_order=False)
        self.assertEqual(mock_run.call_count, 3)

    @patch("subprocess.run")
    def test_install_npm_packages_no_typescript_no_tailwind(self, mock_run):
        install_npm_packages(use_typescript=False, use_tailwind=False)

        expected_calls = [
            call(["npm", "init", "-y"], check=True),
            call(["npm", "install", "react", "react-dom"], check=True),
            call(
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
                    "eslint",
                    "eslint-plugin-react",
                ],
                check=True,
            ),
        ]

        mock_run.assert_has_calls(expected_calls, any_order=False)
        self.assertEqual(mock_run.call_count, 3)

    @patch("subprocess.run")
    def test_install_npm_packages_error(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, "npm install")

        with self.assertRaises(subprocess.CalledProcessError):
            install_npm_packages(use_typescript=False, use_tailwind=False)


if __name__ == "__main__":
    unittest.main()
