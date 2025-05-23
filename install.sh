#!/bin/bash

# Configuration
APP_NAME="streamlit-stockwatchlist"
CONTAINER_NAME="streamlit-stockwatchlist"
PORT=8501
DATA_DIR="./data"

echo "📈 Installing/Updating Stock Watchlist Tool..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker to proceed."
    exit 1
fi

# Stop and remove existing container if it exists
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "Stopping and removing existing container..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Check if directory exists
if [ -d "$APP_NAME" ]; then
    echo "Updating existing installation..."
    cd "$APP_NAME"
    git pull
else
    echo "Performing fresh installation..."
    # Clone repository
    git clone https://github.com/icon3333/streamlit-stockwatchlist.git "$APP_NAME"
    cd "$APP_NAME"
fi

# Create data directory if it doesn't exist
if [ ! -d "$DATA_DIR" ]; then
    mkdir -p "$DATA_DIR"
    echo "Created data directory"
fi

# Build Docker image
echo "Building Docker image..."
docker build -t $APP_NAME .

# Run Docker container
echo "Starting Docker container..."
docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:8501 \
    -v "$(pwd)/$DATA_DIR":/app/data \
    $APP_NAME

echo "✅ Installation/Update complete!"
echo "Access the app at: http://localhost:$PORT"
