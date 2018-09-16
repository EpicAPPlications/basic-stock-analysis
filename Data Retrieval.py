
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'],
                 index=['a', 'b', 'c', 'd'])
df


# In[3]:


df.index


# In[4]:


df.columns


# In[5]:


df.ix['c']


# In[6]:


df.loc['c']


# In[7]:


df.loc[['a', 'd']]


# In[8]:


df.loc[df.index[1:3]]


# In[9]:


df.sum()


# In[10]:


df.apply(lambda x : x ** 2)


# In[11]:


df ** 2


# In[12]:


df['floats'] = (1.5, 2.5, 3.5, 4.5)
df


# In[13]:


df['floats']


# In[14]:


df['names'] = pd.DataFrame(['Yves', 'Guido', 'Felix', 'Francesc'],
                          index=['d', 'a', 'b', 'c'])
df


# In[16]:


df.append({'numbers':100, 'floats': 5.75, 'names': 'Henry'},
                         ignore_index=True)


# In[18]:


df = df.append(pd.DataFrame({'numbers': 100, 'floats': 5.75, 
                             'names': 'Henry',}, index=['z',]))
df


# In[20]:


df.join(pd.DataFrame([1, 4, 9, 16, 25],
            index=['a', 'b', 'c', 'd', 'y'],
            columns=['squares',]))
df


# In[21]:


a= np.random.standard_normal((9, 4))
a.round(6)


# In[22]:


df = pd.DataFrame(a)
df


# In[35]:


df.columns = ['No1', 'No2', 'No3', 'No4']
df


# In[36]:


df['No2'][3]


# In[37]:


dates= pd.date_range('2015-1-1', periods=9, freq='M')
dates


# In[38]:


df.index = dates
df


# In[39]:


np.array(df).round(6)


# In[40]:


df.sum()


# In[41]:


df.mean()


# In[42]:


df.cumsum()


# In[43]:


df.describe()


# In[44]:


np.sqrt(df)


# In[45]:


np.sqrt(df).sum()


# In[46]:


get_ipython().magic(u'matplotlib inline')
df.cumsum().plot(lw=2.0)


# In[47]:


df['No1']


# In[48]:


type(df['No1'])


# In[49]:


import matplotlib.pyplot as plt
df['No1'].cumsum().plot(style='r', lw=2.)
plt.xlabel('date')
plt.ylabel('value')


# In[50]:


df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
df


# In[51]:


groups = df.groupby('Quarter')


# In[52]:


groups.mean()


# In[53]:


groups.max()


# In[54]:


groups.size()


# In[55]:


df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even',
                 'Odd', 'Even', 'Odd']


# In[57]:


groups =df.groupby(['Quarter', 'Odd_Even'])


# In[58]:


groups.size()


# In[59]:


groups.mean()


# In[65]:


import pandas.io.data as web


# In[1]:


import pandas as pd
from urllib import urlretrieve


# In[3]:


es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'
urlretrieve(es_url, 'data/es.txt')
urlretrieve(vs_url, 'data/vs.txt')
get_ipython().system(u'ls -o ./data/*txt')


# In[4]:


import numpy as np
import pandas as pd
import datetime as dt
from urllib import urlretrieve 
get_ipython().magic(u'matplotlib inline')


# In[5]:


url1 = 'http://hopey.netfonds.no/posdump.php?'
url2 = 'date=%s%s%s&paper=AAPL.O&csv_format=csv'
url = url1 + url2


# In[9]:


year = '2014'
month = '08'
days = ['22', '23', '24', '25']


# In[10]:


AAPL = pd.DataFrame()
for day in days:
    AAPL = AAPL.append(pd.read_csv(url % (year, month, day),
                                  index_col = 0, header=0, parse_dates=True))
AAPL.columns = ['bid', 'bdpeth', 'bdeptht', 
               'offer', 'odepth', 'odeptht']

