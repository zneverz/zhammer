#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


# In[25]:


# Load Data From CSV

data_raw = pd.read_csv('x_jce_1.csv')
data_raw.count()


# In[26]:


data_raw.shape


# In[27]:


data_raw.head()


# In[28]:


# Check every relationship between every X and y

d1 = data_raw.copy()
plt.subplot()
plt.scatter(d1['spgz'], d1['jce'])
plt.show()

plt.scatter(d1['sjrs'], d1['jce'])
plt.show()

plt.scatter(d1['xhrs'], d1['jce'])
plt.show()

plt.scatter(d1['xzkhs'], d1['jce'])
plt.show()


# In[29]:


# filter data and check again

d = data_raw[data_raw['jce'] < 2000000000].copy()
plt.subplot()
plt.scatter(d['spgz'], d['jce'])
plt.show()

plt.scatter(d['sjrs'], d['jce'])
plt.show()

plt.scatter(d['xhrs'], d['jce'])
plt.show()

plt.scatter(d['xzkhs'], d['jce'])
plt.show()


# In[30]:


# Define X y in Model

X = d[['spgz','sjrs','xhrs','xzkhs']]
y = d[['jce']]


# In[31]:


# Define Train Model
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# In[18]:


# Fit model

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)


# In[ ]:


# check result

print(linreg.intercept_)
print(linreg.coef_)
linreg.score(X_test, y_test)
linreg.summary()

