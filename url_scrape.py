#!/usr/bin/env python

# Scrapes the Pitchfork /albums/review pages for the URLs to each reviewed album
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

# don't mess with these variables
delay = 1 # time to wait on each page load before reading the page
driver = webdriver.Safari() # options are Chrome(), Safari(), Firefox()
urls = []
album_selector = 'div.review'
url_selector = '.review a.album-link'

# mess with this variable
page_counter = 1 # change this as appropriate -- in 06/2017 there were roughly 1580 album revie pages
destination_file = 'scrape-output.json'

def test_url(page_number):
    base_url = 'http://www.pitchfork.com/reviews/albums/?page='
    page = str(page_number)
    return base_url + page

while page_counter <= 1:
    url = test_url(page_counter)
    print(url)
    driver.get(url)
    sleep(delay)
    page_counter = page_counter + 1
    found_albums = driver.find_elements_by_css_selector(album_selector)
    print('{} albums found.'.format(len(found_albums)))

    for album in found_albums:
        id = album.find_element_by_css_selector(url_selector).get_attribute('href')
        urls.append(id)

    print('album urls found:', len(urls))

    data_to_write = list(set(urls))

    with open(destination_file, 'w') as f:
        for url in urls:
            f.write(url + '\n')

driver.close()
driver.quit()
