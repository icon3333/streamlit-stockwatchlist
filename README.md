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
- **Bulk Import:** Add multiple stocks via CSV upload (CSV must contain a column named 'ticker_symbol')
- **Export Watchlist:** Download your entire watchlist as a CSV file with all stock metrics and custom themes
- **Persistent Storage:** All your watchlist data is stored locally

## CSV Import Format

When using the bulk import feature, your CSV file must meet the following requirements:
- Must contain a column named exactly 'ticker_symbol'
- The ticker_symbol column should contain valid stock ticker symbols (e.g., AAPL, GOOGL, MSFT)
- Additional columns will be ignored
- Each ticker symbol should be on a new row

Example CSV format:
```csv
ticker_symbol
AAPL
GOOGL
MSFT
```

## 🚀 Quick Install and Update (Recommended)

### Using the `install.sh` Script

The install script now supports both fresh installations and updates to existing installations.

**Prerequisites:**

- **Docker** installed on your system. You can download it from the [official Docker website](https://www.docker.com/get-started).

**Steps:**

1. **Download the `install.sh` Script**

   For fresh installation or to update your existing script:

   ```bash
   wget https://raw.githubusercontent.com/icon3333/streamlit-stockwatchlist/main/install.sh
   ```

   Or with curl:

   ```bash
   curl -O https://raw.githubusercontent.com/icon3333/streamlit-stockwatchlist/main/install.sh
   ```

2. **Make the Script Executable**

   ```bash
   chmod +x install.sh
   ```

3. **Run the Installation/Update Script**

   ```bash
   ./install.sh
   ```

The script will automatically:
- Check for an existing installation
- Stop and remove any existing container
- Update the code if it's an existing installation
- Perform a fresh install if it's a new installation
- Preserve your watchlist data
- Build the Docker image
- Start a new container with the latest code

4. **Access the Application**

   Once the script completes, open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

## 🔄 Updates

### Easiest Method (Recommended)
Simply rerun the install script:
```bash
./install.sh
```

### Manual Docker Update

If you prefer to update manually:

```bash
# Stop and remove the current container
docker stop streamlit-stockwatchlist
docker rm streamlit-stockwatchlist

# Rebuild the image with new code
docker build -t streamlit-stockwatchlist .

# Run the new container
docker run -d \
    --name streamlit-stockwatchlist \
    -p 8501:8501 \
    -v "$PWD/data":/app/data \
    streamlit-stockwatchlist
```

### Python Version

For direct Python installations:

```bash
cd streamlit-stockwatchlist
git pull
pip install -r requirements.txt
```

## 🛟 Troubleshooting

- **Port 8501 in use?** Change the port in the install.sh script or when running the Docker container:
  ```bash
  # For Docker run command
  -p YOUR_PORT:8501
  ```
- **Docker Not Installed?** Install Docker from the official website.
- **Permission Issues?** Run the install.sh script with sudo or adjust your user's permissions:
  ```bash
  sudo ./install.sh
  ```
- **Data Not Updating?** Restart the Docker container or Python process.
- **Update Failed?** Try removing the installation directory and running a fresh install:
  ```bash
  rm -rf streamlit-stockwatchlist
  ./install.sh
  ```

## 💾 Data Storage

Your watchlist data is stored in:
- `./data` directory within the project folder
- This data persists across updates and container restarts
- Back up this directory if you want to preserve your watchlist

## Requirements

- Docker (Recommended for the install.sh script)
- Python 3.x (If using direct Python installation)
- See `requirements.txt` for Python dependencies

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