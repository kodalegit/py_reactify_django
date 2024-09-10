def create_postcss_config():
    postcss_config = """
    export default {
    plugins: {
    tailwindcss: {},
    autoprefixer: {},
    },
    }

    """

    with open("postcss.config.js", "w") as f:
        f.write(postcss_config)
