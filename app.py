import streamlit as st
import pandas as pd
import os

from modules.data_fetcher import fetch_stock_data
from modules.database_manager import (
    create_tables,
    add_stock,
    remove_stock,
    update_theme,
    get_all_stocks,
    is_ticker_in_watchlist
)
from modules.caching import check_and_refresh_data
from utils.grouping import group_data
from utils.helpers import display_stock_selection

# Set layout to wide
st.set_page_config(layout="wide")

# Initialize database tables
create_tables()

# Check and refresh data if needed
if check_and_refresh_data():
    st.info("Data refreshed successfully.")

st.title("Stock Watchlist Tool")

# Manage Your Watchlist Section with Expander
with st.expander("# Manage Your Watchlist", expanded=True):
    # Create two columns for input, and remove sections
    col1, col2 = st.columns([1, 1])

    # Column 1: Ticker Input and CSV Upload
    with col1:
        # Row 1: Ticker Input
        ticker_input = st.text_input("Enter a ticker symbol (e.g., AAPL):").strip().upper()
        if st.button("Add Stock", key="add_stock"):
            if ticker_input:
                if is_ticker_in_watchlist(ticker_input):
                    st.warning("Ticker already in watchlist.")
                else:
                    possible_matches = fetch_stock_data(ticker_input)
                    if not possible_matches:
                        st.error("No matching stocks found.")
                    elif len(possible_matches) == 1:
                        stock_data = possible_matches[0]
                        add_stock(stock_data)
                        st.success(f"Added {stock_data['company_name']} ({stock_data['ticker_symbol']}) to your watchlist.")
                    else:
                        # Multiple matches found
                        selected_stock = display_stock_selection(possible_matches)
                        if selected_stock:
                            add_stock(selected_stock)
                            st.success(f"Added {selected_stock['company_name']} ({selected_stock['ticker_symbol']}) to your watchlist.")
            else:
                st.warning("Please enter a ticker symbol.")

        # Row 2: Upload CSV to Add Multiple Tickers
        uploaded_file = st.file_uploader("Choose a CSV file with a single column 'ticker_symbol'", type="csv")

        if uploaded_file:
            try:
                # Read the CSV
                df = pd.read_csv(uploaded_file)

                # Validate that it contains the required column
                if 'ticker_symbol' not in df.columns:
                    st.error("The CSV must contain a column named 'ticker_symbol'.")
                else:
                    # Initialize lists to track results
                    added_tickers = []
                    skipped_tickers = []
                    invalid_tickers = []

                    for ticker in df['ticker_symbol'].unique():
                        ticker = ticker.strip().upper()  # Normalize ticker symbols to uppercase
                        if is_ticker_in_watchlist(ticker):
                            skipped_tickers.append(ticker)
                        else:
                            possible_matches = fetch_stock_data(ticker)
                            if not possible_matches:
                                invalid_tickers.append(ticker)
                            elif len(possible_matches) == 1:
                                stock_data = possible_matches[0]
                                add_stock(stock_data)
                                added_tickers.append(ticker)
                            else:
                                skipped_tickers.append(ticker)  # Skipping ambiguous tickers

                    # Display results
                    if added_tickers:
                        st.success(f"Successfully added: {', '.join(added_tickers)}")
                    if skipped_tickers:
                        st.info(f"Skipped duplicates or ambiguous tickers: {', '.join(skipped_tickers)}")
                    if invalid_tickers:
                        st.error(f"Invalid or not found tickers: {', '.join(invalid_tickers)}")

            except Exception as e:
                st.error(f"Error reading CSV: {e}")

    # Column 3: Remove Ticker
    with col2:
        watchlist_df = get_all_stocks()
        if not watchlist_df.empty:
            remove_ticker = st.selectbox("Select a stock to remove:", watchlist_df['ticker_symbol'])
            if st.button("Remove Stock", key="remove_stock"):
                remove_stock(remove_ticker)
                st.success(f"Removed {remove_ticker} from your watchlist.")
                st.experimental_rerun()
        else:
            st.write("Your watchlist is currently empty.")


# Section: Display Watchlist
st.header("Your Watchlist")
if not watchlist_df.empty:
    # Reorder columns to place 'theme' just after 'industry'
    columns_order = (
        ['ticker_symbol', 'company_name', 'market_cap', 'country', 'industry', 'theme'] + 
        [col for col in watchlist_df.columns if col not in ['ticker_symbol', 'company_name', 'market_cap', 'country', 'industry', 'theme']]
    )
    watchlist_df = watchlist_df[columns_order]

    # Display table with only the 'theme' column editable
    editable_columns = ['theme']

    # Display only 'theme' as editable in the data editor
    edited_df = st.data_editor(
        watchlist_df.set_index('ticker_symbol'),
        use_container_width=True,
        num_rows="dynamic",
        key="watchlist_editor",
        disabled=[col for col in watchlist_df.columns if col not in editable_columns]
    )

    # Create two columns for the buttons
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Update themes in the database
    with col1:
        if st.button("Save Changes"):
            for ticker in edited_df.index:
                new_theme = edited_df.at[ticker, 'theme']
                update_theme(ticker, new_theme)
            st.success("Themes updated successfully.")
            st.rerun()
    
    # Add Export to CSV button in the second column
    with col2:
        csv = watchlist_df.to_csv(index=False)
        st.download_button(
            label="📥 Export Watchlist to CSV",
            data=csv,
            file_name="stock_watchlist.csv",
            mime="text/csv"
        )

# Section: Grouped Stocks
st.header("Grouped Stocks")
if not watchlist_df.empty:
    grouping_column = st.selectbox(
        "Select a column to group by:",
        options=watchlist_df.columns.drop(['id'])
    )
    grouped_data = group_data(watchlist_df, grouping_column)
    for group_name, group_df in grouped_data.items():
        st.subheader(f"Group: {group_name}")
        st.dataframe(group_df.drop(columns=['id']), use_container_width=True)