#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pulls every album review listed in the scrape-output input file (this file comes from the url_scrape code)
#a fair warning -- if you are generating a dataset of the entire Pitchfork corpus, expect it to take several days

from time import sleep
import json
import csv
import urllib
import urllib.request as ur

# don't mess with these variables
delay = 5 # time to wait on each page load before reading the page

with open('scrape-output-1.json', 'r') as f:
    x = 0
    for row in f:
        url = row

        review_url = url.strip('/\n')
        #review_url = review_url.strip('htt')
        #review_url = review_url.strip('ps')
        #review_url = review_url.strip('://')
        #print(row)
        #print(review_url)

        html_name = review_url.strip('htt')
        html_name = html_name.strip('ps')
        html_name = html_name.strip('://')
        html_name = html_name.strip('pitchfork')
        html_name = html_name.strip('.com')
        html_name = html_name.strip('/reviews/albums/')

        #print(html_name)

        html = './raw-html/' + html_name + '.html'

        urllib.request.urlretrieve(review_url, html)
        #ur.urlretrieve(review_url, review_url_html)

        #print(review_url_html)
        print(review_url)
        x = x + 1
        print(x)


        sleep(delay)
