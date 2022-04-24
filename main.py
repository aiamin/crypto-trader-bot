import pandas as pd
import pandas_ta
import ccxt
import schedule


exchange = ccxt.binance()
symbol = 'BTC/USDT'
interval = '5m'

def get_ohlcv(symbol, interval, limit=1000) -> pd.DataFrame:

    # headers
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

    # get candles from exchange
    bars = exchange.fetch_ohlcv(symbol, timeframe=interval, limit=limit)

    # convert list of list to pandas dataframe
    df = pd.DataFrame(bars, columns=columns)

    # convert millisecond to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    return df


