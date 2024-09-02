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

    with open("webpack.config.js", "w") as f:
        f.write(config)


if __name__ == "__main__":
    create_webpack_config(typescript=True)
