import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the price of a European option using the Black-Scholes formula.

    :param S: Current stock price (float)
    :param K: Strike price (float)
    :param T: Time to expiration in years (float)
    :param r: Risk-free interest rate (float)
    :param sigma: Volatility of the stock (float)
    :param option_type: 'call' or 'put' (str)
    :return: Price of the option (float)
    """
    # Calculate d1 and d2 using the Black-Scholes formula
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Option price calculation based on the option type
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return price
