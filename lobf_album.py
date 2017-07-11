#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import datetime
import json
import csv
import urllib

# don't mess with these variables
delay = 5 # time to wait on each page load before reading the page
driver = webdriver.Safari() # options are Chrome(), Safari(), Firefox()
page_title_selector = 'h1.pagetitle'
abstract_selector = 'div.intropara p'
album_title_selector = 'li.album-meta-item h2'
artist_selector = 'li.album-meta-item h1'
artist_url_selector = 'span.main-artist a'
score_selector = 'li.album-meta-item--rating'
author_selector = '/html/body/section[2]/div/div[1]/div[2]/ul/span/span[3]/meta'
author_url_selector = 'span.entry__author a'
country_selector = '/html/body/section[2]/div/div[1]/div[2]/ul/span/li[2]'
date_released_selector = '/html/body/section[2]/div/div[1]/div[2]/ul/span/li[1]'
review_date_selector = '/html/body/section[2]/div/div[1]/div[1]/section/header/p/time'
second_review_selector = 'time'
#album_art_selector = '/html/body/section[2]/div/div[1]/div[2]/img'


with open('lobf_output.json', 'r') as f:
    with open('lobf_results.txt', 'a') as g:
        for line in f:
            url = line
            review_url = url.strip('\n')
            print review_url
            driver.get(review_url)
            sleep(delay)

            page_title = driver.find_element_by_css_selector(page_title_selector).text
            #print page_title

            try:
                abstract = driver.find_element_by_css_selector(abstract_selector).text
                #print abstract
            except NoSuchElementException:
                abstract = 'none'

            try:
                album_title = driver.find_element_by_css_selector(album_title_selector).text
                #print album_title
            except NoSuchElementException:
                album_title = 'none'

            try:
                artist_title = driver.find_element_by_css_selector(artist_selector).text
                artist = artist_title.strip('\n')
                #print artist
            except NoSuchElementException:
                artist_title = 'none'
                artist = 'none'

            try:
                artist_url = driver.find_element_by_css_selector(artist_url_selector).get_attribute('href')
                #print artist_url
            except NoSuchElementException:
                artist_url = 'none'

            score = driver.find_element_by_css_selector(score_selector).text
            #if score == '--':
            #    score = '0'
            #else:
            #    continue
            #print score

            author = driver.find_element_by_xpath(author_selector).get_attribute('content')
            #print author

            author_url = driver.find_element_by_css_selector(author_url_selector).get_attribute('href')
            #print author_url.get_attribute('href')

            try:
                origin_country = driver.find_element_by_xpath(country_selector).text
                in_country = origin_country.strip('Country: ')
                country = in_country.strip('\n')
                #print country
            except NoSuchElementException:
                country = 'none'

            try:
                date_released = driver.find_element_by_xpath(date_released_selector).text
                in_date = date_released.strip('Release date: ')
                release_date = in_date.strip('\n')
                #print release_date
            except NoSuchElementException:
                release_date = 'none'

            try:
                date = driver.find_element_by_xpath(review_date_selector).text
                sep = ','
                review_date = date.split(sep, 1)[0]
                #print review_date
            except NoSuchElementException:
                date = driver.find_element_by_css_selector(second_review_selector).text
                sep = ','
                review_date = date.split(sep, 1)[0]

            ## THIS IS BROKEN

            # img = driver.find_element_by_xpath(album_art_selector).get_attribute('src')
            # album_name = album_title + '_' + artist + '.png'
            # print img
            # print album_name
            # urllib.urlretrieve(img, album_name)

            #####

            output = (review_date + '|' + author + '|' + author_url + '|' +
            album_title + '|' + review_url + '|' + artist + '|' + artist_url + '|' +
            release_date + '|' + score + '|' + country + '|' + page_title + '|' +
            abstract) line_break = '\n' g.write(output.encode('utf-8'))
            g.write("\n")

            print artist

    driver.close()
    driver.quit()
