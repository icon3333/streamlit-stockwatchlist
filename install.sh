#!/bin/bash

# Configuration
APP_NAME="streamlit-stockwatchlist"
CONTAINER_NAME="streamlit-stockwatchlist"
PORT=8501
DATA_DIR="./data"

echo "📈 Installing Stock Watchlist Tool..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker to proceed."
    exit 1
fi

# Clone repository (assumes you have access)
git clone https://github.com/icon3333/streamlit-stockwatchlist.git "$APP_NAME"
cd "$APP_NAME" || exit 1

# Build Docker image
docker build -t $APP_NAME .

# Create data directory
mkdir -p "$DATA_DIR"

# Run Docker container
docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:8501 \
    -v "$DATA_DIR":/app/data \
    $APP_NAME

echo "✅ Installation complete!"
echo "Access the app at: http://localhost:$PORT"