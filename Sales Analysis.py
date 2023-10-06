#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import os
import matplotlib.pyplot as plt


# # Merging 12 months of sales data into a single file.

# In[34]:


df = pd.read_csv("C:\\Users\\HP\\OneDrive\\Documents\\Sales Analysis Python\\Sales_Data\\Sales_April_2019.csv")

files = [file for file in os.listdir("C:\\Users\\HP\\OneDrive\\Documents\\Sales Analysis Python\\Sales_Data")]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("C:\\Users\\HP\\OneDrive\\Documents\\Sales Analysis Python\\Sales_Data\\"+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_months_data.csv", index = False)
    


# # Read in updated dataframe

# In[40]:


# all_data = pd.read_csv("all_months_data.csv")
all_data.head()


# # Clean up the data

# # -Drop rows of NaN

# In[51]:


nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()

all_data = all_data.dropna(how='all')
all_data.head()


# # -Find 'Or' in Month column and delete it

# In[58]:


all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']


# # Convert columns to their correct datatypes

# In[64]:


all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered']) #make int
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])   #make float

all_data.info()


# In[ ]:





# In[ ]:





# # Augment data with additional columns

# # -- Add 'Month' column.

# In[59]:


all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype("int")
all_data.head()


# # --Add a 'Sales' Column.

# In[81]:


all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
all_data.head()


# # --Add a 'City' column.

# # Using the .apply() method:

# In[114]:


def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' (' + get_state(x) + ') ')

all_data.head()


# In[ ]:





# In[ ]:





# In[ ]:





# # Question 1: What was the best month for sales? How much money was earned in that month?

# In[74]:


sales_monthly = all_data.groupby(by='Month').sum()
sales_monthly


# In[72]:


plt.figure(figsize=(10,5))


# In[100]:


months = range(1,13)

plt.bar(months, sales_monthly['Sales'], color = 'red')
plt.xticks(months)
plt.ylabel("Sales in USD")
plt.xlabel('Months')
plt.show()


# In[94]:


months = range(1,13)

plt.plot(months, sales_monthly['Sales'])
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title("Sales for the year 2019")
plt.show()


# # Question 2: What city had the highest number of sales?

# In[133]:


sales_city = all_data.groupby(by='City').sum()
sales_city = sales_city.sort_values(by='Sales', ascending = False)
sales_city


# In[120]:


plt.figure(figsize=(10,5))


# In[142]:


x = [city for city, df in all_data.groupby('City')] 

plt.bar(x, sales_city['Sales'], color = "purple")
plt.xticks(x, rotation='vertical', size=8)
plt.xlabel("City Names")
plt.ylabel("Sales in USD")
plt.title("Cities ranked by Highest Sales")


# # Question 3: What time should we display advertisements to maximize likelihood of customer's buying product?

# In[144]:


all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])


# In[149]:


all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data.head()


# In[153]:


hours = [hour for hour, df in all_data.groupby('Hour')]

plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.grid()
plt.title("Peak Hours of Orders Made")
plt.xlabel("Hour")
plt.ylabel("Number of Orders")


# # Question 4: What products are most often sold together?

# In[167]:


df = all_data[all_data['Order ID'].duplicated(keep=False)]

df['Grouped'] = df.groupby(by="Order ID")['Product'].transform(lambda x: ','.join(x))

df = df[['Order ID', 'Grouped']].drop_duplicates()

df.head(50)


# In[171]:


from itertools import combinations
from collections import Counter

count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))
    
for key, value in count.most_common(10):
    print(key, value)


# # Question 5: What product sold the most? Why do you think it sold the most?

# In[172]:


all_data.head()


# In[191]:


product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

products = [products for products,df in product_group]

plt.figure(figsize=(12,8))
plt.bar(products,
        quantity_ordered,
        color='orange')
plt.xticks(products, rotation = 'vertical')
plt.xlabel('Products')
plt.ylabel('Quantity Ordered')
plt.title("Bar Chart Showing Quantities of Products Ordered")
plt.show()


# In[192]:


prices = all_data.groupby('Product').mean(['Price Each'])





# In[201]:


fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products,quantity_ordered,color='orange')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Products')
ax1.set_ylabel('Quantity Ordered')
ax2.set_ylabel('Price in USD')
ax1.set_xticklabels(products, rotation = 'vertical')

plt.show()


# In[ ]:





# In[ ]:




