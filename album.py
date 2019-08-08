#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pulls every album review listed in the scrape-output input file (this file comes from the url_scrape code)
#a fair warning -- if you are generating a dataset of the entire Pitchfork corpus, expect it to take several days

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import json
import csv
import urllib
import urllib.request as ur

# don't mess with these variables
delay = 5 # time to wait on each page load before reading the page
driver = webdriver.Safari() # options are Chrome(), Safari(), Firefox()

album_selector = 'h1.single-album-tombstone__review-title'
artist_selector = 'ul.artist-links li'
score_selector = 'span.score'
record_label_selector = 'ul.label-list li'

# error being thrown here
year_selector = 'span.single-album-tombstone__meta-year'

review_author_selector = 'ul.authors-detail a'
genre_selector = 'ul.genre-list a'
date_published_selector = 'time.pub-date'
abstract_selector = 'div.review-detail__abstract'
accolades_selector = 'p.bnm-txt'
album_art_selector = 'div.single-album-tombstone__art img'
artist_url_selector = 'ul.artist-links li a'

with open('scrape-output-1.json', 'r') as f:
    with open('scrape-results.txt', 'a') as g:
        for line in f:
            artist_list = []
            genre_list = []
            record_label_list = []
            artist_url_list = []
            genre_url_list = []

            artist1 = 'blank'
            artist2 = 'blank'
            artist3 = 'blank'

            x = 0

            url = line
            review_url = url.strip('\n')
            driver.get(review_url)
            sleep(delay)

            try:

                # artist and artist url block

                artist_name = driver.find_elements_by_css_selector(artist_selector)
                print('{} artists found.'.format(len(artist_name)))
                for artist in artist_name:
                    artist_list.append(artist.text)

                artist_url = driver.find_elements_by_css_selector(artist_url_selector)
                print('{} artist urls found.'.format(len(artist_url)))
                for url in artist_url:
                    artist_url_list.append(url.get_attribute('href'))

                try:
                    artist1 = artist_list[0]
                except IndexError:
                    with open ('urls.txt', 'a') as g:
                        g.write(review_url)
                    continue

                if '/' in artist1:
                    corrected_artist1 = artist1.replace('/', '')
                else:
                    corrected_artist1 = artist1

                try:
                    artist_url1 = artist_url_list[0]
                except IndexError:
                    artist_url1 = 'none'

                try:
                    artist2 = artist_list[1]
                    artist_url2 = artist_url_list[1]
                except IndexError:
                    artist2 = 'none'
                    artist_url2 = 'none'

                try:
                    artist3 = artist_list[2]
                    artist_url3 = artist_url_list[2]
                except IndexError:
                    artist3 = 'none'
                    artist_url3 = 'none'

                # record label block

                record_label = driver.find_elements_by_css_selector(record_label_selector) # these aren't appearing?
                print('{} record labels found.'.format(len(record_label)))
                for label in record_label:
                    record_label_list.append(label.text)

                try:
                    record_label1 = record_label_list[0]
                except IndexError:
                    record_label1 = 'none'

                try:
                    record_label2 = record_label_list[1]
                except IndexError:
                    record_label2 = 'none'

                try:
                    record_label3 = record_label_list[2]
                except IndexError:
                    record_label3 = 'none'

                # genre and genre url block

                try:
                    genres = driver.find_elements_by_css_selector(genre_selector)
                    print('{} genres found.'.format(len(genres)))
                    for genre in genres:
                        genre_list.append(genre.text)

                    genre_url = driver.find_elements_by_css_selector(genre_selector)
                    print('{} genre urls found.'.format(len(genre_url)))
                    for url in genre_url:
                        genre_url_list.append(url.get_attribute('href'))

                    try:
                        genre1 = genre_list[0]
                        genre_url1 = genre_url_list[0]
                    except IndexError:
                        genre1 = 'none'
                        genre_url1 = 'none'

                    try:
                        genre2 = genre_list[1]
                        genre_url2 = genre_url_list[1]
                    except IndexError:
                        genre2 = 'none'
                        genre_url2 = 'none'

                except NoSuchElementException:
                    genre1 = 'NONE'
                    genre_url1 = 'NONE'

                # accolades block

                try:
                    accolades = driver.find_element_by_css_selector(accolades_selector).text
                except NoSuchElementException:
                    accolades = 'none'

                # date published block

                date_published = driver.find_element_by_css_selector(date_published_selector).text

                # other (easier) metadata block

                review_author = driver.find_element_by_css_selector(review_author_selector).text
                review_author_url = driver.find_element_by_css_selector(review_author_selector).get_attribute('href')

                abstract = driver.find_element_by_css_selector(abstract_selector).text

                score = driver.find_element_by_css_selector(score_selector).text

                # album block to catch instances of / in album titles

                album = driver.find_element_by_css_selector(album_selector).text
                if '/' in album:
                    corrected_album = album.replace('/', '')
                else:
                    corrected_album = album

                # removes the weird bullet point from the published year

                inter_year = driver.find_element_by_css_selector(year_selector).text
                inter_year_2 = inter_year.replace(u'\u2022', '')
                year = inter_year_2.replace('  ', '')

                # collects the album art image

                img = driver.find_element_by_css_selector(album_art_selector).get_attribute('src')
                album_name = './album-art/' + corrected_album + '_' + corrected_artist1 + '.png'
                urllib.request.urlretrieve(img, album_name)

                # writes to external file

                output = (date_published + '|' + review_author + '|' + review_author_url + '|' + album + '|' + review_url + '|' + artist1 + '|' + artist_url1 + '|' + artist2 + '|' + artist_url2 + '|' + artist3 + '|' + artist_url3 + '|' + genre1 + '|' + genre_url1 + '|' + genre2 + '|' + genre_url2 + '|' + year + '|' + record_label1 + '|' + record_label2 + '|' + record_label3 + '|' + score + '|' + accolades + '|' + abstract + '|' + album_name)
                line_break = '\n'
                g.write(output)
                g.write("\n")

                review_url_html = './raw-html/' + corrected_album + '_' + corrected_artist1 + '.html'
                urllib.request.urlretrieve(review_url, review_url_html)

                print(album + ' ' + artist1)

                sleep(delay)

            except ValueError:
                with open ('urls.txt', 'a') as g:
                    g.write(review_url)
                    g.write("\n")
                continue

        driver.close()
