#!/bin/bash

# File: 01_setup_ssh.sh
# Purpose: Generate SSH key and configure SSH for Git repositories
# Usage: ./01_setup_ssh.sh [email]

EMAIL=${1:-"machris@umich.com"}

echo "Setting up SSH..."

# Generate SSH key
ssh-keygen -t ed25519 -C "$EMAIL" -f ~/.ssh/id_ed25519 -N ""

# Start ssh-agent and add key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Create SSH config
mkdir -p ~/.ssh
cat > ~/.ssh/config << EOL
Host git.umms.med.umich.edu
    HostName git.umms.med.umich.edu
    User git
    IdentityFile ~/.ssh/id_ed25519

Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
EOL

echo "SSH setup complete. Your public key is:"
cat ~/.ssh/id_ed25519.pub
echo "Please add this key to your GitHub and GitLab accounts."