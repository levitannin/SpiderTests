# -*- coding: utf-8 -*-
"""
CTF Spider -- Created for TraceLabs CTF on July 11th, 2020

This spider will access a seed website and crawl from there, identifying
pages and seeing if key words/phrases are on the webpage.

Darknet or Clearnet?  Both?

Author: @Levitannin
"""

import requests
#import json
import sys
import collections
#from stem.connection import connect # for darknet connection 
#from stem import Signal
from lxml import html, etree
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen, urljoin, URLError
from bs4 import BeautifulSoup as bs4
import ssl

SEED = "https://www.incredibleegg.org/egg-nutrition/"
SEED2 = "https://google.com"

connection = requests.session()
#connection.proxies = {}
#connection.proxies['http'] = 'socks5h://localhost:9050'
#connection.proxies['https'] = 'socks5h://localhost:9050'

s = ssl.create_default_context()
s.check_hostname = False
s.verify_mode = ssl.CERT_NONE

#Steve, the collector of URLS
steve = collections.deque()
steve.append(SEED)
steve.append(SEED2)

#Paul, the reviewer of URLS
paul = set()
paul.add(SEED)
paul.add(SEED2)
'''
def DarknetAccess():
    
    dnConn = connect()
    dnConn.authenticate()
    dnConn.signal(Signal.NEWNYM)
    
    print("Steve and Paul made it to the Darknet! \n" /
          "The Darknet path is %s" % dnConn.get_version())
    
    #Tor IP
    torCon = json.loads(connection.get('http://httpbin.org/ip').text)
    torConIP = torCon["origin"].split(',')
    
    print("The road Steve and Paul took is called: " + torConIP[0] + "\n\n")
    
    if not dnConn:
        print("Steve and Paul fell in a ditch")
        sys.exit(1)'''

def roadtrip(count):
    while len(steve):
        
        patricia = steve.popleft() #Steve hands over URL to patricia
        print(patricia)
        
        try:
            response = connection.get(patricia)
        except requests.RequestException:
            count = count + 1
            continue
    
        banana = response.content #what patricia brings back from the URL
        
        dave = html.fromstring(banana) # Dave turns the banana into something easier to handle...
        pineapple = etree.tostring(dave, pretty_print = True, method = "html")
        
        firefly = bs4(pineapple, features = "lxml")
        for telescope in firefly(["script", "stlye"]):
            telescope.decompose()
        
        stacy = list(firefly.stripped_strings)
        print("This is what Stacy found:")
        print(stacy)
        
        Alice = {urljoin(response.patricia, patricia) for patricia in dave.xpath('//a/@href')}
        
        Alice = Alice - paul
        for tomato in Alice:
            paul.add(tomato)
            steve.append(tomato)
        
        count = count +1
    
    print("And the saga of Steve and Paul, and their friends Dave, Stacy, and tomato loving Alice comes to a close")
    sys.exit(0)

if __name__ == '__main__':
    count = 0
    
    roadtrip(count)
