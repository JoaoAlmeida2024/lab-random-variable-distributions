#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[4]:


df = pd.read_csv(r'C:\Users\joaof\ironhack\labs\lab-customer-analysis-round-2\files_for_lab\csv_files\marketing_customer_analysis.csv')


# In[5]:


df


# In[6]:


numeric_columns = df.select_dtypes(include=[np.number])


# In[7]:


numeric_columns


# In[10]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


import seaborn as sns


# In[14]:


sns.distplot(numeric_columns['Customer Lifetime Value'])
plt.show()


# In[15]:


sns.distplot(numeric_columns['Income'])
plt.show()


# In[16]:


sns.distplot(numeric_columns['Monthly Premium Auto'])
plt.show()


# In[17]:


sns.distplot(numeric_columns['Months Since Last Claim'])
plt.show()


# In[18]:


sns.distplot(numeric_columns['Months Since Policy Inception'])
plt.show()


# In[19]:


sns.distplot(numeric_columns['Number of Open Complaints'])
plt.show()


# # The variables seem to represent a normal distribution

# In[ ]:




