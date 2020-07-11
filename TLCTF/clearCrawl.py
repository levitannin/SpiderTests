#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:56:54 2020

@author: levitannin

To properly use this prototype ensure that tor is installed in the linux
commandline.  To do this follow the steps below:
    sudo apt install tor
    sudo vi /etc/tor/torrc  # Use preferred text editor/viewer
    Uncomment following lines:
        ControlPort 9051
        CookieAuthentication 1  # Set to 0
    sudo /etc/init.d/tor restart
    curl ifconfig.me    # Set up to check ip address
    torify curl ifconfig.me 2>/dev/null     # check ip address -- verify tor connection

This is a bare-bones clear-near crawler.  With time, the crawler will
have machine learning modules added to it in order to better identify data online.
This can be run in tandem with TorCrawl.py

Database storage has been removed.
Killswitch set to 1 hr.
"""
import requests
import json
import sys, time
import collections
from stem.connection import connect # for darknet connection 
from stem import Signal
import logging
from lxml import html, etree
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs4

SEED = {
        "Names go Here",
        "Also key phrases, like usernames or emails",
        "Full sentences can too, but unlikely to get results."
        }

STARTCLEAR = [
    'Google the seed, put in the google URL that results.'
    ]

inurlq_clear = collections.deque()
foundLinks_clear = set()
for link in STARTCLEAR:
    inurlq_clear.append(link)
    foundLinks_clear.add(link)

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

def spyderBody_clear():
    start = time.time()
    count = 0
    identified = []
    
    while len(inurlq_clear):
        url = inurlq_clear.popleft()
        
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
        scrapedLinks = scrapedLinks - foundLinks_clear
        
        soup = bs4(result, features = "lxml")
        for script in soup(["script", "style"]):
            script.decompose()
        linesText = soup.stripped_strings
        linesText = ''.join(linesText)
        
        for link in scrapedLinks:
            if ".onion" not in link:
                foundLinks_clear.add(link)
                inurlq_clear.append(link)
        
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
                    break
                count = count + 1
                continue
        
        finish = time.time()
        killswitch = round(finish - start, 2)
        if killswitch >= 3200.00:
            break

if __name__ == '__main__':
    connecTor()
    id_url = spyderBody_clear()
    
    print("The run has completed.")
    print()
    print("Identified urls are: ")
    print(id_url)
