# Stock Watchlist Tool

A simple Streamlit application to maintain a stock watchlist with key financial metrics. Data is fetched using the `yfinance` API and stored locally using SQLite.

## Features

- **Add Stocks:** Input ticker symbols to add stocks to your watchlist.
- **View Watchlist:** Displays key metrics for each stock.
- **Edit Themes:** Customize the 'theme' column to group stocks.
- **Group Stocks:** Group stocks by any column, including numerical columns divided into quintiles.
- **Automatic Data Refresh:** Data is refreshed every 24 hours to ensure up-to-date information.

## Requirements

- Python 3.x
- See `requirements.txt` for Python dependencies.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/stock-watchlist-tool.git
   cd stock-watchlist-tool
