#!/bin/bash

# File: 02_configure_git.sh
# Purpose: Set up Git configuration
# Usage: ./02_configure_git.sh [name] [email]

NAME=${1:-"Chris Mannina"}
EMAIL=${2:-"machris@umich.edu"}

echo "Configuring Git..."

cat > ~/.gitconfig << EOL
[user]
    name = $NAME
    email = $EMAIL

[core]
    editor = code --wait

[init]
    defaultBranch = main

[alias]
    st = status
    co = checkout
    br = branch
    ci = commit

[url "git@github.com:"]
    insteadOf = https://github.com/

[url "git@git.umms.med.umich.edu:"]
    insteadOf = https://git.umms.med.umich.edu/
EOL

echo "Git configuration complete."