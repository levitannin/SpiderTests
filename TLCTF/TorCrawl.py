#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:56:54 2020

@author: levi

URL Seeds:
    Doris Hingel
        http://msydqstlz2kzerdg.onion/search/?q=Doris+Hingel
    
    David Mawut Abuoi -- Need more info; username; email
    
    Daniel Navarro
        http://msydqstlz2kzerdg.onion/search/?q=Daniel+Navarro
        http://xmh57jrzrnw6insl.onion/4a1f6b371c/search.cgi?s=DRP&q=Daniel+Navarro&cmd=Search%21
        http://hss3uro2hsxfogfq.onion/index.php?q=Daniel+Navarro&session=ftZ2BC520VQfaPJCG%2Fi1whTpgB3OIgsOnfiCfg8bEok%3D&numRows=20&hostLimit=20&template=0
    
    Lindsey Galvan
        http://msydqstlz2kzerdg.onion/search/?q=Lindsey+Galvan
        http://xmh57jrzrnw6insl.onion/4a1f6b371c/search.cgi?s=DRP&q=Lindsey+Galvan&cmd=Search%21
        http://hss3uro2hsxfogfq.onion/index.php?q=Lindsey+Galvan&session=1WAk2vW5jCswR3jjVwbDQAsbDPR4WfXAFGDniBme75Q%3D&numRows=20&hostLimit=20&template=0
    
    Tymayrra Ayala
        http://msydqstlz2kzerdg.onion/search/?q=Tymayrra+Ayala
    
    Tabitha Tennyson
        http://msydqstlz2kzerdg.onion/search/?q=Tabitha+Tennyson
        http://hss3uro2hsxfogfq.onion/index.php?q=Tabitha+Tennyson&session=XlY6T2fYQ%2BUL63VDQZqdd3U9oL1fRax79Cza%2Bc3CPSs%3D&numRows=20&hostLimit=20&template=0
    
    Alejandra Nava
        http://msydqstlz2kzerdg.onion/search/?q=Alejandra+Nava
        http://hss3uro2hsxfogfq.onion/index.php?q=Alejandra+Nava&session=4buHh3PPuyMeipmd7Ij8W%2B5VDYaxyTrJOZwBMrQPSGw%3D&numRows=20&hostLimit=20&template=0
    
    Mercedes Toliver
        http://msydqstlz2kzerdg.onion/search/?q=Mercedes+Toliver
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
