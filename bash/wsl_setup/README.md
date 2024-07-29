# WSL Development Environment Setup

Contains a collection of scripts to set up a development environment in Windows Subsystem for Linux (WSL). These scripts automate the process of configuring SSH, Git, Conda, Docker, and other essential tools for development.

## Purpose

The purpose of these scripts is to provide a quick and consistent way to set up a development environment in WSL.

## Scripts Included

1. `01_setup_ssh.sh`: Generates SSH key and configures SSH for Git repositories
2. `02_configure_git.sh`: Sets up Git configuration
3. `03_install_conda.sh`: Installs Miniconda and initializes it
4. `04_setup_conda_environments.sh`: Creates Conda environments for different development purposes
5. `05_install_docker.sh`: Installs Docker Engine in WSL
6. `06_clone_repositories.sh`: Clones specified Git repositories
7. `main_setup.sh`: Runs all setup scripts in sequence

## Prerequisites

- Windows 10 or 11 with WSL2 installed
- Ubuntu or another compatible Linux distribution running in WSL
- Internet connection for downloading packages and tools

## Usage

1. Clone this repository or download the scripts to your WSL environment.
2. Navigate to the directory containing the scripts.
3. Run the main setup script using the source command:

   ```bash
   source main_setup.sh "Your Name" "your.email@example.com"
   ```

   Replace "Your Name" and "your.email@example.com" with your actual name and email.

4. Follow any prompts or instructions provided by the scripts.
5. After completion, restart your WSL terminal for all changes to take effect.

## Customization

You can customize individual scripts to fit your specific needs:

- Modify Conda environments in `04_setup_conda_environments.sh`
- Add or remove repositories to clone in `06_clone_repositories.sh`
- Adjust Git configurations in `02_configure_git.sh`
