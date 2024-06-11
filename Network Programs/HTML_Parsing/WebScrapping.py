# Web scrapping is done inorder to extract data from a website. 
# It is also called as spidering or web crawling.
# Web scrapping is done using the BeautifulSoup library.
# BeautifulSoup is a library that makes it easy to scrape information from web pages.
# BeautifulSoup is a third party library and needs to be installed.
# pip install beautifulsoup4

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = "https://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))