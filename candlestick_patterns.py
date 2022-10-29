import csv 

def is_bullish_candle(candle):
    """
    Bullish Candle: 
    Day's Close > Day's Open
    """
    return float(candle['Close']) > float(candle['Open'])


def is_bearish_candle(candle):
    """
    Bearish Candle: 
    Day's Close < Day's Open
    """
    return float(candle['Close']) < float(candle['Open'])


def is_bullish_engulfing(candles, index):
    """
    Bullish Engulfing: 
    - opens lower than previous day's close  
    - closes above previous candle open 
    """
    current_day = candles[index]
    previous_day = candles[index-1] 

    # Conditions Above 
    if is_bearish_candle(previous_day)\
        and float(current_day['Close']) > float(previous_day['Open'])\
        and float(current_day['Open']) < float(previous_day['Close']):
        return True


def is_bearish_engulfing(candles, index):
    """
    Bearish Engulfing 
    - opens above previous days close 
    - closes below previous days open 
    """
    current_day = candles[index]
    previous_day = candles[index-1]

    # Conditions above 
    if is_bullish_candle(previous_day)\
        and float(current_day['Open']) > float(previous_day['Close'])\
        and float(current_day['Close']) < float(previous_day['Open']):
        return True 





