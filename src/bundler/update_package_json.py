import json
import os


def update_package_json_scripts():
    package_json_path = "package.json"

    try:
        # Check if the package.json file exists
        if not os.path.isfile(package_json_path):
            raise FileNotFoundError(f"{package_json_path} does not exist.")

        # Read the existing package.json
        with open(package_json_path, "r") as file:
            data = json.load(file)

        # Update the scripts section
        data["scripts"] = {
            "start": "webpack serve",
            "build": "cross-env NODE_ENV=production webpack",
        }

        # Write the updated package.json back to the file
        with open(package_json_path, "w") as file:
            json.dump(data, file, indent=2)

        print(f"Successfully updated {package_json_path} with new scripts.")

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except json.JSONDecodeError as jde:
        print(f"Error decoding JSON: {jde}")
    except IOError as ioe:
        print(f"IO error: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
