import pandas as pd
from pandas.core.frame import DataFrame
import pandas_ta 
import talib as ta 
import yfinance as yf
import datetime as dt

# ta-lib documentation: https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#others-indicators

# GLOBAL variables
df = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close', 'volume'])
ticker = ""

# TODO we need more than just the last value for each indicator
    # need to compare with nth and (n+i)th last values
    # last value alone is useless most likely
    #

# So that dataframe info is not truncated in terminal output during testing
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

numDays = 5
# If ticker is correct and data is still not downloading, check start and end dates. 
today = dt.datetime.today().strftime('%Y-%m-%d')
startDate = (dt.datetime.today()-dt.timedelta(numDays)).strftime('%Y-%m-%d')

def getRecentData(company_name):
    global df
    global ticker

    ticker = company_name
    stock = yf.Ticker(company_name)
    df = stock.history(period="1d", interval="15m", start=startDate, end=today, actions=False)

    print("{} data has been received".format(company_name))

    df['rsi'] = df.ta.rsi()
    # Momentum (+ is uptrend, - is downtrend)
    df['mom'] = df.ta.mom()
    # Ease of Movement: When + and rising, price is increasing on low volume, while - and falling, price is dropping on low volume.
    df['eom'] = df.ta.eom()
    # Awesome Oscialltor: measures market momentum by comparing two MAs (5 and 34 period)
    df['awesome'] = df.ta.ao()
    # Mass Index: when the figure jumps above 27—creating a “bulge”—and then drops below 26.5, the stock is ready to change course
    df['mi'] = df.ta.massi()

    lastClose = df['close'][-1]
    lastRSI = round(df['rsi'][-1], 3)
    lastMOM = round(df['mom'][-1], 3)
    lastEOM =  round(df['eom'][-1], 3)
    lastAwesome = round(df['awesome'][-1], 3)
    lastMassIndex = round(df['mi'][-1], 3)

    data = [('Last Price', lastClose), ('RSI', lastRSI), ('Momentum', lastMOM), ('Ease of Movement', lastEOM), 
    ('Awesome Index', lastAwesome), ('Mass Index', lastMassIndex)]
    
    return data


# print(getRecentData("TSLA"))
