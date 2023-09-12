#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


df = pd.read_excel(r"C:\Users\HP\OneDrive\Documents\YouTube Top Channels\Global_YouTube_Statistics.xlsx")
df


# In[10]:


df.info()


# In[32]:


df.isnull().sum()


# In[12]:


to_drop = ['Abbreviation',
           'lowest_yearly_earnings',
           'lowest_monthly_earnings',
           'highest_monthly_earnings',
           'subscribers_for_last_30_days',
           'created_month',
           'created_date',
          'Gross tertiary education enrollment (%)',
          'Population',
          'Unemployment rate',
          'Urban_population',
          'Latitude',
          'Longitude',
          'video_views_for_the_last_30_days']

df.drop(columns=to_drop, inplace=True)


# In[13]:


df


# In[14]:


df.head(10).sort_values(by='subscribers',ascending=False)


# In[15]:


df=df.head(50).sort_values(by="subscribers",ascending=False)


# In[16]:


df['Youtuber']=df['Youtuber'].str.lstrip('ýýý')


# In[17]:


df


# In[18]:


df['highest_yearly_earnings']=df['highest_yearly_earnings'].astype(int)


# In[19]:


df


# In[20]:


subset = df.loc[:,['category','video views']]
subset.groupby('category').sum()


# In[21]:


most_views = df.groupby('category')['video views'].sum()


# In[22]:


most_views


# In[128]:


most_views.plot(kind='bar',title='Most Viewed Category on YouTube')

xlabel='category'
ylabel='views'


# In[58]:


data = pd.DataFrame(df).head(10)


# In[87]:


plt.figure(figsize=(10,15))
x_axis=data['Youtuber']
y_axis=data['subscribers']
title='Youtubers Ranked by subscriber Count'
plt.xlabel=('Youtubers')
plt.ylabel=('Subscribers')
plt.title('Youtubers Ranked by Subscriber Count')
plt.bar(x_axis,y_axis,width=0.6,color='red',align='edge')
labelx=data['Youtuber']
plt.xticks(rotation=90)
ylabel


# In[56]:


#data.drop(columns='Title',inplace=True) -------dropped 'Title' column


# In[60]:


data_two = pd.DataFrame(df).head(50)


# In[63]:


data_two=data_two.sort_values(by='highest_yearly_earnings',ascending=False)


# In[66]:


data_two.reset_index(inplace=True)


# In[70]:


data_two.drop(columns='index',inplace=True)


# In[72]:


data_two=data_two.head(10)


# In[74]:


plt.figure(figsize=(10,15))
x=data_two['Youtuber']
y=data_two['highest_yearly_earnings']
xlabel='Youtuber'
ylabel='Revenue'
plt.bar(x,y,width=0.7,align='edge',color='orange')
plt.title('YouTubers Ranked by Revenue')
plt.xticks(rotation=90)

