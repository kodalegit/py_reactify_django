import os


def create_webpack_config(typescript=False):
    config = """
    const path = require('path');
    const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');
    const webpack = require('webpack');

    const isDevelopment = process.env.NODE_ENV !== 'production';

    module.exports = {{
        mode: isDevelopment ? 'development' : 'production',
        entry: './src/index.{}',  // Adjust entry point for TS/JS
        output: {{
            path: path.resolve(__dirname, 'dist'),
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
                {}
            ],
        }},
        resolve: {{
            extensions: ['.js', '.jsx', '.json'{}], // Add .ts, .tsx for TypeScript
        }},
        plugins: [
            isDevelopment && new webpack.HotModuleReplacementPlugin(),
            isDevelopment && new ReactRefreshWebpackPlugin(),
        ].filter(Boolean),
        devServer: {{
            static: {
                directory: path.join(__dirname, 'dist'),
            },
            hot: true, // Enable hot module reloading
            port: 9000,
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
        "tsx" if typescript else "jsx",  # Adjust entry for TS or JS
        (
            """
        {{
            test: /\.tsx?$/,
            use: 'ts-loader',
            exclude: /node_modules/,
        }},
        """
            if typescript
            else ""
        ),
        ", '.ts', '.tsx'" if typescript else "",
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
