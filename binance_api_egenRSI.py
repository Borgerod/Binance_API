import requests 
import json 
import pandas as pd 
import numpy as np  
import datetime as dt  

def get_bars(symbol, interval="15m"):
    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df.columns = ['open_time',
                  'Open', 'High', 'Low', 'Close', 'Volume',
                  'close_time', 'qav', 'num_trades',
                  'taker_base_vol', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    return df

def rma(x, n, y0):
	a = (n-1) / n
	ak = a**np.arange(len(x)-1, -1, -1)
	return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]

def dataframer():
  df = (pd.DataFrame(get_bars('BTCUSDT'))).iloc[:, 1:6]
  df['change'] = (df['Close'].astype(float)).diff()
  df['gain'] = df.change.mask(df.change < 0, 0.0)
  df['loss'] = -df.change.mask(df.change > 0, -0.0)
  df['avg_gain'] = rma(df.gain[14+1:].to_numpy(), 14, np.nansum(df.gain.to_numpy()[:14+1])/14)
  df['avg_loss'] = rma(df.loss[14+1:].to_numpy(), 14, np.nansum(df.loss.to_numpy()[:14+1])/14)
  df['rs'] = df.avg_gain / df.avg_loss
  df['rsi_14'] = 100 - (100 / (1 + df.rs))
  return df

def main():
    print(f"{round(dataframer()['rsi_14'][499],2)}%")

if __name__ == '__main__':
    i=0
    while i<=10:
        main()
