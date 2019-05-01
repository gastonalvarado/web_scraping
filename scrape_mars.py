#importing all dependencies
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
from splinter import Browser
import pandas as pd


# # Step 1 - Scraping

# Initialize browser
def init_browser(): 
    
# Choose the executable path to driver
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', headless=True, **executable_path)

# Create dictionary that can be imported into Mongo
mars_mission = {}

# NASA MARS NEWS
def scrape_mars_news():
    #try: 

         # Initialize browser 
        browser = init_browser()

        # Visit Nasa news url through splinter module
        url = 'https://mars.nasa.gov/news'
        browser.visit(url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'lxml')

        # Retrieve the latest element that contains news title and news_paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text

        # Dictionary entry from MARS NEWS
        mars_mission['news_title'] = news_title
        mars_mission['news_paragraph'] = news_p

        return mars_mission

# NASA MARS IMAGES
def scrape_mars_image():

         # Initialize browser 
        browser = init_browser()

        # Visit Nasa news url through splinter module
        url_img_titles = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit'
        browser.visit(url_img_titles)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'lxml')

        # Retrieve the latest element that contains news title and news_paragraph
        find_image=soup.find_all('img')[3]
        featured_image=find_image['src']
        featured_image_url=f'http://www.jpl.nasa.gov{featured_image}'
        featured_image_url
        
        # Dictionary entry from MARS NEWS
        mars_mission['featured_image_url'] = featured_image_url

        return mars_mission
    
# NASA MARS WEATHER
def scrape_mars_weather():

         # Initialize browser 
        browser = init_browser()
        
         # Visit Nasa news url through splinter module
        url_twitter = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(url_twitter)

        # HTML Object 
        html_weather = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_weather, 'lxml')

        # Find all elements that contain tweets
        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

        # Look for entries that display weather related words to exclude non weather related tweets 
        for tweet in latest_tweets: 
                weather_tweet = tweet.find('p').text
                if 'Sol' and 'pressure' in weather_tweet:
                    print(weather_tweet)
                    break
                else: 
                     pass
            
        # Dictionary entry from MARS NEWS
        mars_mission['weather_tweet'] = weather_tweet

        
        return mars_mission


# NASA MARS WEATHER
def scrape_mars_facts():

         # Initialize browser 
        browser = init_browser()
        
         # Visit Nasa news url through splinter module
        mars_facts='https://space-facts.com/mars/'
        browser.visit(mars_facts)

        # HTML Object 
        facts = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(facts, 'lxml')

       # Use Panda's `read_html` to parse the url
        tables = pd.read_html(mars_facts)
        df = tables[0]

        #Retrieve the values from the website's table
        html_table = df.to_html(header=False, index=False) 
     
        # Dictionary entry from MARS NEWS
        mars_mission['html_table'] = html_table

        
        return mars_mission
    

# NASA MARS WEATHER
def scrape_mars_hemisphers():

         # Initialize browser 
        browser = init_browser()
        
         # Visit Nasa news url through splinter module
        hemispheres_url = 'https://astrogeology.usgs.gov'
        browser.visit(hemispheres_url)

        # HTML Object 
        hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(hemispheres, 'lxml')
 
        # Retreive all items that contain mars hemispheres information
        items = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
        hemisphere_image_urls = []

        # Store the main_ul 
        #hemispheres_main_url = 'https://astrogeology.usgs.gov'

        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text
    
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
            # Visit the link that contains the full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
    
            # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
    
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = BeautifulSoup( partial_img_html, 'html.parser')
    
            # Retrieve full image source 
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
            # Append the retreived information into a list of dictionaries 
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    
            # Display hemisphere_image_urls
            hemisphere_image_urls
    
            # Dictionary entry from MARS NEWS
            mars_mission['hemisphere_image_urls'] = hemisphere_image_urls

        
        return mars_mission
    
    
    
    
    
    
    
    
    
    
