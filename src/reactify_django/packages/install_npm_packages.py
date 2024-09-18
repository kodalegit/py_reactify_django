import subprocess


def install_npm_packages(use_typescript, use_tailwind):
    try:
        # Initialize npm in the app directory
        subprocess.run(["npm", "init", "-y"], check=True)

        # Regular dependencies
        dependencies = [
            "react",
            "react-dom",
        ]

        # Dev dependencies
        dev_dependencies = [
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
        ]

        # If TypeScript is used, add TypeScript-related packages
        if use_typescript:
            dev_dependencies.extend(
                [
                    "typescript",
                    "@types/react",
                    "@types/react-dom",
                    "ts-loader",
                    "@babel/preset-typescript",
                    "@typescript-eslint/eslint-plugin",
                    "@typescript-eslint/parser",
                ]
            )
        if use_tailwind:
            dev_dependencies.extend(["tailwindcss", "postcss", "autoprefixer"])

        # Install regular dependencies
        subprocess.run(["npm", "install"] + dependencies, check=True)

        # Install dev dependencies
        subprocess.run(["npm", "install", "--save-dev"] + dev_dependencies, check=True)

        print("NPM packages installed successfully.")

    except subprocess.CalledProcessError as e:
        print(
            f"An error occurred while installing npm packages: {e}. Make sure Node is installed and try again."
        )
        raise
