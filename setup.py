import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypi_analyser",
    version="1.0.0",
    author="Pukar Acharya",
    description="A Python library to monitor PyPi packages!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iampukar/pypi_analyser",
    project_urls={
        "Bug Tracker": "https://github.com/iampukar/pypi_analyser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9.7",
)
