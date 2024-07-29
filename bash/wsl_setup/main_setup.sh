#!/bin/bash

# File: main_setup.sh
# Purpose: Run all setup scripts in sequence using source
# Usage: source main_setup.sh [git_name] [git_email]

# Check if the script is being run with source
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Please run this script using 'source main_setup.sh' instead of executing it directly."
    exit 1
fi

echo "Starting WSL development environment setup..."

# Run individual setup scripts
source ./01_setup_ssh.sh "$2"
source ./02_configure_git.sh "$1" "$2"
source ./03_install_conda.sh
source ./04_setup_conda_environments.sh
source ./05_install_docker.sh
source ./06_clone_repositories.sh

echo "Setup complete! Please restart your WSL terminal for all changes to take effect."