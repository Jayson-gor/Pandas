#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
#importing the csv file
df = pd.read_csv(r'C:\Users\gorja\Downloads\nyc_weather.csv')
#displaying the csv file
df


# In[6]:


#displaying the maximum temperature
df['Temperature'].max()


# In[7]:


#displaying the maximum humidity
df['Humidity'].max()


# In[8]:


#displaying the maximum winddirdegree
df['WindDirDegrees'].max()


# In[9]:


#displaying the maximum dew point
df['DewPoint'].max()


# In[10]:


df.shape


# In[11]:


rows, columns = df.shape
columns


# In[12]:


rows


# In[13]:


#printing the fisrt five rows of data
df.head()


# In[14]:


#printing the first 20 rows of data
df.head(20)


# In[15]:


#displaying the last 5 rows
df.tail()


# In[16]:


#displaying the last 15 rows
df.tail(15)


# In[17]:


df.columns


# In[18]:


df.Events


# In[19]:


df[['Temperature', 'DewPoint', 'Humidity']]


# In[23]:


#determining the maximum temperature
df['Temperature'].max()


# In[24]:


#determining the minimum temeperature
df['Temperature'].min()


# In[25]:


#statistical summary
df.describe()


# In[26]:


#saving the cleaned data to a new csv file
df.to_csv('new_data')


# In[29]:


#to know data types in each column
print(df.dtypes)


# In[31]:


#make EST column a date column
df = pd.read_csv(r'C:\Users\gorja\Downloads\nyc_weather.csv', parse_dates=["EST"])
df


# In[32]:


#confirm the data type of EST
print(df.dtypes)


# In[33]:


df


# In[34]:


#replacing NaN values with 0
df = df.fillna(0)
df


# In[38]:


#replacing the 0 in Events with 'no event'
df['Events'] = df['Events'].replace(0, 'no events')
df


# In[ ]:




