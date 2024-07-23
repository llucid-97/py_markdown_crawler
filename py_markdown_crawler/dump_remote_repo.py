import os
import sys
import subprocess
import fnmatch

def clone_repo(repo_url):
    repo_name = repo_url.split('/')[-1].split('.')[0]
    subprocess.run(['git', 'clone', repo_url, repo_name])
    return repo_name

def read_gitignore(repo_path):
    gitignore_path = os.path.join(repo_path, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as file:
            return file.read().splitlines()
    return []

def should_ignore(file_path, gitignore_patterns, custom_ignore_types):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in custom_ignore_types:
        return True
    
    for pattern in gitignore_patterns:
        if fnmatch.fnmatch(file_path, pattern):
            return True
    return False

def process_files(repo_path, output_file, custom_ignore_types):
    gitignore_patterns = read_gitignore(repo_path)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(repo_path):
            if '.git' in dirs:
                dirs.remove('.git')  # Exclude the .git folder from the walk
            
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, repo_path)
                
                if should_ignore(rel_path, gitignore_patterns, custom_ignore_types):
                    continue  # Skip files matching gitignore patterns or custom ignore types
                
                outfile.write(f"Relative Path: {rel_path}\n")
                outfile.write("File Contents:\n")
                
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    outfile.write("\n\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <git_repo_url>")
        sys.exit(1)

    repo_url = sys.argv[1]
    repo_path = clone_repo(repo_url)
    output_file = f"{repo_path}_combined.txt"
    
    # Custom list of file types to ignore
    custom_ignore_types = ['.png', '.jpeg', '.jpg', '.gif', '.bmp', '.svg', '.ico']
    
    process_files(repo_path, output_file, custom_ignore_types)
    print(f"Combined file created: {output_file}")

if __name__ == '__main__':
    main()