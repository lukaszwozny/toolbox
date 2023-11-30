import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="toolbox",
    version="0.2.0",
    author="Lukasz Wozny",
    author_email="kontakt@lukaszwozny.com",
    description="Helpful functions for apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lukaszwozny/toolbox",
    project_urls={"Bug Tracker": "https://github.com/lukaszwozny/toolbox/issues"},
    license="MIT",
    packages=[
        "toolbox",
        "toolbox.managers",
        "toolbox.managers.static",
        "toolbox.managers.static.sounds",
    ],
    install_requires=required,
    package_data={
        "toolbox.managers.static": ["**/*"],
    },
    include_package_data=True,
)
