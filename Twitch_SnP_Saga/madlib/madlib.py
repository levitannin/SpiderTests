#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:42:52 2020

Steve and Paul like to play games.  They've decided to fill in a madlib together,
but being true to themselves, neither want to do this the easy way.

This is a spider that will go to a provided seed URL, scrape the text, then use
machine learning algorithms to identify parts of speech for filling out a madlib!

@author: levitannin
"""
#   Libraries used in this layer of the program, including other mods we've made.
import sys
import requests, ssl
from lxml import html, etree
from bs4 import BeautifulSoup as bs4
from madlib_PoS import PartsofSpeech

#   Connecting to the network -- setting up the request system for the URL
conn = requests.session()

#   A wrapper for socket objects (ssl == Secure Sockets Layer)
s = ssl.create_default_context()
s.check_hostname = False
s.verify_mode = ssl.CERT_NONE


#   Steve and Paul are going on a roadtrip to the given URL, which allows them
#       to gather text for giving to the Parts of Speech module!
def roadtrip(url, error_count):
    #   This try-block is to help the user ensure a viable website is input
    try:
        response = conn.get(url)
    except requests.RequestException:
        #   If the URL fails, the user has up to 5 tries to get a viable URL
        error_count = error_count + 1
        
        print('ERROR: This url is not accessable!')
        if error_count == 5:
            print('Terminating: Too many Failed Attempts')
            sys.exit()
        else:
            userInput(error_count)
            return
    
    #   The response from duck (our connection to the internet).
    #   This is the raw information from the webpage.
    data = response.content
    
    #   Pulling out the html format from the raw data.
    pull = html.fromstring(data)
    #   Make the html readable to humans.
    readble = etree.tostring(pull, pretty_print = True, method = "html")
    
    #   Take out the unnecessary stuff!  We just want the text--plain and simple
    features = bs4(readble, features = "lxml")
    for f in features(["script", "style"]):
        f.decompose()
    
    #   Get the text in the form of lists, these lists come from the ends of 
    #       phrases, sentences, or breaks in the original code.
    scraped_text = list(features.stripped_strings)
    #   Join the strings together to get the whole text in one large corpus.
    scraped_text = ''.join(scraped_text)
    
    #   Call to the Natural Language Processing (NLP) module we're working on
    PartsofSpeech(scraped_text)

#   This function is to help make sure the user is inputting a valid URL;
#       called by the try-block in roadtrip() if necessary.
def userInput(error_count):
    url = str(input("Please supply a URL for the spider: ... \n"))
    roadtrip(url, error_count)
    

if __name__ == '__main__':
    error_count = 0
    userInput(error_count)
    
    #   Closing statement to make sure we're hitting the end of the program.
    print("\n\n\tTime for the spider to take a nap...")
    sys.exit()
