
# coding: utf-8

# In[35]:


V0 = 17.6639


# In[36]:


r = 0.01


# In[37]:


import pandas as pd
h5 = pd.HDFStore("\\Users\\esehu\\Desktop\\vstoxx_data_31032014.h5",'r')
futures_data = h5['futures_data']
options_data = h5['options_data']
h5.close()


# In[38]:


futures_data


# In[39]:


options_data.info()


# In[40]:


options_data[['DATE', 'MATURITY', 'TTM', 'STRIKE', 'PRICE']].head()


# In[41]:


options_data['IMP_VOL'] = 0.0


# In[42]:


def bsm_call_value(S0,K,T,r,sigma):
    from math import log,sqrt,exp
    from scipy import stats
    
    S0 = float(S0)
    d1 = (log(S0 / K ) + (r + 0.5 * sigma ** 2) * T) /(sigma * sqrt(T))
    d2 = (log(S0 / K ) + (r - 0.5 * sigma ** 2) * T) /(sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1,0.0,1.0)
            - K * exp(-r * T) * stats.norm.cdf(d2,0.0,1.0))
    return value
    
def bsm_vega(S0,K,T,r,sigma):
    from math import log,sqrt
    from scipy import stats 
    S0 = float(S0)
    d1 = (log(S0 / K ) + (r + 0.5 * sigma ** 2) * T) /(sigma * sqrt(T))
    vega = S0 * stats.norm.cdf(d1,0.0,1.0) * sqrt(T)

    return vega

def bsm_impl_vol(S0,K,T,r,C0,sigma_est, it= 100):
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0,K,T,r,sigma_est) - C0)
                     / bsm_vega(S0,K,T,r,sigma_est))
    return sigma_est


# In[43]:


tol = 0.5 
for option in options_data.index:
    forward = futures_data[futures_data['MATURITY']==                           options_data.loc[option]['MATURITY']]['PRICE'].values[0]
    if (forward * (1 - tol) < options_data.loc[option]['STRIKE']
                              < forward * (1 + tol)):
        impl_vol = bsm_impl_vol(
                V0, 
                options_data.loc[option]['STRIKE'],
                options_data.loc[option]['TTM'],
                r,
                options_data.loc[option]['PRICE'],
                sigma_est=2.,
                it=100)
        options_data['IMP_VOL'].loc[option] = imp_vol
        

