import streamlit as st

def construct_url(start_date, end_date):
    """
    Constructs the URL with the selected dates.

    Parameters:
    start_date (date): The selected start date.
    end_date (date): The selected end date.

    Returns:
    str: The constructed URL as a string.
    """
    return f"https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?CodCuadro=400&Idioma=1&FecInicial={start_date.strftime('%Y/%m/%d')}&FecFinal={end_date.strftime('%Y/%m/%d')}&Filtro=0&Exportar=True"

def add_custom_css():
    """
    Adds custom CSS to the Streamlit app.
    """
    st.markdown("""
    <style>
    .table-center {
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)
