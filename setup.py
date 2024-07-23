from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py_markdown_crawler",
    version="0.1.0",
    author="llucid-97",
    author_email="hexxagon6@gmail.com",
    description="A tool to crawl a directory and create a markdown file of all .py files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/py_markdown_crawler",
    packages=find_packages(),
    install_requires=[
        "markdown",
        "pyreadline3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "py_markdown_crawler=py_markdown_crawler:main",
        ],
    },
)