
# coding: utf-8

# In[1]:


def perf_comp_data(func_list, data_list, rep=3, number=1):
    from timeit import repeat
    res_list = {}
    for name in enumerate(func_list):
        stmt = name[1] + '(' + data_list[name[0]] + ')'
        setup = "from __main__ import " + name[1] + ','                                 + data_list[name[0]]
        results = repeat(stmt=stmt, setup=setup, 
                        repeat=rep, number=number)
        res_list[name[1]]= sum(results) / rep
    res_sort = sorted(res_list.iteritems(),
                     key=lambda (k,v): (v,k))
    for item in res_sort:
        rel = item[1] / res_sort[0][1]
        print 'function:' + item[0] +               ', av. time sec: %9.5f, ' %item[1]            + 'relative'
        
    


# In[2]:


from math import *
def f(x):
    return abs(cos(x)) ** 0.5 + sin(2 + 3 * x)


# In[3]:


I = 500000
a_py = range(I)


# In[4]:


def f1(a):
    res = []
    for x in a:
        res.append(f(x))
    return res


# In[5]:


def f2(a):
    return [f(x) for x in a]
def f3(a):
    ex = 'abs(cos(x)) ** 0.5 + sin(2 + 3 * x)'
    return [eval(ex) for x in a]


# In[6]:


import numpy as np


# In[7]:


a_np = np.arange(I)


# In[8]:


def f4(a):
    return (np.abs(np.cos(a)) ** 0.5 + 
            np.sin(2 + 3 * a))


# In[9]:


import numexpr as ne


# In[10]:


def f5(a):
    ex = 'abs(cos(a)) ** 0.5 + sin(2 + 3 * a)'
    ne.set_num_threads(1)
    return ne.evaluate(ex)


# In[11]:


def f6(a):
    ex = 'abs(cos(a)) ** 0.5 + sin(2 + 3 * a)'
    ne.set_num_threads(16)
    return ne.evaluate(ex)


# In[12]:


get_ipython().magic(u'time')
r1 = f1(a_py)


# In[13]:


get_ipython().magic(u'time')
r1 = f1(a_py)
r2 = f2(a_py)
r3 = f3(a_py)
#r4 = f4(a_py)
r5 = f5(a_py)
r6 = f6(a_py)


# In[14]:


func_list = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6']
data_list = ['a_py', 'a_py', 'a_py', 'a_np', 'a_np', 'a_np']


# In[15]:


perf_comp_data(func_list, data_list)


# In[16]:


import numpy as np


# In[17]:


np.zeros((3, 3), dtype=np.float64, order='C')


# In[18]:


c = np.array([[1., 1., 1.],
             [2., 2., 2.],
             [3., 3., 3.]], order='C')


# In[19]:


f = np.array([[1., 1., 1.],
             [2., 2., 2.],
             [3., 3., 3.]], order='F')


# In[20]:


x = np.random.standard_normal((3, 1500000))
C = np.array(x, order='C')
F = np.array(x, order='F')
x = 0.0


# In[21]:


get_ipython().magic(u'timeit C.sum(axis=0)')


# In[22]:


get_ipython().magic(u'timeit C.sum(axis=1)')


# In[23]:


get_ipython().magic(u'timeit C.std(axis=0)')


# In[24]:


get_ipython().magic(u'timeit C.std(axis=1)')


# In[25]:


get_ipython().magic(u'timeit F.sum(axis=0)')


# In[26]:


get_ipython().magic(u'timeit F.sum(axis=1)')


# In[27]:


get_ipython().magic(u'timeit F.std(axis=0)')


# In[28]:


get_ipython().magic(u'timeit F.std(axis=1)')


# In[29]:


C = 0.0; F = 0.0


# In[30]:


def bsm_mcs_valuation(strike):
    import numpy as np
    S0 = 100; T = 1.0; r = 0.05; vola = 0.2
    M = 50; I = 20000
    dt = T / M
    rand = np.random.standard_normal((M + 1, I))
    S = np.zeros((M + 1, I)); S[0] = 50
    for t in range(1, M + 1):
        S[t] = S[t-1] * np.exp((r - 0.5 * vola ** 2) * dt
                              + vola * np.sqrt(dt) * rand[t])
        value = (np.exp(-r * T)
                * np.sum(np.maximum(S[-1] - strike, 0)) / I)
        return value


# In[31]:


def seq_value(n):
    strikes = np.linspace(80, 120, n)
    option_values = []
    for strikes in strikes:
        option_values.append(bsm_mcs_valuation(strikes))
        return strikes, option_values


# In[32]:


n = 100
get_ipython().magic(u'time strikes, option_values_seq = seq_value(n)')


# In[33]:


from IPython.parallel import Client
c = Client(profile="default")
view = c.load_balanced_view()


# In[34]:


import multiprocessing as mp


# In[35]:


import math
def simulate_geometric_brownian_motion(p):
    M, I, p 
    S0 = 100; r = 0.05; sigma = 2; T = 1.0
    dt = T / M
    paths = np.zeros((M + 1, I))
    paths[0] = S0
    for t in range (1, M + 1):
        paths[t] = paths[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + 
                sigma * math.sqrt(dt) * np.random.standard_normal(I))
        return paths
    
    


# In[36]:


M = 5
paths = simulate_geometric_brownian_motion((5, 2))
paths


# In[37]:


I = 10000
M = 100
t = 100


# In[ ]:


from math import cos, log
    def f_py(I, J):
        res = 0
        for i in range(I):
            res += int(cos(log(1)))
        return res

