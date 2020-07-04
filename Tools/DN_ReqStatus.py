#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:38:12 2020

@author: leviathancove
"""

import requests #   handle HTTP/HTTPS connections
import json, sys
from stem.connection import connect
from stem import Signal

SITES = [
    "http://torwikignoueupfm.onion/",
    "http://levitannin.github.io/failcheck",
    ]

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

# Establish connection to Tor using Stem library.
controller = connect()
controller.authenticate()
controller.signal(Signal.NEWNYM)
print("Connected to Tor, running version %s" % controller.get_version())

# Identify base system's IP address
base = json.loads(requests.get('http://httpbin.org/ip').text)
baseIP = base["origin"].split(',')

# Identify Tor connection IP address
torCon = json.loads(session.get('http://httpbin.org/ip').text)
torConIP = torCon["origin"].split(',')

print("Base IP address: " + baseIP[0] + 
      "\n Tor connection IP: " + torConIP[0]  + "\n\n")

if not controller:
    # If unable to connect to the Tor network, exit the program.
    print("ERROR: Unable to establish connection to Tor network.  Exiting.")
    sys.exit(1)

for site in SITES:
    r = session.get(site) 
    conn = r.status_code

    print ("{0:30} {1:10} {2:10}".format(site, conn, r.reason))
