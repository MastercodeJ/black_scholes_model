import math
from scipy.stats import norm
import numpy as np
from .data_process import download_return, download_risk_free


def black_scholes_call( K, T, ticker):
    sigma, price = download_return(ticker)
    risk_free_rate = download_risk_free()
    time = T/365
    d1 = (math.log(price / K) + (risk_free_rate + 0.5 * sigma**2) * time) / (sigma * math.sqrt(time))
    d2 = d1 - sigma * math.sqrt(time)
    call_price = price * norm.cdf(d1) - K * math.exp(-risk_free_rate * time) * norm.cdf(d2)
    return call_price, price, K, risk_free_rate, T, sigma

def black_scholes_put(K, T, ticker):
    sigma, price = download_return(ticker)
    risk_free_rate = download_risk_free()
    time = T/365
    d1 = (math.log(price / K) + (risk_free_rate + 0.5 * sigma**2) * time) / (sigma * math.sqrt(time))
    d2 = d1 - sigma * math.sqrt(time)
    put_price = K * math.exp(-risk_free_rate * time) * norm.cdf(-d2) - price * norm.cdf(-d1)
    return put_price, price, K, risk_free_rate, T, sigma
