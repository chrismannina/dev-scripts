#!/usr/bin/env python3
"""
codebase_analyzer.py

This script analyzes a codebase by outputting its directory structure and file contents.

Usage:
    python codebase_analyzer.py <startpath> <output_file> [--exclude-dirs <dir1> <dir2> ...] [--exclude-types <ext1> <ext2> ...]

Arguments:
    startpath       The root directory of the codebase to analyze.
    output_file     The file where the analysis results will be written.
    --exclude-dirs  Optional list of directories to exclude from the analysis. Overrides defaults.
    --exclude-types Optional list of file extensions to exclude from the analysis. Overrides defaults.

Example:
    python codebase_analyzer.py /path/to/project output.txt --exclude-dirs node_modules build --exclude-types .pyc .log
"""

import os
import argparse
import mimetypes

# Default exclusions
DEFAULT_EXCLUDE_DIRS = {
    '__pycache__', '.git', 'node_modules', 'venv', 'env', 
    'build', 'dist', '.idea', '.vscode'
}
DEFAULT_EXCLUDE_TYPES = {
    '.pyc', '.pyo', '.so', '.o', '.obj', '.dll', '.exe', '.bin',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico',
    '.mp3', '.mp4', '.avi', '.mov', '.flv', '.wav',
    '.zip', '.tar', '.gz', '.rar', '.7z',
    '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx'
}

def list_files(startpath, exclude_dirs, exclude_types):
    result = []
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        result.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not any(f.endswith(ext) for ext in exclude_types):
                result.append(f"{subindent}{f}")
    return result

def is_text_file(file_path, exclude_types):
    if any(file_path.endswith(ext) for ext in exclude_types):
        return False
    
    # Explicitly include common web development file types
    web_dev_extensions = {'.js', '.jsx', '.ts', '.tsx', '.html', '.css', '.json', '.md', '.txt'}
    if any(file_path.endswith(ext) for ext in web_dev_extensions):
        return True
    
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('text')

def read_file(file_path, max_size=1024*1024):  # 1MB limit
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return file.read(max_size)
    except Exception as e:
        return f"Error reading file: {str(e)}"

def create_output(startpath, exclude_dirs, exclude_types, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        directory_structure = list_files(startpath, exclude_dirs, exclude_types)
        f.write("Project Directory Structure:\n")
        f.write("\n".join(directory_structure))
        f.write("\n\n")
        for root, dirs, files in os.walk(startpath):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                file_path = os.path.join(root, file)
                if is_text_file(file_path, exclude_types):
                    f.write(f"File: {file_path}\n")
                    f.write("Contents:\n")
                    f.write(read_file(file_path))
                    f.write("\n\n")

def main():
    parser = argparse.ArgumentParser(description='Analyze a codebase by outputting its directory structure and file contents.')
    parser.add_argument('startpath', type=str, help='The root directory of the codebase.')
    parser.add_argument('output_file', type=str, help='The output text file.')
    parser.add_argument('--exclude-dirs', type=str, nargs='*', default=DEFAULT_EXCLUDE_DIRS, 
                        help='List of directories to exclude. Overrides defaults.')
    parser.add_argument('--exclude-types', type=str, nargs='*', default=DEFAULT_EXCLUDE_TYPES, 
                        help='List of file extensions to exclude. Overrides defaults.')
    args = parser.parse_args()

    exclude_dirs = set(args.exclude_dirs)
    exclude_types = set(args.exclude_types)

    create_output(args.startpath, exclude_dirs, exclude_types, args.output_file)
    print(f"Analysis complete. Results written to {args.output_file}")
    print(f"Excluded directories: {', '.join(exclude_dirs)}")
    print(f"Excluded file types: {', '.join(exclude_types)}")

if __name__ == "__main__":
    main()