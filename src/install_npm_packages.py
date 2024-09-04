import subprocess


def install_npm_packages(use_typescript):
    try:
        # Initialize npm in the app directory
        subprocess.run(["npm", "init", "-y"], check=True)

        # Install React and Webpack with optional TypeScript
        packages = [
            "react",
            "react-dom",
            "webpack",
            "webpack-cli",
            "webpack-dev-server",
            "babel-loader",
            "@babel/core",
            "@babel/preset-env",
            "@babel/preset-react",
        ]
        if use_typescript:
            packages.extend(
                [
                    "typescript",
                    "@types/react",
                    "@types/react-dom",
                    "ts-loader",
                    "@babel/preset-typescript",
                ]
            )

        subprocess.run(["npm", "install"] + packages, check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred installing npm packages: {e}")
