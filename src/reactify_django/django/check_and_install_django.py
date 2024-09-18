import subprocess
import sys


def check_and_install_django():
    try:
        # Check if django is installed by trying to import it
        subprocess.run(
            [sys.executable, "-m", "django", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("Django is already installed.")

    except subprocess.CalledProcessError:
        # Django is not installed, so install it
        print("Django is not installed. Installing Django...")
        subprocess.run([sys.executable, "-m", "pip", "install", "django"], check=True)
        print("Django has been installed successfully.")
