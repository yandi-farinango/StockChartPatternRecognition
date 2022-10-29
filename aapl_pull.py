import yfinance as yf 
import pandas as pd 

data = yf.Ticker('AAPL')

dataframe = data.history(period='1y')

print(dataframe.to_csv())