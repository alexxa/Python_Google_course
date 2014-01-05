#!/usr/bin/python
#PERFORMED BY: alexxa
#DATE: 20.12.2013
#SOURCE: Google Python course https://developers.google.com/edu/python/
# https://developers.google.com/edu/python/exercises/log-puzzle


# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os, re, sys, urllib.request


"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def sort_url(url):
    
    '''
       Sort urls by the 2nd word if present.
    '''
    match = re.search(r'-(\w+)-(\w+)\.\w+', url)
    if match:
        return match.group(2)
    else:
        return url

def read_urls(filename):
    '''
        Returns a list of the puzzle urls from the given log file,
        extracting the hostname from the filename itself.
        Screens out duplicate urls and returns the urls sorted into
        increasing order.
    '''
  
    underbar = filename.index('_')
    host = filename[underbar + 1:]

    # Write the ulrs into a dictionary
    url_dict = {}

    fin = open(filename)
    for line in fin:
        match = re.search(r'"GET (\S+)', line)
        if match:
            path = match.group(1)
            if 'puzzle' in path:
                url_dict['http://' + host + path] = 1
    
    return sorted(url_dict.keys(), key=sort_url)
  

def download_images(urls, to_dir):
    '''
        Given the urls already in the correct order, downloads
        each image into the given directory.
        Gives the images local filenames img0, img1, and so on.
        Creates an index.html in the directory
        with an img tag to show each local image file.
        Creates the directory if necessary.
    '''
    if not os.path.exists(to_dir):
        os.makedirs(to_dir)
        
    index = open(os.path.join(to_dir, 'index.html'), 'w')
    index.write('<html><body>\n')
    
    i = 0
    for url in urls:
        local_name = 'img%d' % i
        print('Retrieving...', url)
        urllib.request.urlretrieve(url, os.path.join(to_dir, local_name))
        index.write('<img src="%s">' % (local_name,))
        i += 1

    index.write('\n</body></html>\n')
    index.close()

# part A - Log File To Urls
#urls = read_urls('animal_code.google.com')
#for url in urls:
#    print(url)

# part B - Download Images Puzzle
#img_urls = read_urls('animal_code.google.com')
#download_images(img_urls, 'img')

# Part C - Image Slice Descrambling
img_urls = read_urls('place_code.google.com')
download_images(img_urls, 'img2')
