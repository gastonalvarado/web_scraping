#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars

# In[1]:


#importing all dependencies
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
from splinter import Browser
import pandas as pd


# # Step 1 - Scraping

# ## Setting up URL's

# In[19]:


#URLs to be used in the complete project

#url_articles = 'https://mars.nasa.gov/news'
url_img_titles = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit'
url_twitter = 'https://twitter.com/marswxreport?lang=en'
mars_facts='https://space-facts.com/mars/'
url_hemispheres='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_unenhanced'


# In[3]:


#get_ipython().system('which chromedriver')


# In[4]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


#Windows Users
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)


# ## Requesting responses

# In[6]:


url_articles = 'https://mars.nasa.gov/news'
browser.visit(url_articles)


# In[7]:


#response = requests.get(url_articles)
response2 = requests.get(url_img_titles)
response3 = requests.get(url_twitter)
response4 = requests.get(mars_facts)
response5 = requests.get(url_hemispheres)
response3 #200 means it went through


# ## Converting into BeautifulSoup

# In[20]:


#soup_articles = BeautifulSoup(response.text, "lxml")
soup_img_title = BeautifulSoup(response2.text, "lxml")
soup_img_twitter = BeautifulSoup(response3.text, "lxml")
soup_mars_facts = BeautifulSoup(response4.text, "lxml")
soup_hemisphers = BeautifulSoup(response4.text, "lxml")


# ## NASA Mars News

# In[9]:


news_article=[]
for x in range(1, 6):

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    
    head_title=soup.find_all('div', class_='content_title')

    for title in head_title:
        data_file=title.text.strip()
        news_article.append(data_file)
        print(data_file)

    #browser.click_link_by_partial_text('Next')


# In[10]:


news_p=[]
for x in range(1, 6):

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    
    article_teaser=soup.find_all('div', class_='image_and_description_container')

    for title in article_teaser:
        data_file=title.text.strip()
        news_p.append(data_file)
        print(data_file)

    #browser.click_link_by_partial_text('Next')


# ## JPL Mars Space Images - Featured Image

# In[11]:


find_image=soup_img_title.find_all('img')[3]
featured_image=find_image['src']
#featured_image
featured_image_url=f'http://www.jpl.nasa.gov{featured_image}'
print(featured_image_url)   


# ## Mars Weather

# In[21]:


weather=soup_img_twitter.find_all('div',class_='content')
weather
mars_weather=[]
for x in weather:
    data_file=(x.find('p').text)
    mars_weather.append(data_file)
    print (data_file)


# ## Mars Facts

# In[14]:


tables = pd.read_html(mars_facts)
#tables
df = tables[0]
df.columns = ['Facts', 'Information']
#df.head()
df.set_index('Facts', inplace=True)
df


# In[15]:


html_table = df.to_html()
html_table


# ## Mars Hemispheres

# In[ ]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]


