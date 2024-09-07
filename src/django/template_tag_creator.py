import os


def create_template_tag():
    tag_code = """
    from django import template
    register = template.Library()

    @register.simple_tag
    def react_root():
        return '<div id="root"></div>'
    """
    tag_path = "your_app/templatetags/react_tags.py"
    os.makedirs(os.path.dirname(tag_path), exist_ok=True)
    with open(tag_path, "w") as tag_file:
        tag_file.write(tag_code)
