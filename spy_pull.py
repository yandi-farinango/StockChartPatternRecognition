import symbol
import yfinance as yf 
import csv


"""
Retrieving price history 
for all SPY companies 

"""

companies = csv.reader(open('pulled_data/companies.csv'))

for company in companies:
    print(company)

    symbol, name = company 

    history_filename = 'pulled_data/historicalSPY/{}.csv'.format(symbol)

    f = open(history_filename, 'w')

    ticker = yf.Ticker(symbol)

    df = ticker.history(period='1y')

    f.write(df.to_csv())

    f.close()