import unittest
from unittest.mock import patch, mock_open
from src.eslint_configurator import configure_eslint


class TestConfigureEslint(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_configure_eslint_without_typescript(self, mock_json_dump, mock_file):
        configure_eslint(use_typescript=False)

        # Check if .eslintrc.json was created with correct content
        mock_file.assert_any_call(".eslintrc.json", "w")
        calls = mock_json_dump.call_args_list
        self.assertEqual(len(calls), 1)

        eslint_config = calls[0][0][0]  # First argument of the first call
        self.assertIn("eslint:recommended", eslint_config["extends"])
        self.assertIn("plugin:react/recommended", eslint_config["extends"])
        self.assertNotIn(
            "plugin:@typescript-eslint/recommended", eslint_config["extends"]
        )
        self.assertNotIn("@typescript-eslint/parser", eslint_config)
        self.assertNotIn("@typescript-eslint", eslint_config["plugins"])

        # Check if .eslintignore was created with correct content
        mock_file.assert_any_call(".eslintignore", "w")
        handle = mock_file()
        handle.write.assert_called_once_with(
            "node_modules/\nbuild/\ndist/\n*.css\n*.scss"
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_configure_eslint_with_typescript(self, mock_json_dump, mock_file):
        configure_eslint(use_typescript=True)

        # Check if .eslintrc.json was created with correct content
        mock_file.assert_any_call(".eslintrc.json", "w")
        calls = mock_json_dump.call_args_list
        self.assertEqual(len(calls), 1)

        eslint_config = calls[0][0][0]  # First argument of the first call
        self.assertIn("eslint:recommended", eslint_config["extends"])
        self.assertIn("plugin:react/recommended", eslint_config["extends"])
        self.assertIn("plugin:@typescript-eslint/recommended", eslint_config["extends"])
        self.assertEqual(eslint_config["parser"], "@typescript-eslint/parser")
        self.assertIn("@typescript-eslint", eslint_config["plugins"])

        # Check if .eslintignore was created with correct content
        mock_file.assert_any_call(".eslintignore", "w")
        handle = mock_file()
        handle.write.assert_called_once_with(
            "node_modules/\nbuild/\ndist/\n*.css\n*.scss"
        )


if __name__ == "__main__":
    unittest.main()
