#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# # Series and DataFrame

# In[ ]:


df = pd.read_csv('data.csv')
df


# ### Group by

# In[ ]:


df.groupby('language')['marks'].sum()


# In[ ]:


type(df.name)


# In[ ]:


type(df)


# In[ ]:


df[['name','marks']]


# ### Filter data frame

# In[ ]:


df.marks>40


# In[ ]:


df[df.marks>40]


# In[ ]:


df.columns


# In[ ]:


df.columns[2]


# In[ ]:


df.ndim


# In[ ]:


df[df.columns]


# In[ ]:


df.loc[0:,['language']]


# In[ ]:


df.iloc[0:3,[0,2]]


# In[ ]:


df.head(2)


# In[ ]:


df.tail(3)


# In[ ]:


df.sample(2)


# In[ ]:


df


# ### Drop data 

# In[ ]:


df.drop('marks',axis=1)


# In[ ]:


newdf = df.drop(df.columns[1],axis=1)


# In[ ]:


newdf


# In[ ]:


df[(df.language=="DS") & (df.marks>42)]


# In[ ]:


newdf.to_csv("newData.csv")


# In[ ]:


df.drop(2)


# In[ ]:


df.info()


# In[ ]:


new = df.drop_duplicates()


# In[ ]:


new


# In[ ]:


new2 = df.drop_duplicates(subset=['language'])


# In[ ]:


new2


# ### Sort Data

# In[ ]:


new2_sorted = new2.sort_values('language')
new2_sorted


# In[ ]:


new2_sorted = new2.sort_values('marks')
new2_sorted


# In[ ]:


new2_sorted = new2.sort_values('marks',ascending=False)
new2_sorted

