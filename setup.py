import re
import setuptools

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bootstrap/bootstrap.py').read(),
    re.M
    ).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pomodoro", # Replace with your own username
    version = version,
    author = "Aaron Couch",
    author_email = "aaron.couch@stackpath.com",
    description = "A simple Python time management tool based on the Pomodoro Technique.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/aaroncouch/pomodoro",
    packages = setuptools.find_packages(),
    entry_points = {
        "console_scripts": [
            "pomodoro = pomodoro.pomodoro:main"
        ]
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
