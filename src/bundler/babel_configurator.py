import os


def create_babel_config(use_typescript=False):
    # Babel config template
    config = """\
module.exports = (api) => {{
  // This caches the Babel config
  api.cache.using(() => process.env.NODE_ENV);

  const isProduction = api.env("production");

  return {{
    presets: [
      "@babel/preset-env",
      // Enable development transform of React with new automatic runtime
      [
        "@babel/preset-react",
        {{ development: !isProduction, runtime: "automatic" }},
      ],
      {}
    ],
  }};
}};
""".format(
        # Conditionally add the TypeScript preset if use_typescript is True
        '"@babel/preset-typescript",'
        if use_typescript
        else ""
    )

    try:
        # Ensure the current directory exists and is writable
        if not os.access(os.getcwd(), os.W_OK):
            raise PermissionError("Write permission denied for the current directory.")

        # Write the Babel configuration to babel.config.js
        with open("babel.config.js", "w") as f:
            f.write(config)
        print("Successfully created babel.config.js")

    except (PermissionError, OSError) as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
