"""
Expanding AAPL.py
we'll run a script to highlight 
bullish engulfing patterns 
in all SP500 companies 

"""

from candlestick_patterns import * 

companies_file = open('pulled_data/companies.csv')

companies = csv.reader(companies_file)

for company in companies:
    # print(company)

    ticker, name = company

    history_file = open('pulled_data/historicalSPY/{}.csv'.format(ticker))

    reader = csv.DictReader(history_file)
    spy_candles = list(reader)

    spy_candles = spy_candles[-2:]

    if len(spy_candles) > 1:
        if is_bullish_engulfing(spy_candles, 1):
            print('{} - {} is bullish engulfing'.format(ticker, spy_candles[1]['Date']))

        if is_bearish_engulfing(spy_candles, 1):
            print('{} - {} is bearish engulfing'.format(ticker, spy_candles[1]['Date']))
        

