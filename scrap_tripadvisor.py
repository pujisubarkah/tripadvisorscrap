#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


html = requests.get('https://www.tripadvisor.com/Hotels-g294230-Yogyakarta_Region_Java-Hotels.html')
html.status_code


# In[3]:


soup = BeautifulSoup(html.content,'lxml')


# In[4]:


hotel = []
for name in soup.findAll('div',{'class': "listing_title"}):
  hotel.append(name.text.strip())

hotel


# In[5]:


ratings = []
for rating in soup.findAll('a', {'class':'ui_bubble_rating'}):
  ratings.append(rating['alt'])

ratings


# In[6]:


reviews = []
for review in soup.findAll('a', {'class':'review_count'}):
  reviews.append(review.text.strip())

reviews


# In[7]:


harga = []
for h in soup.findAll('div',{'class': 'price-wrap'}):
  harga.append(h.text.replace('IDR','').strip())

harga[:5]


# In[8]:


len(harga)


# In[9]:


d1 = {'Hotel':hotel,'Ratings':ratings,'No_of_reviews':reviews,'Harga':harga}


# In[10]:


import pandas as pd


# In[11]:


df = pd.DataFrame.from_dict(d1)
df

