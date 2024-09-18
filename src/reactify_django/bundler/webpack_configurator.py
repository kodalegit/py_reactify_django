import os


def create_webpack_config(app_name, use_typescript):
    config = """\
const path = require('path');
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');
const webpack = require('webpack');

const isDevelopment = process.env.NODE_ENV !== 'production';

module.exports = {{
    mode: isDevelopment ? 'development' : 'production',
    entry: './src/index.{entry_ext}',  // Adjust entry point for TS/JS
    output: {{
        path: path.resolve(__dirname, '{output_path}'),
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
            {typescript_loader}
        ],
    }},
    resolve: {{
        extensions: ['.js', '.jsx', '.json'{extensions}],
    }},
    plugins: [
        isDevelopment && new webpack.HotModuleReplacementPlugin(),
        isDevelopment && new ReactRefreshWebpackPlugin(),
    ].filter(Boolean),
    devServer: {{
        static: {{
            directory: path.join(__dirname, '{output_path}'),
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
""".format(
        entry_ext="tsx" if use_typescript else "jsx",
        output_path=f"static/{app_name}/js",
        typescript_loader=(
            """\
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
            """
            if use_typescript
            else ""
        ),
        extensions=", '.ts', '.tsx'" if use_typescript else "",
    )

    try:
        # Ensure the current directory exists and is writable
        if not os.access(os.getcwd(), os.W_OK):
            raise PermissionError("Write permission denied for the current directory.")

        # Write the Webpack config file
        with open("webpack.config.js", "w") as f:
            f.write(config)
        print("Successfully created webpack.config.js")

    except (PermissionError, OSError) as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
