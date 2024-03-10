#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @created: 02.02.2024
# @author: Aleksey Komissarov
# @author: Claude Opus
# @contact: ad3002@gmail.com

import os
import argparse

def traverse_repository(repo_path, extensions):
    code_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                code_files.append(file_path)
    return code_files

def extract_code(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    return code

def consolidate_code(code_files):
    consolidated_code = ""
    for file_path in code_files:
        code = extract_code(file_path)
        consolidated_code += f"# File: {file_path}\n{code}\n\n"
    return consolidated_code

def main():
    parser = argparse.ArgumentParser(description="Code Consolidator")
    parser.add_argument("-r", "--repo_path", help="Path to the code repository")
    parser.add_argument("-o", "--output_file", default="consolidated_code.py", help="Output file (default: consolidated_code.py)")
    parser.add_argument("--extensions", nargs="+", default=[".py"], help="File extensions to include (default: .py)")
    args = parser.parse_args()

    repo_path = args.repo_path
    extensions = args.extensions
    output_file = args.output_file

    code_files = traverse_repository(repo_path, extensions)
    consolidated_code = consolidate_code(code_files)
    
    with open(output_file, "w") as file:
        file.write(consolidated_code)

if __name__ == "__main__":
    main()