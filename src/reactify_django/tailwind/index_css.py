import os


def write_tailwind_css():
    # Define the Tailwind directives for the CSS file
    tailwind_css = """@tailwind base;
@tailwind components;
@tailwind utilities;
"""

    # Path to index css file
    css_file_path = os.path.join("src", "index.css")

    # Write the Tailwind directives to the styles.css file
    with open(css_file_path, "w") as file:
        file.write(tailwind_css)
