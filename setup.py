from setuptools import setup, find_packages

setup(
    name="reactify-django",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click==8.1.7",
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
