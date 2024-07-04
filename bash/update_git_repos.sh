#!/bin/bash

# Define the root directory containing all project subdirectories
PROJECTS_DIR="path/to/projects"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

SEP="=================================================="

updated_repos=()
skipped_repos=()
failed_repos=()

# Iterate over each subdirectory in the projects directory
for dir in "$PROJECTS_DIR"/*/; do
    # Check if the directory is a Git repository
    if [ -d "$dir/.git" ]; then
        echo -e "${YELLOW}$SEP${NC}"
        echo -e "Updating repository in ${GREEN}$dir${NC}"
        cd "$dir"
        # Pull the latest changes from the default remote repository and branch
        if git pull origin main; then
            echo -e "${GREEN}Successfully updated $dir${NC}"
            updated_repos+=("$dir")
        else
            echo -e "${RED}Update failed for $dir. Please check the output for details.${NC}"
            failed_repos+=("$dir")
        fi
    else
        echo -e "${RED}$dir is not a Git repository, skipping.${NC}"
        skipped_repos+=("$dir")
    fi
done

echo -e "${YELLOW}$SEP${NC}"
echo -e "${GREEN}All repositories have been processed.${NC}"

# Print summary
echo -e "${YELLOW}$SEP${NC}"
echo -e "${GREEN}Summary:${NC}"
echo -e "${GREEN}Updated Repositories:${NC}"
for repo in "${updated_repos[@]}"; do
    echo -e "${GREEN}- $repo${NC}"
done

echo -e "${YELLOW}Skipped Directories (Not Git Repositories):${NC}"
for repo in "${skipped_repos[@]}"; do
    echo -e "${YELLOW}- $repo${NC}"
done

echo -e "${RED}Repositories that failed to update:${NC}"
for repo in "${failed_repos[@]}"; do
    echo -e "${RED}- $repo${NC}"
done
echo -e "${YELLOW}$SEP${NC}"
