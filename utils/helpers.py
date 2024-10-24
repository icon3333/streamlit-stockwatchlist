import streamlit as st

def display_stock_selection(stock_list):
    options = []
    for idx, stock in enumerate(stock_list):
        option = f"{stock['company_name']} ({stock['ticker_symbol']}) - {stock['industry']} - Market Cap: {stock['market_cap']}"
        options.append((option, idx))
    selection = st.selectbox("Multiple matches found. Please select one:", [opt[0] for opt in options])
    selected_index = next(idx for opt, idx in options if opt == selection)
    return stock_list[selected_index]
