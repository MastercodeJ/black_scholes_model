from datetime import datetime, date
import numpy as np
import pandas as pd
import yfinance as yf

def download_return(stock):
    yf_df = yf.Ticker(stock)
    df = yf_df.history(period ='1y') 
    df = df.sort_values(by="Date")
    df = df.dropna()
    df = df.assign(close_day_before=df.Close.shift(1))
    df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)
    sigma = np.sqrt(252) * df['returns'].std()
    return sigma, df['Close'].iloc[-1]

def download_risk_free():
    yf_df = yf.Ticker('^TNX')
    risk_rate = yf_df.history(period ='1d')['Close'].iloc[-1]/100
    return risk_rate
