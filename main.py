import yfinance as yf 
import pandas as pd 

pizza = yf.Ticker('AAPL')

dataframe = pizza.history(period='1y')

print(dataframe.to_csv())