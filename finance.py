import yfinance as yf

def get_stock_price(ticker):
    """
    Fetch the current stock price for the given ticker.

    :param ticker: Stock ticker (string)
    :return: Current price of the stock (float) or 0 if not found.
    """
    stock = yf.Ticker(ticker)

    # Fetch stock price from Yahoo Finance
    try:
        current_price = stock.history(period="1m")['Close'].iloc[-1]
    except (IndexError, KeyError):
        try:
            current_price = stock.fast_info['lastPrice']
        except (IndexError, KeyError, AttributeError):
            current_price = 0  # Default if data retrieval fails
    
    return current_price
