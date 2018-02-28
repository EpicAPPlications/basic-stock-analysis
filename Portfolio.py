import pandas as pd 
import numpy as np 
import pandas_datareader as data
import datetime as dt
import matplotlib.pyplot as plt    
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

ticker = 'AAPL'
ticker1 = 'ACLS'
ticker2 = 'ADBE'
ticker3 = 'ADSK'
ticker4 = 'AMAT'
ticker5 = 'AMZN'
ticker6 = 'ARNC'
ticker7 = 'AVX'
ticker8 = 'AWX'
ticker9 = 'BEP'
ticker10 = 'CSBR'
ticker11 = 'CVY'
ticker12 = 'D'
ticker13 = 'DEM'
ticker14 = 'DES'
ticker15 = 'DEW'
ticker16 = 'DFE'
ticker17 = 'DGS'
ticker18 = 'DHS'
ticker19 = 'DLN'
begdate = dt.datetime(2018, 1, 1)
enddate = dt.datetime(2018, 2, 26)

#AAPL TICKER
data1 = data.DataReader(ticker,'google',begdate,enddate)
aapl_df = pd.DataFrame(data1)
date_df = pd.to_datetime(list(aapl_df.index))
adj_close_df = list(aapl_df)

#ACLS ticker
data2 = data.DataReader(ticker1,'google',begdate,enddate)
acls_df = pd.DataFrame(data2)
date_df1 = pd.to_datetime(list(acls_df.index))
adj_close_df = list(acls_df)

#ADBE ticker
data3 = data.DataReader(ticker2,'google',begdate,enddate)
adbe_df = pd.DataFrame(data3)
date_df2 = pd.to_datetime(list(adbe_df.index))
adj_close_df = list(adbe_df)

#ADSK ticker
data4 = data.DataReader(ticker3,'google',begdate,enddate)
adsk_df = pd.DataFrame(data4)
date_df3 = pd.to_datetime(list(adsk_df.index))
adj_close_df = list(adsk_df)

#AMAT ticker
data5 = data.DataReader(ticker4,'google',begdate,enddate)
amat_df = pd.DataFrame(data5)
date_df4 = pd.to_datetime(list(amat_df.index))
adj_close_df = list(amat_df)

#AMZN ticker
data6 = data.DataReader(ticker5,'google',begdate,enddate)
amzn_df = pd.DataFrame(data6)
date_df5 = pd.to_datetime(list(amzn_df.index))
adj_close_df = list(amzn_df)

#ARNC ticker
data7 = data.DataReader(ticker6,'google',begdate,enddate)
arnc_df = pd.DataFrame(data7)
date_df6 = pd.to_datetime(list(arnc_df.index))
adj_close_df = list(arnc_df)

#AVX ticker
data8 = data.DataReader(ticker7,'google',begdate,enddate)
avx_df = pd.DataFrame(data8)
date_df7 = pd.to_datetime(list(avx_df.index))
adj_close_df = list(avx_df)

#AWX ticker
data9 = data.DataReader(ticker8,'google',begdate,enddate)
awx_df = pd.DataFrame(data9)
date_df8 = pd.to_datetime(list(awx_df.index))
adj_close_df = list(awx_df)

#BEP ticker
data10 = data.DataReader(ticker9,'google',begdate,enddate)
bep_df = pd.DataFrame(data10)
date_df9 = pd.to_datetime(list(bep_df.index))
adj_close_df = list(bep_df)

#CSBR ticker
data11 = data.DataReader(ticker10,'google',begdate,enddate)
csbr_df = pd.DataFrame(data11)
date_df10 = pd.to_datetime(list(csbr_df.index))
adj_close_df = list(csbr_df)

#CVY ticker
data12 = data.DataReader(ticker11,'google',begdate,enddate)
cvy_df = pd.DataFrame(data12)
date_df11 = pd.to_datetime(list(cvy_df.index))
adj_close_df = list(cvy_df)

#D ticker
data13 = data.DataReader(ticker12,'google',begdate,enddate)
d_df = pd.DataFrame(data13)
date_df12 = pd.to_datetime(list(d_df.index))
adj_close_df = list(d_df)

#DEM ticker
data14 = data.DataReader(ticker13,'google',begdate,enddate)
dem_df = pd.DataFrame(data14)
date_df13 = pd.to_datetime(list(dem_df.index))
adj_close_df = list(dem_df)

#DES ticker
data15 = data.DataReader(ticker14,'google',begdate,enddate)
des_df = pd.DataFrame(data15)
date_df14 = pd.to_datetime(list(des_df.index))
adj_close_df = list(des_df)

#DEW ticker
data16 = data.DataReader(ticker15,'google',begdate,enddate)
dew_df = pd.DataFrame(data16)
date_df15 = pd.to_datetime(list(dew_df.index))
adj_close_df = list(dew_df)

#DFE ticker
data17 = data.DataReader(ticker16,'google',begdate,enddate)
dfe_df = pd.DataFrame(data17)
date_df16 = pd.to_datetime(list(dfe_df.index))
adj_close_df = list(dfe_df)

#DGS ticker
data18 = data.DataReader(ticker17,'google',begdate,enddate)
dgs_df = pd.DataFrame(data18)
date_df17 = pd.to_datetime(list(dgs_df.index))
adj_close_df = list(dgs_df)

#DHS ticker
data19 = data.DataReader(ticker18,'google',begdate,enddate)
dhs_df = pd.DataFrame(data19)
date_df = pd.to_datetime(list(dhs_df.index))
adj_close_df = list(dhs_df)

#DLN ticker
data20 = data.DataReader(ticker19,'google',begdate,enddate)
dln_df = pd.DataFrame(data20)
date_df = pd.to_datetime(list(dln_df.index))
adj_close_df19 = list(dln_df)

#Stock plots
plt.plot(date_df, aapl_df, 'r', label = 'AAPL' )
plt.plot(date_df1, acls_df, '-.r', label = 'ACLS')
plt.plot(date_df2, adbe_df, 'b', label = 'ADBE')
plt.plot(date_df3, amat_df, '-.b', label = 'AMAT')
plt.plot(date_df4, amzn_df, 'c', label = 'AMZN')
plt.plot(date_df5, arnc_df, '-.c', label = 'ARNC')
plt.plot(date_df6, avx_df, 'm', label = 'AVX')
plt.plot(date_df, awx_df, '-.m', label = 'AWX')
plt.plot(date_df, bep_df, 'y', label = 'BEP')
plt.plot(date_df, csbr_df, '-.y', label = 'CSBR')
plt.plot(date_df, cvy_df, 'k', label = 'CVY')
plt.plot(date_df, d_df, '-.k', label = 'D')
plt.plot(date_df, dem_df, '-r', label = 'DEM')
plt.plot(date_df, des_df, '-b', label = 'DES')
plt.plot(date_df, dew_df, '-c', label = 'DEW')
plt.plot(date_df, dfe_df, '-m', label = 'DFE')
plt.plot(date_df, dgs_df, '-y', label = 'DGS')
plt.plot(date_df, dhs_df, '-k', label = 'DHS')
plt.plot(date_df, dln_df, '-w', label = 'DLN')

#Plot Labels
#plt.legend()
plt.title("Stocks")
plt.xlabel("Date")
plt.ylabel("Dollars")
plt.show()
