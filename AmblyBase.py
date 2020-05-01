#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
    
In cases where a new IP may be necessary, run the following command:
    echo -e 'AUTHENTICATE ""\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051
    curl ifconfig.me
    torify curl ifconfig.me 2>/dev/null
"""

import requests #   handle HTTP/HTTPS connections
from lxml import html, etree #  Parse HTML
from urllib.parse import urlparse
from urllib.parse import urljoin
import collections #    work with queues
import sys #    work with argv

try:
    # Suppress the warnings for SSL connections
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except:
    pass

# Argument to the code -- fed-in URL from commandline
START = sys.argv[1]

# Stores all the URLs found
# Add this value to the START value to avoid multiple instances of the same URL
urlq = collections.deque()
urlq.append(START)

found = set()
found.add(START)

while len(urlq):
    # grab left-most item from the queue
    url = urlq.popleft()
    
    # Use the pulled item to request the (tor)webpage.
    response = requests.get(url)
    # Gather the contents of the page.
    body = html.fromstring(response.content)
    
    # Formats into human-readable text then prints.
    result = etree.tostring(body, pretty_print = True, method = "html")
    print(result)
    
    # Find all links without leaving the site
    # Create another for off-site links
    inlinks = {urljoin(response.url, url) for url in body.xpath('//a/@href') if urljoin(response.url, url).startswith(START)}
    #exlinks = {urljoin(response.url, url) for url in body.xpath('//a/@href') if not urljoin(response.url, url).startswith(START)}
    
    # These are the gathered links.
    print("THESE INTERNAL LINKS WERE FOUND")
    for link in inlinks:
        print()
        print(link)
    
    '''print("THESE EXTERNAL LINKS WERE FOUND")
    for links in exlinks:
        print()
        print(links)'''
    
    # Add new URLs to list while removing any already found.
    for link in (inlinks - found):
        found.add(link)
        urlq.append(link)
    '''for link in (exlinks - found):
        found.add(link)
        urlq.append(link)'''

print("The following are all found links:")
for link in found:
    print()
    print(link)
