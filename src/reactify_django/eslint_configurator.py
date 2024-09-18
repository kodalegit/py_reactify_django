import json


def configure_eslint(use_typescript):
    eslint_config = {
        "env": {"browser": True, "es2020": True},
        "extends": ["eslint:recommended", "plugin:react/recommended"],
        "parserOptions": {
            "ecmaFeatures": {"jsx": True},
            "ecmaVersion": 12,
            "sourceType": "module",
        },
        "plugins": ["react"],
        "rules": {"react/prop-types": "off"},
    }

    if use_typescript:
        eslint_config["extends"].extend(["plugin:@typescript-eslint/recommended"])
        eslint_config["parser"] = "@typescript-eslint/parser"
        eslint_config["plugins"].append("@typescript-eslint")

    # Write ESLint configuration to .eslintrc.json
    with open(".eslintrc.json", "w") as f:
        json.dump(eslint_config, f, indent=2)

    # Create .eslintignore file
    eslintignore_content = """
node_modules/
build/
dist/
*.css
*.scss
"""
    with open(".eslintignore", "w") as f:
        f.write(eslintignore_content.strip())

    print("ESLint configured successfully.")
