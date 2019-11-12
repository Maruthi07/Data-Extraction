#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
get_ipython().system('pip install tabula-py')
from tabula import wrapper
df= wrapper.read_pdf('C:/Users/ramaruth/Downloads/hdfc.pdf')


# In[164]:


df


# In[165]:


data=df[['Date','Narration','Withdrawal Amt.','Deposit Amt.','Closing Balance']]


# Here the null values of Narration doesn't provide any transacton details.Hence Deleting them

# In[166]:


data[data.Narration.isnull()]


# In[167]:


data=data.dropna(subset=['Narration'],axis = 0, how ='any') 


# In[168]:


data[data.Narration.isnull()]


# In[169]:


data.isnull().sum()


# Replacing NAN values with 0

# In[170]:


data=data.fillna(value='0')


# In[171]:


data


# In[172]:


data.drop(data.tail(8).index,inplace=True)


# In[173]:


data


# Deleting the rows which doesn't provide any transaction details.

# In[174]:


data.drop(data.index[[3,7,9,18,20,23,25,27]],inplace=True)


# In[175]:


data


# Converting the data into csv file format

# In[177]:


data.to_csv('C:/Users/ramaruth/Downloads/hdfc_new.csv',header=True)

