#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[4]:


df=pd.read_csv('Downloads/Heart_Disease_Prediction.csv')


# In[5]:


df.head()


# In[6]:


df.isnull().sum()


# In[7]:


print(df.info())


# In[ ]:




