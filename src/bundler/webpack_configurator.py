import os


def create_webpack_config(app_name, use_typescript):
    config = """
    const path = require('path');
    const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');
    const webpack = require('webpack');

    const isDevelopment = process.env.NODE_ENV !== 'production';

    module.exports = {{
        mode: isDevelopment ? 'development' : 'production',
        entry: './src/index.{}',  // Adjust entry point for TS/JS
        output: {{
            path: path.resolve(__dirname, '{}'),
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
                {}
            ],
        }},
        resolve: {{
            extensions: ['.js', '.jsx', '.json'{}],
        }},
        plugins: [
            isDevelopment && new webpack.HotModuleReplacementPlugin(),
            isDevelopment && new ReactRefreshWebpackPlugin(),
        ].filter(Boolean),
        devServer: {{
            static: {
                directory: path.join(__dirname, '{}'),
            },
            hot: true, // Enable hot module reloading
            port: 3000,
            compress: true,
            client: {
                logging: "error",
                overlay: true,
            },
            devMiddleware: {
                writeToDisk: true,
            }
        }},
    }};
    """.format(
        "tsx" if use_typescript else "jsx",
        f"static/{app_name}/js",
        (
            """
        {{
            test: /\.tsx?$/,
            use: 'ts-loader',
            exclude: /node_modules/,
        }},
        """
            if use_typescript
            else ""
        ),
        ", '.ts', '.tsx'" if use_typescript else "",
        f"static/{app_name}/js",
    )

    try:
        # Ensure the current directory exists and is writable
        if not os.access(os.getcwd(), os.W_OK):
            raise PermissionError("Write permission denied for the current directory.")

        # Write the Webpack config file
        with open("webpack.config.js", "w") as f:
            f.write(config)
        print("Successfully created webpack.config.js")

    except PermissionError as pe:
        print(f"Error: {pe}")
    except OSError as e:
        print(f"OS error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
