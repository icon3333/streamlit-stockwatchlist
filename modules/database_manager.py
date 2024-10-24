import sqlite3
import pandas as pd
import os

DB_PATH = 'data/watchlist.db'

def get_connection():
    # Ensure the 'data' directory exists and the database is initialized
    if not os.path.exists('data'):
        os.makedirs('data')
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS watchlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker_symbol TEXT UNIQUE NOT NULL,
            company_name TEXT,
            market_cap REAL,
            country TEXT,
            industry TEXT,
            full_time_employees INTEGER,
            website TEXT,
            currency TEXT,
            total_debt REAL,
            total_cash REAL,
            quick_ratio REAL,
            debt_to_equity REAL,
            pe_ratio REAL,
            price_to_book REAL,
            price_to_sales REAL,
            ev_ebitda REAL,
            operating_margin REAL,
            profit_margin REAL,
            gross_margin REAL,
            return_on_assets REAL,
            return_on_equity REAL,
            operating_cash_flow REAL,
            free_cash_flow REAL,
            fcf_sales_ratio REAL,
            dividend_yield REAL,
            theme TEXT DEFAULT ''
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_stock(stock_data):
    conn = get_connection()
    cursor = conn.cursor()
    columns = ', '.join(stock_data.keys())
    placeholders = ', '.join(['?'] * len(stock_data))
    sql = f'INSERT OR REPLACE INTO watchlist ({columns}) VALUES ({placeholders})'
    cursor.execute(sql, list(stock_data.values()))
    conn.commit()
    conn.close()

def remove_stock(ticker_symbol):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM watchlist WHERE ticker_symbol = ?', (ticker_symbol,))
    conn.commit()
    conn.close()

def update_theme(ticker_symbol, theme):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE watchlist SET theme = ? WHERE ticker_symbol = ?', (theme, ticker_symbol))
    conn.commit()
    conn.close()

def get_all_stocks():
    conn = get_connection()
    df = pd.read_sql_query('SELECT * FROM watchlist', conn)
    conn.close()
    return df

def get_metadata(key):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM metadata WHERE key = ?', (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def set_metadata(key, value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)', (key, value))
    conn.commit()
    conn.close()

def is_ticker_in_watchlist(ticker_symbol):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM watchlist WHERE ticker_symbol = ?', (ticker_symbol,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
