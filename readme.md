This tool crawls a specified directory and creates a markdown file containing all the .py files found, each in a code block preceded by its path.

## Installation

You can install this package using pip:

```
pip install py_markdown_crawler
```

## Usage

After installation, you can run the tool from the command line:

```
py_markdown_crawler
```

You will be prompted to enter:
1. The directory path to crawl
2. The name of the output markdown file

The tool will then create a markdown file with the specified name, containing all the .py files from the specified directory and its subdirectories.

## Features

- Crawls directories recursively
- Creates a well-formatted markdown file
- Supports path autocompletion (if pyreadline3 is installed)
- Works on Windows, macOS, and Linux

## License

This project is licensed under the MIT License - see the LICENSE file for details.

