
# coding: utf-8

# In[2]:


a = 10
type(a)


# In[3]:


a.bit_length()


# In[4]:


a = 100000
a.bit_length()


# In[5]:


googol = 10 ** 100
googol


# In[6]:


googol.bit_length()


# In[7]:


1 + 4


# In[8]:


1 / 4


# In[9]:


type (1/4)


# In[10]:


1. / 4


# In[11]:


type (1./4)


# In[12]:


b = 0.35
type(b)


# In[13]:


b + 0.1 


# In[14]:


c = 0.5 
c.as_integer_ratio()


# In[15]:


b.as_integer_ratio()


# In[16]:


import decimal
from decimal import Decimal


# In[17]:


decimal.getcontext()


# In[18]:


d = Decimal(1) / Decimal(11)
d


# In[19]:


decimal.getcontext().prec = 4 #lower precision than the default


# In[20]:


e = Decimal(1) / Decimal(11)
e


# In[21]:


decimal.getcontext().prec = 50 #higher precision than the default


# In[22]:


f = Decimal(1) / Decimal(11)
f


# In[23]:


g = d + e + f
g


# In[24]:


t = 'this is a string object'


# In[25]:


t.capitalize


# In[26]:


t.capitalize()


# In[27]:


t.split()


# In[28]:


t.find('string')


# In[29]:


t.find('Python')


# In[30]:


t.replace(' ', '|')


# In[31]:


'http://www.python.org'.strip('htp:/')


# In[32]:


import re


# In[33]:


series = """
'01/18/2018 13:00:00', 100, '1st';
'01/18/2018 13:30:00', 110, '2nd';
'01/18/2018 14:00:00', 120, '3rd'
"""


# In[34]:


dt = re.compile("'[0-9/:\s]+'") #datetime


# In[35]:


result = dt.findall(series)
result


# In[36]:


from datetime import datetime
pydt = datetime.strptime(result[0].replace("'", ""),'%m/%d/%Y %H:%M:%S')
pydt


# In[37]:


print pydt


# In[38]:


print type(pydt)


# In[39]:


t = (1, 2.5, 'data')
type(t)


# In[40]:


t[2]


# In[41]:


type(t[2])


# In[42]:


t.count('data')


# In[43]:


t.index(1)


# In[44]:


l = [1, 2.5, 'data']
l[2]


# In[45]:


l = list(t)
l


# In[46]:


type(l)


# In[47]:


l.append([4, 3]) #append list at the end
l


# In[48]:


l.extend([1.0, 1.5, 2.0]) # append elements of list
l


# In[49]:


l.insert(1, 'insert') #insert object before index position
l


# In[50]:


l.remove('data')
l


# In[51]:


p = l.pop(3) #remove first occurence of object
print l, p


# In[52]:


l[2:5]


# In[53]:


for element in l[2:5]:
    print element ** 2


# In[54]:


r = range (0, 8, 1)
r


# In[55]:


type(r)


# In[56]:


for i in range(2, 5):
    print l[i] ** 2


# In[57]:


for i in range(1, 10):
    if i % 2 == 0:
        print "%d is even" % i
    elif i % 3 == 0:
        print "%d is multiple of 3" % i
    else:
        print "%d is odd" % i


# In[58]:


total = 0 
while total < 100:
    total += 1
    print total


# In[59]:


m = [i**2 for i in range(5)]
m


# In[60]:


def f(x):
    return x ** 2
f(2)


# In[61]:


def even(x):
    return x % 2 == 0
even(3)


# In[62]:


map(even, range(10))


# In[63]:


map(lambda x: x ** 2, range(10))


# In[64]:


filter(even, range(15))


# In[65]:


reduce(lambda x, y: x+y, range(10))


# In[66]:


d = {
    'Name' : 'Angela Merkel',
    'County' : 'Germany',
    'Profession' : 'Chancelor',
    'Age' : 60
}
type(d)


# In[67]:


print d['Name'], d['Age']


# In[68]:


d.keys()


# In[69]:


d.values()


# In[70]:


d.items()


# In[71]:


birthday = True
if birthday is True:
    d['Age'] +=1
    print d['Age']


# In[72]:


for item in d.iteritems():
    print item


# In[73]:


s = set(['u', 'd', 'ud', 'du', 'd', 'du'])
s


# In[74]:


t = set (['d', 'dd', 'uu', 'u'])
t


# In[75]:


s.union(t)


# In[76]:


s.intersection(t)


# In[77]:


s.difference(t)


# In[78]:


t.difference(s)


# In[79]:


s.symmetric_difference(t)


# In[80]:


from random import randint
l = [randint(0,10) for i in range(1000)]
len(l)


# In[81]:


l[:20]


# In[82]:


s = set(l)
s


# In[83]:


v = [0.5, 0.75, 1.0, 1.5, 2.0]


# In[84]:


m = [v, v, v]
m


# In[85]:


m[1]


# In[86]:


m[1][0]


# In[87]:


v1 =[0.5, 1.5]
v2 =[1, 2]
m = [v1, v2]
c = [m, m]
c


# In[88]:


c[1][1][0]


# In[89]:


v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = [v, v, v]
m


# In[90]:


v[0] = 'Python'
m


# In[91]:


from copy import deepcopy
v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = 3 * [deepcopy(v), ]
m


# In[92]:


v[0] = 'Python'
m


# In[93]:


import numpy as np


# In[94]:


a = np.array([0, 0.5, 1.0, 1.5, 2.0])
type(a)


# In[95]:


a[:2]


# In[96]:


a.std


# In[97]:


a.std()


# In[98]:


a.sum()


# In[99]:


a.cumsum()


# In[100]:


a * 2


# In[101]:


a ** 2


# In[102]:


np.sqrt(a)


# In[103]:


b = np.array([a, a * 2])
b


# In[104]:


b[0]


# In[105]:


b[1]


# In[106]:


b[0,2]


# In[107]:


b.sum()


# In[108]:


b.sum(axis = 0) # sum along the axis 


# In[109]:


b.sum(axis = 1)


# In[110]:


c = np.zeros((2, 3, 4), dtype='i' , order='C')
c


# In[111]:


d = np.ones_like(c, dtype='f16', order='C')
d


# In[112]:


import random 
I = 5000
get_ipython().magic(u'time mat = [[random.gauss(0,1) for j in range(I)] for i in range(I)]')


# In[113]:


get_ipython().magic(u'time reduce(lambda x, y: x + y,             [reduce(lambda x, y: x + y, row)                                 for row in mat])')


# In[114]:


get_ipython().magic(u'time mat = np.random.standard_normal((I, I))')


# In[115]:


get_ipython().magic(u'time mat.sum()')


# In[116]:


dt = np.dtype([('Name', 'S10'),('Age', 'i4'),
              ('Height', 'f'), ('Children/Pets', 'i4', 2)])
s = np.array([('Smith', 45, 1.83, (0,1)),
              (('Jones'), 53, 1.72, (2,2))], dtype=dt)
s


# In[117]:


s['Name']


# In[118]:


s['Height'].mean


# In[119]:


s['Height'].mean()


# In[120]:


s[1]['Age']


# In[121]:


r = np.random.standard_normal((4,3))
s = np.random.standard_normal((4,3))


# In[122]:


r + s


# In[123]:


2 * r + 3


# In[124]:


s = np.random.standard_normal(3)
r + s


# In[125]:


s = np.random.standard_normal(4)
r + s 


# In[126]:


r.transpose() + s 


# In[127]:


np.shape(r.T)


# In[128]:


np.shape(r)


# In[129]:


def f(x):
    return 3 * x + 5


# In[130]:


f(0.5)


# In[131]:


f(r)


# In[132]:


np.sin(r)


# In[133]:


np.sin(np.pi)


# In[134]:


x = np.random.standard_normal((5, 1000000))
y = 2 * x + 3
C = np.array((x, y), order ='C')
F = np.array((x, y), order ='F')
x = 0.0; y = 0.0 


# In[135]:


C[:2].round(2)


# In[136]:


get_ipython().magic(u'timeit C.sum()')


# In[137]:


get_ipython().magic(u'timeit F.sum()')


# In[138]:


get_ipython().magic(u'timeit C[0].sum(axis=0)')


# In[139]:


get_ipython().magic(u'timeit C[0].sum(axis=1)')


# In[140]:


get_ipython().magic(u'timeit F[0].sum(axis=0)')


# In[141]:


get_ipython().magic(u'timeit F[0].sum(axis=1)')


# In[142]:


F = 0.0; C = 0.0


# In[1]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

