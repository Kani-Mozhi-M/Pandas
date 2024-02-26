#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


df=pd.read_csv(r"C:\Users\Kanimozhi.M\Downloads\countries of the world.csv")
df


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.describe()


# In[15]:


pd.set_option('display.max.rows',227)


# In[16]:


df


# In[17]:


pd.set_option('display.max.columns',1)


# In[18]:


df


# In[19]:


df.info()


# In[20]:


df.shape


# In[21]:


df.tail(13)


# In[25]:


df['Region']


# In[27]:


df.loc[224]


# In[28]:


df.iloc[1]

