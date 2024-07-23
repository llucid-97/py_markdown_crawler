import os
import markdown
import sys

# Determine which readline package to use based on the OS
if sys.platform.startswith('win'):
    try:
        import pyreadline3 as readline
    except ImportError:
        print("pyreadline3 is not installed. Path autocompletion will be disabled.")
        print("To enable, install pyreadline3 with: pip install pyreadline3")
        readline = None
else:
    import readline

def complete_path(text, state):
    if readline is None:
        return None
    
    if '~' in text:
        text = os.path.expanduser(text)
    
    dir_name = os.path.dirname(text)
    dir_name = '.' if not dir_name else dir_name
    file_name = os.path.basename(text)
    
    if not os.path.isdir(dir_name):
        return None
    
    files = os.listdir(dir_name)
    matches = [f for f in files if f.startswith(file_name)]
    
    if state < len(matches):
        full_path = os.path.join(dir_name, matches[state])
        if os.path.isdir(full_path):
            return full_path + os.sep
        return full_path
    return None

def setup_autocompletion():
    if readline is not None:
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(complete_path)

def crawl_directory(directory):
    markdown_content = ""
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                
                markdown_content += f"## {relative_path}\n\n"
                markdown_content += "```python\n"
                
                with open(file_path, 'r', encoding='utf-8') as py_file:
                    markdown_content += py_file.read()
                
                markdown_content += "\n```\n\n"
    
    return markdown_content

def save_markdown(content, output_file):
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write(content)

def main():
    setup_autocompletion()
    
    directory_to_crawl = input("Enter the directory path to crawl: ")
    output_file = input("Enter the output markdown file name: ")
    
    if not output_file.endswith('.md'):
        output_file += '.md'
    
    markdown_content = crawl_directory(directory_to_crawl)
    save_markdown(markdown_content, output_file)
    
    print(f"Markdown file '{output_file}' has been created successfully.")
if __name__ == "__main__":
    main()