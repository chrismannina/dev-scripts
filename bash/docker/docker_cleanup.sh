#!/bin/bash

# Function to check if Docker daemon is running and accessible
check_docker() {
    if ! docker info >/dev/null 2>&1; then
        echo "Error: Docker daemon is not running or you don't have permission to access it."
        echo "Please start Docker or check your permissions and try again."
        exit 1
    fi
}

# Function to remove dangling images
remove_dangling_images() {
    echo "Removing dangling images..."
    dangling_images=$(docker images -f "dangling=true" -q)
    if [ -z "$dangling_images" ]; then
        echo "No dangling images found."
    else
        docker rmi $dangling_images
        echo "Dangling images removed successfully."
    fi
}

# Main execution
check_docker
remove_dangling_images

echo "Cleanup completed."