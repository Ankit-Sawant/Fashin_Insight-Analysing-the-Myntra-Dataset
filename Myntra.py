#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[41]:


df_raw = pd.read_csv("C:/Users/Ankit/OneDrive/Desktop/Tushar Sir/myntra.csv")


# In[42]:


df_raw.shape


# In[43]:


df_raw.columns


# In[44]:


df_raw.info()


# In[45]:


df_raw.head()


# In[46]:


unique_asin = df_raw['asin'].unique()
print(unique_asin)


# In[47]:


df= df_raw.drop(['img', 'asin',  'id'], axis=1)


# In[48]:


df.head()


# In[49]:


missing_values = df.isnull().sum()
print(missing_values)


# In[50]:


df.columns


# In[51]:


df.info()


# In[52]:


# Compute the correlation matrix
correlation_matrix = df.corr(numeric_only=True)

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)

# Set the title of the heatmap
plt.title('Correlation Matrix Heatmap')

# Display the heatmap
plt.show()


# In[53]:


name_counts = df['name'].value_counts()
print(name_counts)


# In[54]:


# Select only the top 5 value counts
top_5_counts = name_counts.head(5)
top_5_counts


# In[55]:


# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=top_5_counts.index, y=top_5_counts.values)
plt.xticks(rotation=90)
plt.xlabel('Name')
plt.ylabel('Count')
plt.title('Top 5 Value Counts for Name Column')
plt.tight_layout()

# Display the plot
plt.show()


# In[56]:


df['price'].describe()


# In[57]:


# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=20, kde=True)

# Set labels and title
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Price Column')

# Display the plot
plt.show()


# In[58]:


df[df["price"]<50000].count()


# In[59]:


# Apply logarithmic transformation
log_prices = np.log(df['price'])

# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(log_prices, bins=20, kde=True)

# Set labels and title
plt.xlabel('Logarithm of Price')
plt.ylabel('Frequency')
plt.title('Distribution of Logarithm of Price Column')

# Display the plot
plt.show()


# In[60]:


df['mrp'].describe()


# In[61]:


# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['mrp'], bins=20, kde=True)

# Set labels and title
plt.xlabel('MRP')
plt.ylabel('Frequency')
plt.title('Distribution of MRP Column')

# Display the plot
plt.show()


# In[62]:


# Apply logarithmic transformation
log_prices = np.log(df['mrp'])

# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(log_prices, bins=20, kde=True)

# Set labels and title
plt.xlabel('Logarithm of MRP')
plt.ylabel('Frequency')
plt.title('Distribution of Logarithm of mrp Column')

# Display the plot
plt.show()


# In[63]:


df['rating'].describe()


# In[64]:


# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['rating'], bins=20, kde=True)

# Set labels and title
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Rating Column')

# Display the plot
plt.show()


# In[65]:


# Filter out the "0" values in the rating column
filtered_ratings = df[df['rating'] != 0]['rating']

# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(filtered_ratings, bins=20, kde=True)

# Set labels and title
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Rating Column (excluding 0)')

# Display the plot
plt.show()


# In[66]:


df['ratingTotal'].describe()


# In[67]:


# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['ratingTotal'], bins=20, kde=True)

# Set labels and title
plt.xlabel('Rating Total')
plt.ylabel('Frequency')
plt.title('Distribution of RatingTotal Column')

# Display the plot
plt.show()


# In[68]:


# Apply logarithmic transformation
log_ratingTotal = np.log(df['ratingTotal'])

# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(log_ratingTotal, bins=20, kde=True)

# Set labels and title
plt.xlabel('Logarithm of Rating Total')
plt.ylabel('Frequency')
plt.title('Distribution of Logarithm of RatingTotal Column')

# Display the plot
plt.show()


# In[69]:


top_10_products = df.nlargest(10, 'ratingTotal')
print(top_10_products[['name', 'ratingTotal']])


# In[70]:


df['discount'].describe()


# In[71]:


# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['discount'], bins=20, kde=True)

# Set labels and title
plt.xlabel('Discount')
plt.ylabel('Frequency')
plt.title('Distribution of Discount Column')

# Display the plot
plt.show()


# In[72]:


# Apply logarithmic transformation
log_discount = np.log(df['discount'] + 1)  # Adding 1 to avoid log(0)


# In[73]:


# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(log_discount, bins=20, kde=True)

# Set labels and title
plt.xlabel('Logarithm of Discount')
plt.ylabel('Frequency')
plt.title('Distribution of Logarithm of Discount Column')

# Display the plot
plt.show()


# In[74]:


top_10_products = df.nlargest(10, 'discount')
print(top_10_products[['name', 'discount']])


# In[75]:


df.columns


# In[76]:


seller_counts = df['seller'].value_counts()
print(seller_counts)


# In[97]:


# Get the top 5 sellers by value counts
top_5_sellers = df['seller'].value_counts().head(5)

# Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=top_5_sellers.index, y=top_5_sellers.values)

# Set labels and title
plt.xlabel('Seller')
plt.ylabel('Count')
plt.title('Top 5 Sellers by Value Counts')

# Rotate x-axis labels for better readability if needed
plt.xticks(rotation=45)

# Display the plot
plt.show()


# In[98]:


#top_rated_products = df.sort_values(by=['rating', 'ratingTotal'], ascending=[False, False])
#top_rated_products = top_rated_products.head(10)
#top_rated_products


# # Top 10 items/types which has maximum average market price

# In[79]:


item = df['purl']
lst=[]

for i in item:
    word=i.split('/')
    lst.append(word[3])
df['items'] =lst 
df.head(5)


# In[80]:


df.drop(columns= ['purl'],axis =1,inplace = True)
df.head(5)


# In[95]:


df1=df.groupby('items')['mrp'].mean().sort_values(ascending = False).head(10).reset_index().head(10)
df1
#df['items'].unique() 


# In[92]:


plt.style.use('dark_background')
plt.figure(figsize=(12,4))
plt.xticks(rotation=45)
sns.lineplot(x='items',y='mrp',data=df1,marker='*')


# # Top 10 items / types with maximum discount price

# In[84]:


df2=df.groupby('items')['discount'].max().sort_values(ascending =  False).head(10).reset_index()
df2


# In[85]:


plt.figure(figsize=(12,4))
plt.xticks(rotation=90)

plt.title(' Top 10 items with maximum discount price')
sns.barplot(x='items',y='discount',data=df2)


# # Top 10 items with highest rating

# In[86]:


df3=df.groupby('items')['rating','ratingTotal'].max().sort_values(by =['rating','ratingTotal'],ascending =False).head(10).reset_index()
df3


# In[87]:


plt.figure(figsize=(12,4))
plt.title('Top 10 items with highest rating')
sns.barplot(data=df3,x='ratingTotal',y='items')


# # which seller has got maximum profit

# In[88]:


df['Profit']=df['mrp']-df['price']
df.head(5)


# In[89]:


df4=df.groupby('seller')['Profit'].agg(['max','mean']).sort_values(by ='mean' ,ascending = False).head(10).reset_index()
df4


# In[90]:


plt.figure(figsize=(12,4))
plt.xticks(rotation=90)
sns.barplot(x='seller', y='max', color='blue', alpha=0.7, label='Maximum',data=df4)
sns.barplot(x='seller', y='mean', color='red', alpha=0.7, label='Mean',data=df4)
plt.xlabel('Items')
plt.ylabel('Values')
plt.legend()

