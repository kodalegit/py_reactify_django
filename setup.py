from setuptools import setup, find_packages

setup(
    name="reactify-django",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.12.5",  # Typer for CLI creation
        "rich>=13.8.1",  # Rich for styled console output
        "tqdm>=4.66.5",  # tqdm for progress bars
        "questionary>=2.0.1",  # Questionary for interactive prompts
    ],
    entry_points={
        "console_scripts": [
            "reactify-django=src.cli:setup_django_react",
        ],
    },
    include_package_data=True,
    description="CLI tool to configure React and TypeScript in Django",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kodalegit/react-in-django",
    author="Victor Kimani",
    author_email="victorkimani77@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
