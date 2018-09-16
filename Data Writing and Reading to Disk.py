
# coding: utf-8

# In[1]:


path = '/flash/data/'


# In[2]:


import numpy as np
from random import gauss


# In[3]:


a = [gauss(1.5, 2) for i in range(1000000)]


# In[4]:


import pickle #writes the previous list item into the disk later


# In[5]:


pkl_file = open(path + 'data.pkl', 'w')


# In[3]:


rows = 5000
a = np.random.standard_normal((rows, 5))


# In[4]:


a.round(4)


# In[6]:


import pandas as pd
t = pd.date_range(start='2014/1/1', periods=rows, freq='H')


# In[7]:


t


# In[8]:


import sqlite3 as sq3


# In[9]:


query = 'CREATE TABLE numbs (Date date, No1 real, No2 real)'


# In[10]:


con = sq3.connect(path + 'numb.db')

