import unittest
from unittest.mock import mock_open, patch
from src.reactify_django.django.template_tag_creator import create_template_tag


class TestCreateTemplateTag(unittest.TestCase):

    @patch("src.reactify_django.django_configurator.os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_create_template_tag(self, mock_open, mock_makedirs):
        app_name = "myapp"

        # Call the function
        create_template_tag(app_name)

        # Define expected paths
        tag_path = f"{app_name}/templatetags/react_root.py"
        init_path = f"{app_name}/templatetags/__init__.py"

        # Define expected tag content
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
        # Check that os.makedirs was called with the correct directory
        mock_makedirs.assert_called_once_with(f"{app_name}/templatetags", exist_ok=True)

        # Check that open was called with the correct file paths and mode
        mock_open.assert_any_call(tag_path, "w")
        mock_open.assert_any_call(init_path, "w")

        # Check that the correct content was written to react_root.py
        handle = mock_open()
        handle.write.assert_any_call(tag_code)

        # Check that the __init__.py file contains the expected content
        init_code = "# This file makes the templatetags directory a Python package\n"
        handle.write.assert_any_call(init_code)

        # Verify the function printed the correct output
        with patch("builtins.print") as mock_print:
            create_template_tag(app_name)
            mock_print.assert_called_once_with(
                f"Custom template tag and __init__.py file created in {app_name}/templatetags/"
            )


if __name__ == "__main__":
    unittest.main()
