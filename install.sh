#!/bin/bash

# Configuration
APP_NAME="streamlit-stockwatchlist"
CONTAINER_NAME="streamlit-stockwatchlist"
PORT=8501
DATA_DIR="$HOME/.stockwatchlist/data"
REPO_URL="https://github.com/icon3333/streamlit-stockwatchlist.git"
BRANCH="prod"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}📈 Installing Stock Watchlist Tool...${NC}"

# Create temporary directory and navigate to it
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR" || exit 1

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${YELLOW}Docker not found. Installing Python version...${NC}"
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
        exit 1
    fi
    
    # Clone repository
    echo "Cloning repository..."
    git clone -b ${BRANCH} "$REPO_URL" . || {
        echo -e "${RED}Failed to clone repository${NC}"
        exit 1
    }
    
    # Install dependencies
    echo "Installing Python dependencies..."
    python3 -m pip install -r requirements.txt
    
    echo -e "${GREEN}✅ Installation complete!${NC}"
    echo "To run: streamlit run app.py"
    echo "Then open http://localhost:${PORT} in your browser"
    exit 0
fi

# Create data directory
mkdir -p "$DATA_DIR"

# Clone repository
echo "Cloning repository..."
git clone -b ${BRANCH} "$REPO_URL" . || {
    echo -e "${RED}Failed to clone repository${NC}"
    exit 1
}

# Verify Dockerfile exists
if [ ! -f "Dockerfile" ]; then
    echo -e "${RED}Error: Dockerfile not found${NC}"
    exit 1
fi

# Build and run with Docker
echo "🐳 Building Docker container..."
docker build -t $APP_NAME . || {
    echo -e "${RED}Docker build failed${NC}"
    exit 1
}

# Stop existing container if it exists
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

# Run the container
echo "🚀 Starting container..."
docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:8501 \
    -v "$DATA_DIR":/app/data \
    $APP_NAME || {
    echo -e "${RED}Failed to start Docker container${NC}"
    exit 1
}

echo -e "${GREEN}✅ Installation complete!${NC}"
echo -e "Access the app at: ${YELLOW}http://localhost:${PORT}${NC}"

# Clean up temporary directory
cd || exit
rm -rf "$TEMP_DIR"