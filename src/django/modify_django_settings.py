import os


def add_app_django_settings(project_name, app_name):
    settings_path = os.path.join(project_name, "settings.py")

    if not os.path.isfile(settings_path):
        raise FileNotFoundError(f"{settings_path} does not exist")

    try:

        with open(settings_path, "r") as file:
            settings_content = file.readlines()

        in_installed_apps = False
        with open(settings_path, "w") as file:
            for line in settings_content:
                if line.strip().startswith("INSTALLED_APPS"):
                    in_installed_apps = True
                    file.write(line)
                    continue

                if in_installed_apps:
                    if line.strip().endswith("]"):
                        # Add app name before the closing bracket
                        file.write(f"    '{app_name}',\n")
                        in_installed_apps = False

                file.write(line)

        print(f"App '{app_name}' has been added to INSTALLED_APPS in {settings_path}")

    except IOError as e:
        raise IOError(f"An error occurred while accessing {settings_path}: {e}")
