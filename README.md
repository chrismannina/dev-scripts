# Dev Scripts

This repository contains a collection of useful scripts for developers to streamline various tasks.

## Scripts

### 1. Create Project Structure (Python)

**File:** `python/create_project_structure.py`

Creates a directory and file structure based on an input file.

**Usage:**
```
python create_project_structure.py <structure_file> [--indent-size <size>] [--output-dir <path>]
```

**Example:**
```
python create_project_structure.py project_structure.txt --indent-size 2 --output-dir ./new_project
```

### 2. Codebase Analyzer (Python)

**File:** `python/codebase_analyzer.py`

Analyzes a codebase by outputting its directory structure and file contents.

**Usage:**
```
python codebase_analyzer.py <startpath> <output_file> [--exclude-dirs <dir1> <dir2> ...] [--exclude-types <ext1> <ext2> ...]
```

**Example:**
```
python codebase_analyzer.py ./my_project output.txt --exclude-dirs node_modules .git --exclude-types .pyc .log
```

### 3. Update Git Repos (Bash)

**File:** `bash/update_git_repos.sh`

Updates all Git repositories in a specified directory.

**Usage:**
```
bash update_git_repos.sh
```

### 4. Check Git Status (Bash)

**File:** `bash/check_git_status.sh`

Checks the status of all Git repositories in a specified directory.

**Usage:**
```
bash check_git_status.sh
```

## Requirements

- Python 3.x for Python scripts
- Bash shell for Bash scripts

## Configuration

- For the Git-related bash scripts, you may need to modify the `PROJECTS_DIR` variable in each script to point to your projects directory.
