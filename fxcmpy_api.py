import pandas as pandas
import matplotlib.pyplot as plt
import enum, time, os
import fxcmpy

# fxcmpy gives bids and asks

# add as enviro variable in docker setup
fxcmpy_token=os.environ.get('FXCM_API_KEY', '')

api=fxcmpy.fxcmpy(access_token=fxcmpy_token,log_level='error')

api.get_instruments()

api.get_candles('EUR/USD')

# daily data
api.get_candles('EUR/USD', period='D1')
# minute data
api.get_candles('EUR/USD', period='m1')

# number must be between 0 and 10K
api.get_candles('EUR/USD', period='D1', number=10000)
api.get_candles('EUR/USD', start='2019-01-01',end='2020-01-01' )


# stock indexes
api.get_candles('SPX500', period='D1', number=10000)

# commodities
api.get_candles('XAU/USD', period='D1', number=10000)

#cryptos
api.get_candles('BTC/USD', period='D1', number=10000)


#streaming real time data

# the subscribe market data offers a callback as a paremeter, so this can be tied to some other process of storing the data
api.subscribe_market_data('EUR/USD')

api.get_unsubscribed_symbols()

while True:
    time.sleep(1)
    print(api.get_last_price('EUR/USD').name, api.get_last_prices('EUR/USD').Ask)

api.unsubscribe_market_data('EUR/USD')

api.get_subscribed_symbols()
#disconnect from api
api.close()

