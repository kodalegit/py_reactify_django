import unittest
from unittest import mock
from src.bundler_configurator import create_webpack_config


class TestCreateWebpackConfig(unittest.TestCase):

    @mock.patch("os.access")
    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_create_webpack_config(self, mock_open, mock_os_access):
        # Setup mocks
        mock_os_access.return_value = True  # Simulate that the directory is writable

        app_name = "test_app"
        use_typescript = True

        # Call the function
        create_webpack_config(app_name, use_typescript)

        # Check that the Webpack config file was opened for writing
        mock_open.assert_called_once_with("webpack.config.js", "w")

        # Get the file handle
        handle = mock_open()

        # Define the expected configuration
        expected_entry = "./src/index.tsx"
        expected_output_path = f"static/{app_name}/js"
        expected_loader = """
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
        """
        expected_extensions = ", '.ts', '.tsx'"
        expected_config = f"""\

    const path = require('path');
    const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');
    const webpack = require('webpack');

    const isDevelopment = process.env.NODE_ENV !== 'production';

    module.exports = {{
        mode: isDevelopment ? 'development' : 'production',
        entry: '{expected_entry}',  // Adjust entry point for TS/JS
        output: {{
            path: path.resolve(__dirname, '{expected_output_path}'),
            filename: 'bundle.js',
        }},
        module: {{
            rules: [
                {{
                    test: /\.(js|jsx)$/,
                    exclude: /node_modules/,
                    use: {{
                        loader: 'babel-loader',
                        options: {{
                            plugins: [
                                isDevelopment && require.resolve('react-refresh/babel')
                            ].filter(Boolean),
                        }},
                    }},
                }},
                {{
                    test: /\.css$/,  // Apply this rule to CSS files
                    use: [
                        'style-loader',  // Inject CSS into the DOM
                        'css-loader',    // Resolves @import and url() paths
                        'postcss-loader' // Process Tailwind and Autoprefixer via PostCSS
                    ],
                }},
                {expected_loader}
            ],
        }},
        resolve: {{
            extensions: ['.js', '.jsx', '.json'{expected_extensions}],
        }},
        plugins: [
            isDevelopment && new webpack.HotModuleReplacementPlugin(),
            isDevelopment && new ReactRefreshWebpackPlugin(),
        ].filter(Boolean),
        devServer: {{
            static: {{
                directory: path.join(__dirname, '{expected_output_path}'),
            }},
            hot: true, // Enable hot module reloading
            port: 3000,
            compress: true,
            client: {{
                logging: "error",
                overlay: true,
            }},
            devMiddleware: {{
                writeToDisk: true,
            }}
        }},
    }};
    """

        # Check that the correct content was written
        written_content = handle.write.call_args_list
        expected_content = [mock.call(expected_config)]
        self.assertEqual(written_content, expected_content)

    @mock.patch("os.access")
    def test_permission_error(self, mock_os_access):
        # Setup mocks to simulate permission error
        mock_os_access.return_value = False

        with self.assertRaises(PermissionError):
            create_webpack_config("test_app", True)

    @mock.patch("os.access", return_value=True)
    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_os_error(self, mock_open, mock_os_access):
        # Setup mock to raise an OSError
        mock_open.side_effect = OSError("Mock OS Error")

        with self.assertRaises(OSError):
            create_webpack_config("test_app", True)


if __name__ == "__main__":
    unittest.main()
