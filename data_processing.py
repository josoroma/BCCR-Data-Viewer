
import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

def get_date_inputs(start_date_default, end_date_default):
    """
    Gets date inputs from the sidebar in the streamlit application.

    Parameters:
    start_date_default (datetime): The default start date.
    end_date_default (datetime): The default end date.

    Returns:
    tuple: The selected start and end dates.
    """
    start_date = st.sidebar.date_input("Start Date", start_date_default)
    end_date = st.sidebar.date_input("End Date", end_date_default)
    return start_date, end_date

def fetch_data(url):
    """
    Fetches data from the URL and returns a processed DataFrame.

    Parameters:
    url (str): The URL from which to fetch the data.

    Returns:
    pd.DataFrame: The processed data as a pandas DataFrame, or None if no tables are found.
    """
    tables = pd.read_html(url, header=0, skiprows=5)
    if tables:
        df = process_data(tables[0])
        return df

def process_data(df):
    """
    Processes the DataFrame and returns the modified version.

    Parameters:
    df (pd.DataFrame): The original data as a pandas DataFrame.

    Returns:
    pd.DataFrame: The processed data as a pandas DataFrame.
    """
    df = df.iloc[:, :3]
    df.columns = ["DATE", "SALE", "BUY"]
    df["SALE"] = df["SALE"] / 100000
    df["BUY"] = df["BUY"] / 100000
    df["SALE"] = df["SALE"].astype(str).str.replace(',', '.').astype(float) / 1000
    df["BUY"] = df["BUY"].astype(str).str.replace(',', '.').astype(float) / 1000
    df["LOW"] = df["SALE"].shift(-1)
    df["CLOSE"] = df["SALE"].shift(-1)
    df.at[df.index[-1], "LOW"] = df.at[df.index[-1], "SALE"]
    df.at[df.index[-1], "CLOSE"] = df.at[df.index[-1], "SALE"]
    return df
