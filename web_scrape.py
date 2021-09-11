# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

#wvu review
def web_scrape(URL, div_class, div_itemprop, reviews):
    '''
    web scrape function to extract the reviews from a website.
    inputs: URL - string, div_class - string, div_itemprop - string, reviews - list
    output: reviews - list, populated with web content
    '''
    URL = URL
    
    # spoofed headers to emulate browser visit
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    
    r = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(r.content, 'html5lib') 
    
    #store html attributes in table
    table = soup.find('div', attrs = {'class':'profile__bucket--3'}) 
       
    
    # iterate over rows that contain reviewBody, store in list
    for row in table.findAll('div',
                             attrs = {'itemprop':'reviewBody'}):

        review = row.span.text
        reviews.append(review)
    
    
    return(reviews)

# set params

URL = "https://www.niche.com/colleges/west-virginia-university/reviews/"
div_class = 'profile__bucket--3'
div_itemprop = 'reviewBody'
reviews = []

# run function

df_reviews = pd.DataFrame(web_scrape(URL, div_class, div_itemprop, reviews), columns=['reviews'])

# export to csv    

df_reviews.to_csv('wvu_reviews.csv')






