import pandas as pandas
import yfinance as yf
import matplotlib.pyplot as plt
import enum, time

class stocks (enum.Enum):
    general_electric = 'GE'
    apple = 'AAPL'

class indexes (enum.Enum):
    dow_jones_index='^DJI'
    s_and_p_500='^GSPC'
    total_return_dow_jones_index='^DJITR'
    total_return_s_and_p_500='^GSPCTR'

# EUROUSD is 1 euro=X USD
class currencies (enum.Enum):
    euro_usd='EURUSD=X'
    usd_euro='USDEUR=X'

class cryptocurrencies (enum.Enum):
    btc_usd='BTC-USD'
    eth_usd='ETH-USD'

class etf (enum.Enum):
    iShares_20_year_treasury='TLT'

class treasury_yield (enum.Enum):
    us_10_year='^TNX'
    us_5_year='^FVX'

def download_yahoo_data_start_end(tickers, start_date=None, end_date=None, interval='1d', prepost=False, actions=True):
    """
    get yahoo finance data for a list of tickers.
    By default get entire history unless star,end dates specified.

    interval can be 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    Can only get
    Arguments: 7 days worth of 1m granularity
        tickers {list} -- list of tickers
        start_date {str} -- start date for data
        end_date {str} -- end date for data

    Returns:
        dataframe -- historical data for the ticker
    """
    return yf.download(tickers, start=start_date, end=end_date)

def download_yahoo_data_period(tickers, period,interval='1d', prepost=False,actions=True),:
    """
    get yahoo finance data for a list of tickers.
    By default get entire history unless star,end dates specified.

    periods are: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    Arguments:
        tickers {list} -- list of tickers
        start_date {str} -- start date for data
        end_date {str} -- end date for data

    Returns:
        dataframe -- historical data for the ticker
    """
    return yf.download(tickers, period=period)


AAPL=download_yahoo_data(['AAPL'])
AAPL.describe()
print(AAPL.tail())

#adj close prices backward adjusted for dividends
# yahoo already backward adjusts for stock splits
AAPL[AAPL['Dividends']>0]

pd.read_csv('AAPL.csv',parse_dates=['Date'],index_col='Date')

# for multiple stocks can use group_by='Ticker' to group by ticker instad of the columns

#! Normalize Prices
norm= index_df.div(index_df.iloc[0]).mul(100)



#! get ticker object
apple_ticker=yf.Ticker('AAPL')
# download method is better than history...
apple_ticker.history()

df=pd.series(apple_ticker.info, name=apple).to_frame().T

ticker=['MSFT','AAPL']

# add more rows to dataframe for key info of stocks
[df.loc[f"{i}"]=pd.Series(yf.Ticker(i).info) for i in ticker]

apple_ticker.balance_sheet
apple_ticker.financials
apple_ticker.cashflow

for i in ticker:
    yf.Ticker(i).financials.to_csv(f"{i}.csv")

#! get put call options
calls=apple_ticker.option_chain()[0]
puts=apple_ticker.option_chain()[1]


#! example of streaming real time data
while True:
    time.sleep(60)
    data=yf.download('EURUSD=X',interval='1m',period='1d')
    print(data.index[-1],data.iloc[-1,3])
