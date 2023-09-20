
import streamlit as st
import json
import plotly.graph_objects as go

def display_data(df):
    """
    Displays the data in a table and JSON format, only including the "DATE", "SALE", "BUY", "LOW", and "CLOSE" columns.

    Parameters:
    df (pd.DataFrame): The data as a pandas DataFrame.
    """
    selected_columns = ["DATE", "SALE", "BUY", "LOW", "CLOSE"]
    df_html = df[selected_columns].to_html(classes="table-center", escape=False)
    st.markdown(df_html, unsafe_allow_html=True)
    st.title("JSON")
    json_data = df[selected_columns].to_json(orient="records", date_format="iso")
    pretty_json = json.dumps(json.loads(json_data), indent=4)
    st.code(pretty_json, language="json")

def plot_data(df):
    """
    Creates and displays a plot of the data.

    Parameters:
    df (pd.DataFrame): The data as a pandas DataFrame.
    """
    fig = go.Figure(data=[go.Candlestick(x=df["DATE"], open=df["SALE"], high=df["SALE"], low=df["LOW"], close=df["CLOSE"])])
    fig.update_layout(title="CRC/USD Prices", xaxis_title="Date", yaxis_title="Price (in colones)")
    st.plotly_chart(fig)
