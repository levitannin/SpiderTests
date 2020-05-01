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
import sys
from lxml import html, etree #  Parse HTML
from urllib.parse import urljoin
import collections #    work with queuesi
from bs4 import BeautifulSoup

inLinks = open('internal_links.txt', 'w')
exLinks = open('external_links.txt', 'w')
wpData = open('scraped_pages.txt', 'w+')

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
inurlq = collections.deque()
inurlq.append(START)
exurlq = collections.deque()

infound = set()
infound.add(START)
exfound = set()

def reviewOp():
    print("Choose one of the Following Review Choices:")
    print()
    print("1 Internal Urls")
    print("2 External URLs")
    print("3 Back to Main Menu")
    print()
    choice = int(input("Input the numeric value for your choice: "))
    
    if(choice == 1):
        reviewIn()
    elif(choice == 2):
        reviewEx()
    elif(choice == 3):
        main()
    else:
        print("ERROR: Invalid Input")
        reviewOp()

def reviewIn():
    # grab left-most item from the queue
    url = inurlq.popleft()
    
    # Use the pulled item to request the (tor)webpage.
    response = requests.get(url)
    # Gather the contents of the page.
    body = html.fromstring(response.content)
    
    # Formats into human-readable text then prints.
    result = etree.tostring(body, pretty_print = True, method = "html")
    soup = BeautifulSoup(result)
    for script in soup(["script", "style"]):
        script.decompose()
    linesText = list(soup.stripped_strings)
    print(linesText)
    #content(result)
    
    # Find all links without leaving the site
    # Create another for off-site links
    inlinks = {urljoin(response.url, url) for url in body.xpath('//a/@href') if urljoin(response.url, url).startswith(START)}
    exlinks = {urljoin(response.url, url) for url in body.xpath('//a/@href') if not urljoin(response.url, url).startswith(START)}
    
    # Add new URLs to list while removing any already found.
    for link in (inlinks - infound):
        infound.add(link)
        inurlq.append(link)
    for link in (exlinks - exfound):
        exfound.add(link)
        exurlq.append(link)
    main()

def reviewEx():
    # grab left-most item from the queue
    url = exurlq.popleft()
    
    # Use the pulled item to request the (tor)webpage.
    response = requests.get(url)
    # Gather the contents of the page.
    body = html.fromstring(response.content)
    
    # Formats into human-readable text then prints.
    result = etree.tostring(body, pretty_print = True, method = "html")
    content(result)
    
    # Find all links without leaving the site
    # Create another for off-site links
    inlinks = {urljoin(response.url, url) for url in body.xpath('//a/@href') if urljoin(response.url, url).startswith(START)}
    exlinks = {urljoin(response.url, url) for url in body.xpath('//a/@href') if not urljoin(response.url, url).startswith(START)}
    
    # Add new URLs to list while removing any already found.
    for link in (inlinks - infound):
        infound.add(link)
        inurlq.append(link)
    for link in (exlinks - exfound):
        exfound.add(link)
        exurlq.append(link)
    main()

def content(result):
    '''pullText = result.join(html.select("//body//text()").extract()).strip()
    wpData.write(pullText)
    print(pullText)
    '''
    soup = BeautifulSoup(result)
    for script in soup(["script", "style"]):
        script.decompose()
    linesText = list(soup.stripped_strings)
    
    print(linesText)
    
    for line in linesText:
        wpData.write(line)
        
    main()

def storeIn(inLinks):
    print("The following are links found related to the starter URL: \n")
    for link in infound:
        print()
        print(link)
        inLinks.write(link)
        inLinks.write('\n')
    
    main()
        

def storeEx(exLinks):
    print("The following are all found links:")
    for link in exfound:
        print()
        print(link)
        exLinks.write(link)
        exLinks.write('\n')
    
    main()

def closeOut():
    inLinks.close()
    exLinks.close()
    wpData.close()
    sys.exit("All Files Closed.  Terminating Program")

def main():
    print("Ambly Menu:")
    print("1 Review Next Link")
    print("2 Store and Print Web-page Content")
    print("3 Store and Print Internal URLs found")
    print("4 Store and Print External URLs found")
    print("5 Quit")
    print()
    choice = int(input("Input your choice of the above options: "))
    
    if (choice == 1): reviewOp()
    elif(choice == 2): content()
    elif(choice == 3): storeIn(inLinks)
    elif(choice == 4): storeEx(exLinks)
    elif(choice == 5): closeOut()
    else:
        print("ERROR: Invalid Input")
        main()

if __name__ == '__main__':    
    main()