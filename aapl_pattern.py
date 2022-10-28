import csv 

def is_bearish_candlestick(candle):
    """
    Bearish Candle: 
    Day's Close < Day's Open
    """
    return candle['Close'] < candle['Open']



def is_bullish_engulfing(candles, index):
    """
    Bullish Engulfing: 
    - opens lower than previous day's close  
    - closes above previous candle open 
    """

    current_day = candles[index]
    previous_day = candles[index-1] 

    # Conditions Above 
    if is_bearish_candlestick(previous_day)\
        and current_day['Close'] > previous_day['Open']\
        and current_day['Open'] < previous_day['Close']:
        return True


with open('AAPL.csv') as f:
    reader = csv.DictReader(f)
    print(reader)
    candles = list(reader)

for i in range(1, len(candles)):
    print(candles[i])

    if is_bullish_engulfing(candles, i):
        print('{} is Bullish'.format(candles[i]['Date']))




