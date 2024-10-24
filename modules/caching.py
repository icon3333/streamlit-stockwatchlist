import datetime
from modules.database_manager import (
    get_all_stocks,
    add_stock,
    get_metadata,
    set_metadata
)
from modules.data_fetcher import fetch_stock_data

REFRESH_INTERVAL_HOURS = 24

def check_and_refresh_data():
    last_refresh_str = get_metadata('last_refresh')
    if last_refresh_str:
        last_refresh = datetime.datetime.fromisoformat(last_refresh_str)
    else:
        last_refresh = None

    now = datetime.datetime.now()

    if not last_refresh or (now - last_refresh).total_seconds() >= REFRESH_INTERVAL_HOURS * 3600:
        # Refresh data
        stocks = get_all_stocks()
        for _, row in stocks.iterrows():
            ticker_symbol = row['ticker_symbol']
            stock_data_list = fetch_stock_data(ticker_symbol)
            if stock_data_list:
                stock_data = stock_data_list[0]
                add_stock(stock_data)
        # Update last refresh time
        set_metadata('last_refresh', now.isoformat())
        return True
    else:
        return False
