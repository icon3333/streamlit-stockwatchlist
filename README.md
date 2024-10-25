# Stock Watchlist Tool 📈

> **Note**: This is a hobby project created with the assistance of LLMs (Large Language Models). All tools and code here are for experimental and learning purposes only, not intended for production use. Feel free to explore and play around!

A Streamlit-based application to maintain and analyze your stock watchlist with real-time data from Yahoo Finance.

## 👋 About This Project

I'm a hobby programmer who enjoys experimenting with different tools and technologies. This project was created using:
- LLMs (like ChatGPT/Claude) for code assistance
- Streamlit for the web interface
- Python for data processing
- Docker for containerization

The goal is to learn and have fun while building something useful! While the code works, it's meant for personal use and experimentation rather than production environments.

## Features

- **Add Stocks:** Input ticker symbols to add stocks to your watchlist
- **View Watchlist:** Displays key metrics for each stock
- **Edit Themes:** Customize the 'theme' column to group stocks
- **Group Stocks:** Group stocks by any column, including numerical columns divided into quintiles
- **Automatic Data Refresh:** Data is refreshed every 24 hours to ensure up-to-date information
- **Bulk Import:** Add multiple stocks via CSV upload
- **Persistent Storage:** All your watchlist data is stored locally

## 🚀 Quick Install (Recommended)

```bash
wget -O - https://raw.githubusercontent.com/icon3333/streamlit-stockwatchlist/prod/install.sh | bash
```
Then open http://localhost:8501 in your browser.

## 🔧 Manual Installation Options

### Option 1: Using Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/icon3333/streamlit-stockwatchlist.git
cd streamlit-stockwatchlist

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
git clone https://github.com/icon3333/streamlit-stockwatchlist.git
cd streamlit-stockwatchlist

# Install dependencies
python3 -m pip install streamlit pandas yfinance

# Run the application
streamlit run app.py
```

## 💾 Data Storage

- Docker: Data stored in `$HOME/.stock-watchlist/data`
- Python: Data stored in `./data`

## 🔄 Updates

### Docker Version
```bash
cd streamlit-stockwatchlist
git pull
docker build -t stock-watchlist .
docker restart stock-watchlist
```

### Python Version
```bash
cd streamlit-stockwatchlist
git pull
pip install -r requirements.txt
```

## 🛟 Troubleshooting

- **Port 8501 in use?** Change the port: `-p YOUR_PORT:8501`
- **Database issues?** Check write permissions in the data directory
- **Data not updating?** Restart the container or Python process

## Requirements

- Python 3.x
- See `requirements.txt` for Python dependencies
- Docker (optional, but recommended)

## ⚠️ Disclaimer

This is a hobby project created for learning and experimentation. The code and tools provided:
- Are not production-ready
- May contain bugs or security issues
- Should be used at your own risk
- Are meant for educational purposes
- May need significant modifications for serious use

## License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- Thanks to the LLM communities for assistance and inspiration
- Built with Streamlit and other open-source tools
- Stock data provided by Yahoo Finance API