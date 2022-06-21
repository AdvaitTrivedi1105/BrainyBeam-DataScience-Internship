#!/usr/bin/env python
# coding: utf-8

# In[103]:


import pandas as pd


# In[104]:


a = {
    "name":['a','b','c'],
    "language":['python','ds','cpp'],
    "marks":[30,40,50]
}


# In[105]:


df = pd.DataFrame(a)
df.ndim


# In[106]:


df


# In[107]:


type(df.name)


# In[108]:


df = pd.read_csv('data.csv')


# In[109]:


df


# In[110]:


a=['a','b','c']
b=[45,67,24]
z=dict(zip(a,b))


# In[111]:


z


# In[112]:


df1 = pd.DataFrame(z,index=[0,1,2,3,4])
df1


# In[113]:


s1 = pd.Series(a)
s1


# In[114]:


s2 = pd.Series(b)
s2


# In[115]:


df[df.marks>40]


# In[116]:


newdf = df[df.marks==50]
newdf


# In[117]:


newdf = df[(df.marks>50) & (df.language=='python')]
newdf


# In[118]:


df[['name','marks']]


# In[119]:


df[0:2]


# In[120]:


df[-1:]


# In[121]:


df.loc[[0,2],:]


# In[122]:


df.loc[0,:]


# In[123]:


df.loc[0:2,:]


# In[124]:


df.loc[0:1,:]


# In[125]:


df['merge'] = df['name'] + df['language']
df

