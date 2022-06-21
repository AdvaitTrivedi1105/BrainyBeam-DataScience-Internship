#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


a = np.array([[4,6,7,8],[9,10,11,12]])
a.ndim


# In[4]:


a


# In[6]:


z = np.zeros(7)
z


# In[9]:


print(a)
t = a.T
t


# In[11]:


a.shape


# In[12]:


r = a.reshape(4,2)
r


# In[13]:


c = np.array([3,4,5,6,8])


# In[14]:


np.mean(c)


# In[15]:


np.median(c)


# In[ ]:




