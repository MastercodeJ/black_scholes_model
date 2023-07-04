import math
from scipy.stats import norm

def black_scholes_call(S, K, r, T, sigma):
    print(S, K, r, T, sigma)
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price 

def black_scholes_put(S, K, r, T, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

# # Example usage
# S = 100  # Current stock price
# K = 100  # Strike price
# r = 0.05  # Risk-free interest rate
# T = 1  # Time to expiration (in years)
# sigma = 0.2  # Volatility

# put_price = black_scholes_put(S, K, r, T, sigma)
# print("Put Price:", put_price)

# # Example usage
# S = 100  # Current stock price
# K = 1  # Strike price
# r = 0.05  # Risk-free interest rate
# T = 1  # Time to expiration (in years)
# sigma = 0.2  # Volatility

# call_price = black_scholes_call(S, K, r, T, sigma)
# print("Call Price:", call_price)