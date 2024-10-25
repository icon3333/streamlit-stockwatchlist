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

## 🚀 Quick Install (Recommended)

### Using the `install.sh` Script

**Prerequisites:**

- **Docker** installed on your system. You can download it from the [official Docker website](https://www.docker.com/get-started).

**Steps:**

1. **Download the `install.sh` Script**

   You can download the script directly using `wget` or `curl`:

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

3. **Run the Installation Script**

   ```bash
   ./install.sh
   ```

The script will perform the following actions:

- Check for Docker Installation: Ensures Docker is installed. If not, it prompts you to install Docker and exits.
- Clone the Repository: Clones the streamlit-stockwatchlist repository into a directory named streamlit-stockwatchlist.
- Build the Docker Image: Builds a Docker image named streamlit-stockwatchlist using the optimized Dockerfile.
- Create Data Directory: Creates a persistent data directory at $HOME/.stockwatchlist/data.
- Run the Docker Container: Runs the Docker container in detached mode, mapping port 8501 and mounting the data directory for persistent storage.

4. **Access the Application**

   Once the script completes, open your web browser and navigate to:

   ```
   http://localhost:8501
   ```

   You'll see the Stock Watchlist Tool up and running!

## 🔧 Manual Installation Options

### Option 1: Using Docker

If you prefer to perform the installation manually without the install.sh script, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/icon3333/streamlit-stockwatchlist.git
   cd streamlit-stockwatchlist
   ```

2. **Build the Docker Image**

   ```bash
   docker build -t streamlit-stockwatchlist .
   ```

3. **Create Data Directory**

   ```bash
   mkdir -p $HOME/.stockwatchlist/data
   ```

4. **Run the Docker Container**

   ```bash
   docker run -d \
       --name streamlit-stockwatchlist \
       -p 8501:8501 \
       -v $HOME/.stockwatchlist/data:/app/data \
       streamlit-stockwatchlist
   ```

5. **Access the Application**

   Open your browser and go to http://localhost:8501.

### Option 2: Direct Python Installation

For those who prefer not to use Docker, you can run the application directly using Python:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/icon3333/streamlit-stockwatchlist.git
   cd streamlit-stockwatchlist
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   streamlit run app.py
   ```

4. **Access the Application**

   Open your browser and navigate to http://localhost:8501.

## 💾 Data Storage

- **Docker Installation:** Data is stored in `./data` within the project directory
- **Python Installation:** Data is stored in `./data` within the project directory

## 🔄 Updates

### Docker Version

```bash
cd streamlit-stockwatchlist
git pull
docker build -t streamlit-stockwatchlist .
docker restart streamlit-stockwatchlist
```

### Python Version

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
