#!/usr/bin/env python3
"""
create_project_structure.py

This script creates a directory and file structure based on an input file.

Usage:
    python create_project_structure.py <structure_file> [--indent-size <size>] [--output-dir <path>]

The structure file should contain a hierarchical representation of directories and files:
- Use indentation (default 4 spaces) to indicate nesting
- End directory names with a '/'
- File names should not end with a '/'

Example structure file:
    project/
        src/
            main.py
            utils.py
        tests/
            test_main.py
        README.md
"""

import os
import sys
import argparse
import logging

def create_structure(structure_file, indent_size, output_dir):
    current_path = [output_dir]
    
    logging.info(f"Creating project structure from {structure_file} in {output_dir}")
    
    with open(structure_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.rstrip()
            if not line:
                continue
            
            # Count leading spaces to determine depth
            depth = len(line) - len(line.lstrip())
            if depth % indent_size != 0:
                logging.warning(f"Line {line_num}: Indentation is not a multiple of {indent_size}")
            name = line.strip()
            
            # Adjust current path based on depth
            while len(current_path) > (depth // indent_size) + 1:  # +1 for output_dir
                current_path.pop()
            
            try:
                if name.endswith('/'):
                    # It's a directory
                    current_path.append(name[:-1])
                    dir_path = os.path.join(*current_path)
                    os.makedirs(dir_path, exist_ok=True)
                    logging.info(f"Created directory: {dir_path}")
                else:
                    # It's a file
                    file_path = os.path.join(*current_path, name)
                    with open(file_path, 'a') as f:
                        pass
                    logging.info(f"Created file: {file_path}")
            except OSError as e:
                logging.error(f"Error creating {name}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Create a project structure from a file.")
    parser.add_argument("structure_file", help="Path to the structure file")
    parser.add_argument("--indent-size", type=int, default=4, help="Number of spaces per indentation level")
    parser.add_argument("--output-dir", default=os.getcwd(), help="Directory to create the structure in")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    if not os.path.exists(args.structure_file):
        logging.error(f"Error: File '{args.structure_file}' not found.")
        sys.exit(1)

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    create_structure(args.structure_file, args.indent_size, args.output_dir)
    logging.info(f"Project structure created successfully in {args.output_dir}!")

if __name__ == "__main__":
    main()