
# # import requests 
# # import json 
# # import pandas as pd 
# # import numpy as np  
# # import datetime as dt  
# # import asyncio
# # import aiohttp

# # # i=0
# # # while i<=10:

# # async def get_bars(symbol, interval="15m"):
# #     root_url = 'https://api.binance.com/api/v1/klines'
# #     url = root_url + '?symbol=' + symbol + '&interval=' + interval
# #     async with json.loads(requests.get(url).text) as data:
# #       df = pd.DataFrame(data)
# #       df.columns = ['open_time',
# #                     'Open', 'High', 'Low', 'Close', 'Volume',
# #                     'close_time', 'qav', 'num_trades',
# #                     'taker_base_vol', 'taker_quote_vol', 'ignore']
# #       df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
# #       print(df)
# #       return await df

# # # def rma(x, n, y0):
# # # 	a = (n-1) / n
# # # 	ak = a**np.arange(len(x)-1, -1, -1)
# # # 	return np.r_[np.full(14, np.nan), y0, np.cumsum(ak * x) / ak / 14 + y0 * a**np.arange(1, len(x)+1)]

# # # def dataframer():
# # #   df=(pd.DataFrame(get_bars('BTCUSDT'))).iloc[:, 1:6]
# # #   df['change'] = (df['Close'].astype(float)).diff()
# # #   df['gain'] = df.change.mask(df.change < 0, 0.0)
# # #   df['loss'] = -df.change.mask(df.change > 0, -0.0)
# # #   df['avg_gain'] = rma(df.gain[14+1:].to_numpy(), 14, np.nansum(df.gain.to_numpy()[:14+1])/14)
# # #   df['avg_loss'] = rma(df.loss[14+1:].to_numpy(), 14, np.nansum(df.loss.to_numpy()[:14+1])/14)
# # #   df['rs'] = df.avg_gain / df.avg_loss
# # #   df['rsi_14'] = 100 - (100 / (1 + df.rs))
# # #   print(df['rsi_14'][499])
# # # dataframer()


# # asyncio.run(get_bars('BTCUSDT'))









# # import asyncio

# # # from binance import AsyncClient


# # # async def main():

# # #     client = await AsyncClient.create()
# # #     exchange_info = await client.get_exchange_info()
# # #     tickers = await client.get_all_tickers()

# # if __name__ == "__main__":

# #     loop = asyncio.get_event_loop()
# #     loop.run_until_complete(main())

# # from binance import AsyncClient, BinanceSocketManager


# # async def kline_listener(client):
# #     bm = BinanceSocketManager(client)
# #     async with bm.kline_socket(symbol='BTCUSDT') as stream:
# #         while True:
# #             res = await stream.recv()
# #             print(res)

# # async def main():

# #     client = await AsyncClient.create()
# #     await kline_listener(client)
# # asyncio.run(main())

# import asyncio
# from binance import AsyncClient, BinanceSocketManager


# async def kline_listener(client):
#     bm = BinanceSocketManager(client)
#     symbol = 'BNBBTC'
#     res_count = 0
#     async with bm.kline_socket(symbol=symbol) as stream:
#         while True:
#             res = await stream.recv()
#             res_count += 1
#             print(res)
#             if res_count == 5:
#                 res_count = 0
#                 order_book = await client.get_order_book(symbol=symbol)
#                 print(order_book)
# # client= await AsyncClient.create()
# # asyncio.run(kline_listener(client))





# async def main():
#     client = await AsyncClient.create()
#     # exchange_info = await client.get_exchange_info()
#     # tickers = await client.get_all_tickers()

# if __name__ == "__main__":

#     loop = asyncio.get_event_loop()
#     asyncio.run(main())
#     # loop.run_until_complete(main())






# api_secret='bb7jnEQSd1YImgv0fGKWAJ6DGRoUuDLNBwSVEWht4FeQtheUhcmE9u5r3UbRT999'
# api_key='yVZwnOpRSnY7g2wVUyXbcKZ8YDX2G5BThVFiM8AP73ywI6XzFTpefcmJC6aQgqZv'

# import asyncio
# from binance.client import Client
# from binance import AsyncClient
# client = Client('yVZwnOpRSnY7g2wVUyXbcKZ8YDX2G5BThVFiM8AP73ywI6XzFTpefcmJC6aQgqZv', 'bb7jnEQSd1YImgv0fGKWAJ6DGRoUuDLNBwSVEWht4FeQtheUhcmE9u5r3UbRT999')
# async def main():

#     # initialise the client
#     client = await AsyncClient.create(api_key, api_secret)

# if __name__ == "__main__":

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())




import asyncio
from binance import AsyncClient

async def main():
    client = await AsyncClient.create()

    # fetch exchange info
    res = await client.get_exchange_info()
    print(json.dumps(res, indent=2))

    await client.close_connection()

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())