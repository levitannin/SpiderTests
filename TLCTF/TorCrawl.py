#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:56:54 2020

@author: levi
"""
import requests
import json
import sys, time
import collections
import concurrent.futures
from stem.connection import connect # for darknet connection 
from stem import Signal
import logging
from lxml import html, etree
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs4
import connectDB

SEED = {
        "Names go Here",
        "Also key phrases, like usernames or emails",
        "Full sentences can too, but unlikely to get results."
        }

STARTTOR = [
    'I will provide URLs for the Darknet',
    'See above'
            ]

inurlq_Tor = collections.deque()
foundLinks_Tor = set()
for link in STARTTOR:
    inurlq_Tor.append(link)
    foundLinks_Tor.add(link)

conn = requests.session()
conn.proxies = {}
conn.proxies['http'] = 'socks5h://localhost:9050'
conn.proxies['https'] = 'socks5h://localhost:9050'

try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except:
    pass

def connecTor():
    controller = connect()
    controller.authenticate()
    controller.signal(Signal.NEWNYM)
    print("Connected to Tor, running version %s," % controller.get_version())
    
    base = json.loads(requests.get('http://httpbin.org/ip').text)
    baseIP = base["origin"].split(',')
    
    tor = json.loads(conn.get('http://httpbin.org/ip').text)
    torIP = tor["origin"].split(',')
    
    print("Base IP address: " + baseIP[0] +
          "\n Tor connection IP: " + torIP[0] + "\n\n")
    
    if not controller:
        print("ERROR: Unable to establish connection to Tor network. Existing.")
        sys.exit(1)

def spyderBody_Tor():
    start = time.time()
    count = 0
    identified = []
    
    while len(inurlq_Tor):
        url = inurlq_Tor.popleft()
        
        try:
            response = conn.get(url)
        except requests.RequestException:
            count = count + 1
            continue
        
        spyHTML = response.content
        
        try:
            body = html.fromstring(spyHTML)
        except:
            if isinstance(body, etree.ParserError) and 'empty' in str(body):
                logging.warning("html_sanitize failed to parse %s" % url)
            count = count + 1
            continue
        
        try:
            result = etree.tostring(body, pretty_print = True, method = "html")
        except:
            count = count + 1
            continue
        
        scrapedLinks = {urljoin(response.url, url) for url in body.xpath('//a/@href')}
        scrapedLinks = scrapedLinks - foundLinks_Tor
        
        soup = bs4(result, features = "lxml")
        for script in soup(["script", "style"]):
            script.decompose()
        linesText = soup.stripped_strings
        linesText = ''.join(linesText)
        
        for link in scrapedLinks:
            if ".onion" in link:
                foundLinks_Tor.add(link)
                inurlq_Tor.append(link)

        for s in SEED:
            if s in linesText:
                print("CLEARNET: Seed: " + s + " found at: " + url)
                identified.append(url)
                count = count + 1
            else: 
                print('Not Found')
                finish = time.time()
                killswitch = round(finish - start, 2)
                if killswitch >= 3200.00:
                    return identified
                    break
                count = count + 1
                continue
        
        finish = time.time()
        killswitch = round(finish - start, 2)
        if killswitch >= 3200.00:
            return identified
            break

if __name__ == '__main__':
    connecTor()
    id_url = spyderBody_Tor()
     
    print("The run has completed.")
    print()
    print("Identified urls are: ")
    print(id_url)
