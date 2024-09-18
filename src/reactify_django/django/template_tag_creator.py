import os


def create_template_tag(app_name):
    tag_code = f"""
from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def react_root():
    # Create the URL for the React bundled script using Django's static tag
    script_url = static('{app_name}/js/bundle.js')
    return f'''
<div id="root"></div>
<script src="{{{{ script_url }}}}"></script>
'''
"""

    tag_path = f"{app_name}/templatetags/react_root.py"
    os.makedirs(os.path.dirname(tag_path), exist_ok=True)
    with open(tag_path, "w") as tag_file:
        tag_file.write(tag_code)

    init_path = os.path.join(app_name, "templatetags", "__init__.py")
    with open(init_path, "w") as init_file:
        init_file.write(
            "# This file makes the templatetags directory a Python package\n"
        )

    print(
        f"Custom template tag and __init__.py file created in {app_name}/templatetags/"
    )
