#!/bin/bash

# Configuration
APP_NAME="stock-watchlist"
CONTAINER_NAME="stock-watchlist"
PORT=8501
DATA_DIR="$HOME/.stock-watchlist/data"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}📈 Installing Stock Watchlist Tool...${NC}"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${YELLOW}Docker not found. Installing Python version...${NC}"
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
        exit 1
    fi
    
    # Install dependencies
    echo "Installing Python dependencies..."
    python3 -m pip install streamlit pandas yfinance
    
    # Clone repository
    git clone https://github.com/yourusername/stock-watchlist.git
    cd stock-watchlist
    
    echo -e "${GREEN}✅ Installation complete!${NC}"
    echo "To run: streamlit run app.py"
    echo "Then open http://localhost:8501 in your browser"
    exit 0
fi

# Create data directory
mkdir -p "$DATA_DIR"

# Clone repository
git clone https://github.com/yourusername/stock-watchlist.git
cd stock-watchlist

# Build and run with Docker
echo "🐳 Building Docker container..."
docker build -t $APP_NAME .

# Stop existing container if it exists
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

# Run the container
echo "🚀 Starting container..."
docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:8501 \
    -v "$DATA_DIR":/app/data \
    $APP_NAME

echo -e "${GREEN}✅ Installation complete!${NC}"
echo -e "Access the app at: ${YELLOW}http://localhost:$PORT${NC}"