import os


def write_tailwind_css(app_name):
    # Define the Tailwind directives for the CSS file
    tailwind_css = """@tailwind base;
    @tailwind components;
    @tailwind utilities;
    """
    # Define the path where the styles.css file will be created
    static_dir = os.path.join("static", app_name)

    # Create the directory if it doesn't exist
    os.makedirs(static_dir, exist_ok=True)

    # Define the path to the styles.css file
    css_file_path = os.path.join(static_dir, "styles.css")

    # Write the Tailwind directives to the styles.css file
    with open(css_file_path, "w") as file:
        file.write(tailwind_css)
