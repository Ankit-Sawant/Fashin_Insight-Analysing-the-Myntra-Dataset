#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df_raw = pd.read_csv("C:/Users/Ankit/OneDrive/Desktop/Tushar Sir/myntra.csv")


# In[3]:


df_raw.shape


# In[4]:


df_raw.columns


# In[5]:


df_raw.info()


# In[6]:


df_raw.head()


# In[7]:


unique_asin = df_raw['asin'].unique()
print(unique_asin)


# In[8]:


df= df_raw.drop(['img', 'asin',  'id'], axis=1)

df.head()


# In[9]:


missing_values = df.isnull().sum()
print(missing_values)


# In[10]:


df.columns


# In[11]:


df.info()


# In[12]:


# Compute the correlation matrix
correlation_matrix = df.corr(numeric_only=True)


# In[13]:


# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
# Set the title of the heatmap
plt.title('Correlation Matrix Heatmap')
# Display the heatmap
plt.show()


# In[14]:


name_counts = df['name'].value_counts()
print(name_counts)


# In[15]:


# Select only the top 5 value counts
top_5_counts = name_counts.head(5)
top_5_counts


# In[16]:


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


# In[17]:


top_10_products = df.nlargest(10, 'discount')
print(top_10_products[['name', 'discount']])


# In[18]:


df.columns


# In[19]:


seller_counts = df['seller'].value_counts()
print(seller_counts)


# In[20]:


# Get the top 5 sellers by value counts
top_5_sellers = df['seller'].value_counts().head(5)


# In[21]:


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
#top_rated_products = df.sort_values(by=['rating', 'ratingTotal'], ascending=[False, False])
#top_rated_products = top_rated_products.head(10)
#top_rated_products


# In[22]:


# Top 10 items/types which has maximum average market price

item = df['purl']
lst=[]

for i in item:
    word=i.split('/')
    lst.append(word[3])
df['items'] =lst 
df.head(5)


# In[23]:


df['items'].unique()


# In[24]:


df.drop(df[df['items']=='https:'].index,inplace=True)


# # CLOTHES

# In[25]:


Clothes=df[df['items'].isin(['tshirts','shorts','shirts', 'tops', 'dresses', 'jeans','co-ords', 'tights', 'leggings', 'jumpsuit', 
                             'trousers','track-pants', 'shrug','kurtas', 'sarees','lehenga-choli', 'kurta-sets', 'ethnic-dresses', 
                             'kurtis','lingerie-set', 'churidar', 'swimwear-cover-up-top', 'shapewear','bra', 'sweatshirts','swimwear',
                             'nightdress', 'lounge-pants', 'night-suits','lounge-shorts','sherwani', 'pyjamas', 'blazers', 
                             'innerwear-vests', 'trunk','boxers', 'lounge-tshirts', 'tracksuits', 'swim-tops','swim-bottoms', 
                             'scarves','dupatta','capris', 'stockings','jackets','nehru-jackets','dungarees','skirts', 'sweaters', 
                             'jeggings','salwar','thermal-tops','camisoles', 'bodysuit', 'suits','palazzos', 'dress-material',
                             'patiala','saree-blouse','shawl', 'coats','sleepsuit', 'burqas','oven-glove', 'clothing-fabric',
                             'rain-jacket', 'pagri-and-safa','salwar-and-dupatta','patiala-and-dupatta',
                             'swimwear-cover-up-bottom','jackets-smart'])]


# In[26]:


Clothes.head()


# In[27]:


df1=Clothes.groupby('seller')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df1.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df1


# ## ROADSTER

# In[28]:


d1=Clothes[Clothes['seller']=='Roadster']
d1.head()


# In[29]:


df11=d1.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df11.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df11


# ## WROGN

# In[30]:


d2=Clothes[Clothes['seller']=='WROGN']
d2.head()


# In[31]:


df12=d2.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df12.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df12


# ## H&M

# In[32]:


d3=Clothes[Clothes['seller']=='H&M']
d3.head()


# In[33]:


df13=d3.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df13.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df13


# # FOOTWEAR

# In[34]:


Footwear=df[df['items'].isin(['flip-flops', 'heels', 'flats', 'sports-shoes', 'casual-shoes',
                              'socks','sports-sandals','shoe-accessories','baby-sippers','boots','booties','formal-shoes'])]


# In[35]:


df2=Footwear.groupby('seller')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df2.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df2


# ## HRX by Hrithik Roshan	

# In[36]:


d4=Footwear[Footwear['seller']=='HRX by Hrithik Roshan']
d4.head()


# In[37]:


df24=d4.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df24.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df24


# ## Red Tape

# In[38]:


d5=Footwear[Footwear['seller']=='Red Tape']
d5.head()


# In[39]:


df25=d5.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df25.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df25


# ## Levis

# In[40]:


d6=Footwear[Footwear['seller']=='Levis']
d6.head()


# In[41]:


df26=d6.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df26.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df26


# # ACCESORIES

# In[42]:


Acc=df[df['items'].isin(['jewellery-set', 'sunglasses', 'ring',
                         'hair-accessory', 'belts','anklet', 'necklace-and-chains', 'bangle', 'handbags', 'bracelet',
                         'mangalsutra','smart-watches', 'watch-gift-set', 'watches', 'briefs','lingerie-accessories',
                         'backpacks', 'gold-coin', 'pendant-gold','headphones','swimwear-accessories','clutches','caps',
                         'laptop-bag', 'toe-rings','duffel-bag','wallets','head-jewellery', 'pendant','mobile-accessories',
                         'hair-brush-and-comb','earrings-gold', 'ring-gold','hat','messenger-bag','mens-grooming-kit',
                         'waist-pouch','saree-accessories','brooch', 'nosepin','earrings-diamond','aprons',
                         'watch-organiser','travel-accessory','electric-toothbrush','silver-coins',
                         'handkerchief','fitness-bands','sports-accessories', 'ties','necklace-gold'
                         'pendant-diamond','gloves','nosepin-gold','mufflers','ties-and-cufflinks','pens',
                         'stationery','headband', 'watch-straps','cufflinks','lubricants','kitchen-gloves','key-chain',
                         'necklace-and-chains-diamond','sunglasses-case','rakhi','mittens','wristbands','bangle-gold',
                         'nosepin-diamond', 'ring-diamond','bracelet-diamond','rucksacks'])]


# In[43]:


df3=Acc.groupby('seller')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df3.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df3


# ## boAt

# In[44]:


d7=Acc[Acc['seller']=='boAt']
d7.head()


# In[45]:


df37=d7.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df37.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df37


# ## HRX by Hrithik Roshan

# In[46]:


d8=Acc[Acc['seller']=='HRX by Hrithik Roshan']
d8.head()


# In[47]:


df38=d8.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df38.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df38


# ## Daniel Klein

# In[48]:


d9=Acc[Acc['seller']=='Daniel Klein']
d9.head()


# In[49]:


df39=d9.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df39.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df39


# # HOME ESSENTIALS

# In[50]:


Home_Ess=df[df['items'].isin(['trimmer','hair-appliance','bedsheets', 'bed-covers', 'blankets-quilts-and-dohars','bedding-set', 
                              'doormats', 'carpets', 'floor-mats--dhurries','bath-towels', 'bath-robe', 'face-towels',
                              'towel-set','kitchen-storage', 'cookware', 'water-bottle', 'serveware','bar-and-drinkware',
                              'dinnerware', 'cups-and-mugs', 'table-lamps','floor-lamps', 'ceiling-lamps', 'wall-lamps',
                              'mattress-protector', 'pillows','hand-towels', 'bathroom-accessories', 'dining-essentials',
                              'appliance-covers','kitchen-tools', 'outdoor-lamps','string-lights','mosquito-nets', 
                              'table-covers','frames','massager','bar-accessories','trays', 'umbrellas','speakers','hat',
                              'beach-towels', 'coasters', 'cutlery','table-placemats', 'bathroom-lights', 'bath-rugs', 
                              'shower-curtains','bath-accessories','hand-wash-and-sanitizer','duvet-cover','condoms','pillow-covers', 
                              'curtains-and-sheers', 'table-cloth', 'kitchen-linen-sets','toiletry-kit','insect-repellent',
                              'bakeware', 'charms','table-napkins','kitchen-towels', 'tablet-sleeve', 'laundry-bag', 
                              'cushions','table-linen-sets', 'photo-frames',
                              'hooks-and-holders','sleeping-bag','personal-care-hamper','sleeping-mat', 'garden-accessories',
                              'showpieces', 'face-shield', 'yoga-mats','hanger', 'clocks','wall-art', 'cushion-covers',
                              'swings', 'high-chairs', 'rockers','walkers','bath-tub', 'chair-pads','wall-shelves', 
                              'napkin-set', 'festive-decor', 'mirrors','diwan-set', 'wall-decor','pooja-essentials',
                              'candle-holders', 'throws', 'aroma-oil-diffusers', 'jackets-smart','sofa-covers', 'bath-sets'])]


# In[51]:


df4=Home_Ess.groupby('seller')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df4.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df4


# ## Philips

# In[52]:


d10=Home_Ess[Home_Ess['seller']=='Philips']
d10.head()


# In[53]:


df41=d10.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df41.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df41


# ## Story@home

# In[54]:


d11=Home_Ess[Home_Ess['seller']=='Story@home']
d11.head()


# In[55]:


df42=d11.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df42.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df42


# ## Milton

# In[56]:


d12=Home_Ess[Home_Ess['seller']=='Story@home']
d12.head()


# In[57]:


df43=d12.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df43.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df43


# # TROLLY  & KIDS CARE

# In[58]:


Kids=df[df['items'].isin(['baby-dolls','trolley-bag','soft-toys-and-dolls','activity-toys-and-games',
                          'musical-toys','baby-care-products', 'construction-toys', 'toy-vehicles',
                          'baby-apparel-gift-set','baby-bed-sets','baby-pillow','baby-gear--nursery',
                          'baby-photoshoot-props', 'strollers',  'table-tennis-kits','jibbitz', 
                          'carry-cot', 'baby-sleeping-bag','baby-bathers', 'learning-and-development-toys',
                          'baby-utensils', 'feeding-bottles', 'collectibles','baby-sippers','baby-nail-grooming',
                          'school-essentials','baby-shower-caps','teether', 'breast-pumps','bottle-cleaners', 
                          'baby-hair-brush', 'feeding-essentials','art-and-craft', 'box',
                          'food-feeders','baby-oral-care','pacifiers', 'baby-bath-sponges', 'cradles','baby-pool'    
])]


# In[59]:


df5=Kids.groupby('seller')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df5.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df5


# ## Safari

# In[60]:


d13=Kids[Kids['seller']=='Safari']
d13.head()


# In[61]:


df51=d13.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df51.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df51


# ## DukieKooky

# In[62]:


d14=Kids[Kids['seller']=='DukieKooky']
d14.head()


# In[63]:


df52=d14.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df52.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df52


# ## Moms Home	

# In[64]:


d15=Kids[Kids['seller']=='Moms Home']
d15.head()


# In[65]:


df53=d15.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df53.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df53


# # PERSONAL CARE AND COSMETICS

# In[66]:


PC=df[df['items'].isin([ 'bath-and-body-gift-set','body-wash-and-scrub','highlighter-and-blush','highlighter-and-blush',
                        'eyeshadow', 'lipstick', 'eyebrow-enhancer', 'nail-essentials','face-moisturisers', 'shampoo-and-conditioner',
                        'face-wash-and-cleanser', 'bb-and-cc-cream', 'toner','hair-serum',
                        'hair-cream-and-mask', 'face-scrub-and-exfoliator','foundation-and-primer', 'concealer', 'compact',
                        'lip-gloss','face-serum-and-gel','sunscreen','shaving-essentials', 'body-lotion', 'perfume-and-body-mist',
                        'hair-oil', 'deodorant','foundation', 'kajal-and-eyeliner', 'mascara', 'face-primer','makeup-remover',
                        'lip-care', 'epilator', 'shaving-brush--razor','fragrance-gift-set', 'makeup-gift-set', 'skin-care-gift-set',
                        'beauty-accessory', 'hair-care-kit','mask-and-peel', 'hair-colour', 'hair-masks', 'makeup-brushes',
                        'lip-liner','beauty-gift-set', 'eye-cream',  'nail-polish','body-oil', 'body-wax-and-essentials', 
                        'eye-mask-and-patches','beard--moustache-care','facial-kit','hair-spray', 'hair-gel-and-spray',
                        'hand-and-feet-cream','makeup-kit','sheet-masks', 'feminine-hygiene','bath-soak-salt-and-oil',
                        'setting-spray', 'hair-gels-and-wax', 'tissues-and-wipes', 'bleach','eye-primer','false-eyelashes',
                        'sindoor','lip-plumper'])]


# In[67]:


df6=PC.groupby('seller')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df6.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df6


# ## Biotique

# In[68]:


d16=PC[PC['seller']=='Biotique']
d16.head()


# In[69]:


df61=d16.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df61.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df61


# ## Plum

# In[70]:


d17=PC[PC['seller']=='Plum']
d17.head()


# In[71]:


df62=d17.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df62.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df62


# ## Lotus Herbals

# In[72]:


d18=PC[PC['seller']=='Lotus Herbals']
d18.head()


# In[73]:


df63=d18.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df63.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df63


# # OTHERS 

# In[74]:


Others=df[df['items'].isin([ 'ride-on-vehicles','decals-and-stickers', 'pocket-squares', 'bolsters', 'tent','organisers',
                            'boxes', 'runners','rockers','warmers', 'car-seats','ottomans','role-play-and-playsets',
                            'footballs', 'bolster-covers','free-gifts','throws'])]


# In[75]:


df7=Others.groupby('seller')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df7.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df7


# ## My Gift Booth

# In[76]:


d19=Others[Others['seller']=='My Gift Booth']
d19.head()


# In[77]:


df71=d19.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df71.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df71


# ## RANGOLI	

# In[78]:


d20=Others[Others['seller']=='RANGOLI']
d20.head()


# In[79]:


df72=d20.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df72.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df72


# ## Van Heusen

# In[80]:


d21=Others[Others['seller']=='Van Heusen']
d21.head()


# In[81]:


df73=d21.groupby('items')['ratingTotal'].sum().sort_values(ascending = False).head(10).reset_index().head(10)
df73.rename(columns={'ratingTotal':'Consumers'},inplace=True)
df73


# In[ ]:




