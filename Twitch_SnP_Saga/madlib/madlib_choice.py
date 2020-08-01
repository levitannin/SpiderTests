#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:44:32 2020

This module will hold the madlib that we'll be working with, unless we bring
in multiple madlibs to choose between.  That may extend it!

There are a few functions which will work to pull a word out of the parts of 
speech lists we made in madlib_PoS at random to fill in our madlib as necessary.

We'll be focusing on this module in the next tutorial!

@author: levitannin
"""
from random import *

def wordChoice(PoS_List):
    
    r = randint(1, len(PoS_List))
    word = PoS_List[r]
    print(r, word)
    
    return word
