# Description: This is a stock market dashboard to show some charts on some stock

# Libraries imports
import streamlit as st
import pandas as pd
from PIL import Image

# Add a title and an image
st.write("""
# Crypto Market Analysis
**Visually** Show Data on a Stock! Date Range from 3rd of March, 2016
to 25th of June, 2021
""")

image = Image.open("C:/Users/30694/PycharmProjects/pythonProject/crypto_analysis.jpg")
st.image(image, use_column_width=True)

# Create a sidebar header
st.sidebar.header('User Input')


# Get the User's Input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2021-06-01")
    end_date = st.sidebar.text_input("End Date", "2021-06-25")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "BTC")
    return start_date, end_date, stock_symbol


# Create a function to get the crypto
def get_crypto_name(symbol):
    if symbol == 'BTC':
        return 'BTC'
    elif symbol == 'ETH':
        return 'ETH'
    else:
        return 'None'


# Create a function to get the proper crypto data and the proper timeframe
def get_data(symbol, start, end):
    # Load the data
    if symbol.upper() == 'BTC':
        df = pd.read_csv("C:/Users/30694/PycharmProjects/pythonProject/Stocks/BTC-EUR.csv")
    elif symbol.upper() == 'ETH':
        df = pd.read_csv("C:/Users/30694/PycharmProjects/pythonProject/Stocks/ETH-EUR.csv")
    else:
        df = pd.DataFrame(
            columns=['unix', 'date', 'symbol', 'open', 'high', 'low', 'close', 'Volume EUR', 'Volume BTC'])
    #Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    #Set the start and end index rows both to 0
    start_row = 0
    end_row = 0

    #find dates
    for i in df.itertuples():
        if pd.to_datetime(i[2]) == start:

            start_row = i[0]

        if pd.to_datetime(i[2]) == end:

            end_row = i[0]




    return df.iloc[end_row:start_row, :]

#Get the user's inputs
start, end, symbol = get_input()
#Get the data
df = get_data(symbol, start, end)
#Get company name
coin_name = get_crypto_name(symbol.upper())

#Display the close price
st.header(coin_name+" Close Price\n")
st.line_chart(df['close'])

#Display open price
st.header(coin_name+" Open Price\n")
st.line_chart(df['open'])

#Display High price
st.header(coin_name+" High Price\n")
st.line_chart(df['high'])

#Display low price
st.header(coin_name+" Low Price\n")
st.line_chart(df['low'])

#Display the Euro Volume
st.header(coin_name+" Volume Eur\n")
st.line_chart(df['Volume EUR'])

#Display the Btc or ETH Volume
if coin_name=='BTC':
    st.header(coin_name+" Volume Btc\n")
    st.line_chart(df['Volume BTC'])
elif coin_name=='ETH':
    st.header(coin_name+" Volume Eth\n")
    st.line_chart(df['Volume ETH'])

#Get statistics on the data
st.header('Data Statistics')
st.write(df.describe())
