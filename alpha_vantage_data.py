import pandas as pandas
import matplotlib.pyplot as plt
import enum, time,os
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.cryptocurrencies import CryptoCurrencies

# add as enviro variable in docker setup
free_api_key=os.environ.get('ALPHA_API_KEY', '')
# up to 5 API requests per minute and 500 requests per day

ts=TimeSeries(key=free_api_key, output_format='pandas')

# output sizes are full and compact. ful is total history, compact is last 100 timestamps / datapoints
GE=ts.get_daily_adjusted('GE', outputsize='full')
GE[1]
GE[0]

# alpha vantage doesn't get adjusted for stock splits and dividends when using method get_daily. use get_daily_adjusted instead

# see what stock splits happened
GE.iloc[:,-1].value_counts()
# get timestamp of particular one
GE[GE.iloc[:,-1]==3]


# make index datetimeindex instead of string
GE.index=pd.to_datetime(GE.index)

# get 1 min data
# ts.get_intraday('MSFT',outputsize='full',interval='1min')[0]

# get batch stock quotes (most recent)
ticker_list=[]'AAPL','MSFT','FB']
stocks=ts.get_batch_stock_quotes(ticker_list)

# technical indicators

ti=TechIndicators(key=free_api_key, output_format='pandas')

sma=ti.get_sma('MSFT',interval='daily',time_period=50)[0]

bbands=ti.get_bbands('MSFT',interval='daily',time_period=50)[0]

# add close price to bollinger bands df (want to adadjusted!!)
bbands['close']=close.iloc[:,0]


macd=ti.get_macd('MSFT',interval='daily')[0]

# currencies
# supports 150 currencies

fx=ForeignExchange(key=free_api_key, output_format='pandas')

eurusd=fx.get_currency_exchange_daily('EUR','USD',outputsize='full')[0]

#intraday
fx.get_currency_exchange_intraday('EUR','USD', interval='1min', outputsize='full')[0]

# cryptocurrencies more than 500 supported
cc=CryptoCurrencies(key=free_api_key, output_format='pandas')


VTC= cc.get_digital_currency_daily(symbol='BTC',market='USD')
BTC[1]
BTC[0
