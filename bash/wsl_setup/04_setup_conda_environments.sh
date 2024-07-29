#!/bin/bash

# File: 04_setup_conda_environments.sh
# Purpose: Create Conda environments for different development purposes
# Usage: ./04_setup_conda_environments.sh

echo "Setting up Conda environments..."

# Create data engineering environment
conda create -n data_eng python=3.12 -y
conda activate data_eng
conda install -c conda-forge dbt-core prefect pandas sqlalchemy psycopg2 pymysql black -y
conda deactivate

# Create Django web dev environment
conda create -n django python=3.12 -y
conda activate django
conda install -c conda-forge django black pytest -y
pip install django-ninja django-environ django-debug-toolbar django-extensions
conda deactivate

# Create generic Python environment
conda create -n dev python=3.12 -y
conda activate dev
conda install -c conda-forge numpy pandas matplotlib scikit-learn jupyter black pytest requests beautifulsoup4 -y
conda deactivate

echo "Conda environments setup complete. Available environments:"
conda env list