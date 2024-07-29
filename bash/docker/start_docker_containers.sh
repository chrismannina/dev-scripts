#!/bin/bash

# Set the path to your docker-compose.yml file
COMPOSE_FILE_PATH="$HOME/projects/env_relay/start_development.yml"

# Check if the docker-compose file exists
if [ ! -f "$COMPOSE_FILE_PATH" ]; then
    echo "Error: docker-compose.yml file not found at $COMPOSE_FILE_PATH"
    exit 1
fi

# Bring up the containers
echo "Bringing up the containers..."
docker compose -f "$COMPOSE_FILE_PATH" up -d

# Check the exit status
if [ $? -eq 0 ]; then
    echo "Containers have been successfully brought up."
else
    echo "Error: Failed to bring up the containers."
    exit 1
fi

# Optional: List running containers
echo "Running containers:"
docker compose -f "$COMPOSE_FILE_PATH" ps