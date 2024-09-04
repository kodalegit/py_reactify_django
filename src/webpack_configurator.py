import os


def create_webpack_config(typescript=False):
    config = """
    const path = require('path');

    module.exports = {{
        entry: './src/index.{}',
        output: {{
            path: path.resolve(__dirname, 'dist'),
            filename: 'bundle.js',
        }},
        module: {{
            rules: [
                {{
                    test: /\.(js|jsx)$/,
                    exclude: /node_modules/,
                    use: ['babel-loader'],
                }},
                {}
            ],
        }},
        resolve: {{
            extensions: ['.js', '.jsx', '.json'],
        }},
        devServer: {{
            contentBase: path.join(__dirname, 'dist'),
            compress: true,
            port: 9000,
        }},
    }};
    """.format(
        "tsx" if typescript else "jsx",
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
