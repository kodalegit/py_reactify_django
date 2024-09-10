def create_tailwind_config(use_typescript):
    file_types = "ts,tsx" if use_typescript else "js,jsx"
    tailwind_config = f"""
    /** @type {{import('tailwindcss').Config}} */
    module.exports = {{
    content: ["./src/**/*.{{{file_types}}}"],
    theme: {{
        extend: {{}},
    }},
    plugins: [],
    }};
    """

    # Write the configuration to 'tailwind.config.js'
    with open("tailwind.config.js", "w") as file:
        file.write(tailwind_config)
