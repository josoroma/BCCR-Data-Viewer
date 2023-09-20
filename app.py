
from data_processing import get_date_inputs, fetch_data, process_data
from visualization import display_data, plot_data
from utils import construct_url, add_custom_css
from settings import logging
from datetime import datetime, timedelta
import streamlit as st

def main():
    """
    The main function that orchestrates the execution of other functions to display the BCCR data viewer.
    """
    st.title("BCCR Data Viewer")
    current_date = datetime.now()
    start_date_default = current_date - timedelta(days=7)
    end_date_default = current_date

    start_date, end_date = get_date_inputs(start_date_default, end_date_default)
    if start_date and end_date:
        url = construct_url(start_date, end_date)
        try:
            df = fetch_data(url)
            if df is not None:
                plot_data(df)
                display_data(df) 
            else:
                st.write("No tables found in the HTML.")
        except Exception as e:
            logging.error("An error occurred while fetching the data: %s", e)
            st.write("An error occurred while fetching the data.")
    else:
        st.write("Please select valid dates.")

    add_custom_css()

if __name__ == "__main__":
    main()
