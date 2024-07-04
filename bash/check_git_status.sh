#!/bin/bash

# Define the root directory containing all project subdirectories
PROJECTS_DIR="/home/machris/projects"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Separator for visual separation in output
SEP="=================================================="

# Iterate over each subdirectory in the projects directory
for dir in "$PROJECTS_DIR"/*/; do
    echo -e "${YELLOW}$SEP${NC}"
    # Check if the directory is a Git repository
    if [ -d "$dir/.git" ]; then
        cd "$dir"
        # Fetch the current branch name
        current_branch=$(git rev-parse --abbrev-ref HEAD)
        # Check the status of the repository
        if git status | grep -q 'nothing to commit, working tree clean'; then
            echo -e "Repository in ${GREEN}$dir${NC} is on branch ${GREEN}$current_branch${NC} and is ${GREEN}up to date${NC}."
        else
            echo -e "Repository in ${YELLOW}$dir${NC} on branch ${YELLOW}$current_branch${NC} has ${YELLOW}uncommitted changes${NC}:"
            # Display summary of changes
            git status -s | while read -r line; do
                echo -e "${YELLOW}$line${NC}"
            done
        fi
    else
        echo -e "${RED}$dir is not a Git repository, skipping.${NC}"
    fi
done

echo -e "${YELLOW}$SEP${NC}"
echo -e "Completed checking all repositories."
