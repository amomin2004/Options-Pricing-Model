import streamlit as st
from black_scholes import black_scholes
from finance import get_stock_price
from datetime import datetime

# Frontend for the Black-Scholes Calculator
st.title('Black-Scholes Option Pricing Calculator')

# Step 1: Collect stock ticker input
ticker = st.text_input('Enter Stock Ticker (e.g., AAPL):', value='AAPL')

# Step 2: Fetch current stock price
current_price = get_stock_price(ticker)
st.write(f"Current Price of {ticker}: {current_price}")

# Step 3: Gather Black-Scholes parameters
strike_price = st.number_input('Strike Price:', min_value=0.0, value=100.0, step=1.0)

# Expiration Date Picker
expiry_date = st.date_input('Expiration Date:', value=datetime.today())
expiry_years = (expiry_date - datetime.today().date()).days / 365.0  # Convert days to years

# Black-Scholes parameters
risk_free_rate = st.number_input('Risk-Free Rate (in %):', min_value=0.0, value=5.0, step=0.1) / 100
volatility = st.number_input('Volatility (in %):', min_value=0.0, value=20.0, step=0.1) / 100
option_type = st.selectbox('Option Type:', ['call', 'put'])

# Step 4: Calculate option price using Black-Scholes
if st.button('Calculate Option Price'):
    if current_price > 0:
        option_price = black_scholes(current_price, strike_price, expiry_years, risk_free_rate, volatility, option_type)
        st.write(f"The price of the {option_type} option is: ${option_price:.2f}")
    else:
        st.write("Unable to fetch stock price. Please try again.")
