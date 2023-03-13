"""Setup for the hello_world package."""
import setuptools


setuptools.setup(

    # Name of the package as used by import.
    name="hello_world",

    # Package version
    version="0.1.0",

    # Decriptive information.
    description="Python packaging tutorial package",
    keywords="hello,world,tutorial,packaging",
    url="https://www.github.com/JohnDoe/python-packaging/",

    # Author settings.
    author="John Doe",
    author_email="john.doe@gmail.com",

    # Specify which (sub)package(s) to include.
    # Tip: Use setuptools.find_packages("src") to automate discovery.
    packages=["hello_world"],

    # Which folder contains the package(s).
    package_dir={"": "src"},

    # Dependencies for the package.
    install_requires=[
        "pandas==1.5.3",
    ],

)
