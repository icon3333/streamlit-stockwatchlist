import yfinance as yf

def fetch_stock_data(ticker_symbol):
    ticker_symbol = ticker_symbol.upper()
    ticker = yf.Ticker(ticker_symbol)

    try:
        info = ticker.info
    except Exception:
        return None

    if 'shortName' not in info:
        return None

    stock_data = {
        'ticker_symbol': ticker_symbol,
        'company_name': info.get('shortName', ''),
        'market_cap': info.get('marketCap', 0),
        'country': info.get('country', ''),
        'industry': info.get('industry', ''),
        'full_time_employees': info.get('fullTimeEmployees', 0),
        'website': info.get('website', ''),
        'currency': info.get('currency', ''),
        'total_debt': info.get('totalDebt', 0),
        'total_cash': info.get('totalCash', 0),
        'quick_ratio': info.get('quickRatio', 0),
        'debt_to_equity': info.get('debtToEquity', 0),
        'pe_ratio': info.get('trailingPE', 0),
        'price_to_book': info.get('priceToBook', 0),
        'price_to_sales': info.get('priceToSalesTrailing12Months', 0),
        'ev_ebitda': info.get('enterpriseToEbitda', 0),
        'operating_margin': info.get('operatingMargins', 0),
        'profit_margin': info.get('profitMargins', 0),
        'gross_margin': info.get('grossMargins', 0),
        'return_on_assets': info.get('returnOnAssets', 0),
        'return_on_equity': info.get('returnOnEquity', 0),
        'operating_cash_flow': info.get('operatingCashflow', 0),
        'free_cash_flow': info.get('freeCashflow', 0),
        'fcf_sales_ratio': 0,  # Placeholder
        'dividend_yield': info.get('dividendYield', 0),
        'theme': ''
    }

    # Calculate FCF/Sales Ratio if possible
    total_revenue = info.get('totalRevenue', None)
    if stock_data['free_cash_flow'] and total_revenue:
        stock_data['fcf_sales_ratio'] = stock_data['free_cash_flow'] / total_revenue

    return [stock_data]
