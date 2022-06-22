#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# In[4]:


from matplotlib import pyplot as plt
import pandas as pd


# In[5]:


x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.bar(x,y)
plt.show()


# In[6]:


a=['Male','Female']
b=[30,60]
plt.bar(a,b)
plt.show()


# In[7]:


df = pd.read_csv("sales.csv")


# In[8]:


df


# In[18]:


online = len(df.Sales_Channel=="online")
offline = len(df.Sales_Channel=="offline")


# In[19]:


index = ["Online","Offline"]
values = [online,offline]


# In[20]:


plt.bar(index,values)
plt.show()


# In[33]:


plt.barh(index,values,color="tomato")
plt.show()


# In[34]:


plt.hist(online)
plt.show()


# In[53]:


a = [20,30,50]
plt.pie(a,labels=["mango","apple","berry"],autopct="%0.2f%%",startangle=0,explode=[0,0.1,0])
plt.legend(loc="lower right")
plt.show()


# In[ ]:




