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
        url = 'https://mars.nasa.gov/news/'
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

    #finally:

        #browser.quit()

