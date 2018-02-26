import pandas as pd 
import numpy as np 
import pandas_datareader as data
import datetime as dt
import matplotlib.pyplot as plt    
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

ticker = 'AAPL'
begdate = dt.datetime(2017, 1, 1)
enddate = dt.datetime(2018, 1, 2)
data1 = data.DataReader(ticker,'google',begdate,enddate)
aapl_df = pd.DataFrame(data1)
date_df = pd.to_datetime(list(aapl_df.index))
adj_close_df = list(aapl_df)
plt.plot(date_df, aapl_df)
plt.title("Apple")
plt.xlabel("Date")
plt.ylabel("Dollars")
plt.show()