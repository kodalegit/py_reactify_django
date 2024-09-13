import unittest
from unittest.mock import mock_open, patch
from src.bundler.babel_configurator import create_babel_config


class TestCreateBabelConfig(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.access", return_value=True)  # Simulate writable directory
    def test_create_babel_config_with_typescript(self, mock_access, mock_open):
        # Call the function with TypeScript enabled
        create_babel_config(use_typescript=True)

        # Check if the file was opened in write mode
        mock_open.assert_called_with("babel.config.js", "w")

        # Check if the file content written matches the expected Babel config with TypeScript
        expected_config = """\
module.exports = (api) => {
  // This caches the Babel config
  api.cache.using(() => process.env.NODE_ENV);

  const isProduction = api.env("production");

  return {
    presets: [
      "@babel/preset-env",
      // Enable development transform of React with new automatic runtime
      [
        "@babel/preset-react",
        { development: !isProduction, runtime: "automatic" },
      ],
      "@babel/preset-typescript",
    ],
  };
};
"""
        mock_open().write.assert_called_once_with(expected_config)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.access", return_value=True)  # Simulate writable directory
    def test_create_babel_config_without_typescript(self, mock_access, mock_open):
        # Call the function with TypeScript disabled
        create_babel_config(use_typescript=False)

        # Check if the file was opened in write mode
        mock_open.assert_called_with("babel.config.js", "w")

        # Check if the file content written matches the expected Babel config without TypeScript
        expected_config = """\
module.exports = (api) => {
  // This caches the Babel config
  api.cache.using(() => process.env.NODE_ENV);

  const isProduction = api.env("production");

  return {
    presets: [
      "@babel/preset-env",
      // Enable development transform of React with new automatic runtime
      [
        "@babel/preset-react",
        { development: !isProduction, runtime: "automatic" },
      ],
      
    ],
  };
};
"""
        mock_open().write.assert_called_once_with(expected_config)

    @patch("os.access", return_value=False)  # Simulate non-writable directory
    def test_permission_error(self, mock_access):
        with self.assertRaises(PermissionError):
            create_babel_config()

    @patch("os.access", return_value=True)  # Simulate writable directory
    @patch("builtins.open", side_effect=OSError("OS error"))
    def test_os_error(self, mock_access, mock_open_side_effect):
        with self.assertRaises(OSError):
            create_babel_config()


if __name__ == "__main__":
    unittest.main()
