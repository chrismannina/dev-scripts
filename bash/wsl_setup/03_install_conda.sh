#!/bin/bash

# File: 03_install_conda.sh
# Purpose: Install Miniconda and initialize it
# Usage: ./03_install_conda.sh

echo "Installing Miniconda..."

# Download Miniconda installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh

# Install Miniconda
bash ~/miniconda.sh -b -p $HOME/miniconda

# Remove the installer
rm ~/miniconda.sh

# Initialize Conda
eval "$($HOME/miniconda/bin/conda shell.bash hook)"
conda init

# Update Conda
conda update -n base -c defaults conda -y

echo "Conda installation complete. Please restart your terminal or run 'source ~/.bashrc' to use Conda."