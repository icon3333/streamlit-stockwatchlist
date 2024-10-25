# Stock Watchlist Tool 📈

A Streamlit-based application to maintain and analyze your stock watchlist with real-time data from Yahoo Finance.

## 🚀 Quick Install

### One-Line Installation (Recommended)
```bash
wget -O - https://raw.githubusercontent.com/yourusername/stock-watchlist/main/install.sh | bash
```
Then open http://localhost:8501 in your browser.

## 🔧 Manual Installation Options

### Option 1: Using Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/stock-watchlist.git
cd stock-watchlist

# Build and run with Docker
docker build -t stock-watchlist .
docker run -d \
    --name stock-watchlist \
    -p 8501:8501 \
    -v $HOME/.stock-watchlist/data:/app/data \
    stock-watchlist
```

### Option 2: Direct Python Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/stock-watchlist.git
cd stock-watchlist

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 📊 Features
- Add stocks by ticker symbol
- Bulk import via CSV
- Real-time financial data
- Custom themes/categories
- Group and analyze stocks
- Automatic data refresh
- Persistent storage

## 💾 Data Storage
- Docker: Data stored in `$HOME/.stock-watchlist/data`
- Python: Data stored in `./data`

## 🔄 Updates

### Docker Version
```bash
cd stock-watchlist
git pull
docker build -t stock-watchlist .
docker restart stock-watchlist
```

### Python Version
```bash
cd stock-watchlist
git pull
pip install -r requirements.txt
```

## 🛟 Troubleshooting
- Port 8501 already in use? Change it in the docker run command: `-p YOUR_PORT:8501`
- Database issues? Check write permissions in the data directory
- Data not updating? Restart the container or the Python process

## 🔒 Security Note
This tool is designed for local use. If deploying on a server, please implement appropriate security measures.

## 📝 License
MIT License - See LICENSE file for details