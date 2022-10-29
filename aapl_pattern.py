from candlestick_patterns import * 

with open('pulled_data/AAPL.csv') as f:
    reader = csv.DictReader(f)
    print(reader)
    candles = list(reader)

for i in range(1, len(candles)):
    print(candles[i])

    if is_bullish_engulfing(candles, i):
        print('{} is Bullish'.format(candles[i]['Date']))

    if is_bearish_engulfing(candles, i):
        print('{} is Bearish'.format(candles[i]['Date']))