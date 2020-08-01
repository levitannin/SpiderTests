#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 15:24:27 2020

More examples of NLTK tutorials can be found:
    https://github.com/levitannin/ml-training/tree/master/tutorials_sentdex/NLTK

The following are parts of speech that we care about for the madlib, keep 
these in mind for the parsing we'll be doing in this module.
    Parts of Speech to Tag:
        JJ      -- Adjective
        JJR     -- Adjective, Compariative
        JJS     -- Adjective, superlative
        NN      -- Noun, singular
        NNS     -- Noun plural
        NNP     -- Proper Noun, Singular
        NNPS    -- Proper Noun, Plural
        RB      -- Adverb 
        RBR     -- Comparitive
        RBS     -- Adverb Superlative
        VB      -- Verb
        VBD     -- Verb, past tense
        VBG     -- Verb, present particle
        VBN     -- Verb, past particle
        VBP     -- Verb, singular present
        VBZ     -- Verb, person singular, present.

The different lists of words pulled from the scraped text will be pushed to the
madlib module (madlib_choice.py).

@author: levitannin
"""


from nltk.tokenize import word_tokenize, PunktSentenceTokenizer, sent_tokenize
from nltk import pos_tag
from madlib_choice import wordChoice

#   Use this commented out section of code to download all dependencies you may need.
#nltk.download()

def PartsofSpeech(corpus):
    print("Got it!")
    
    NounList = ['NN', 'NNS', 'NNP', 'NNPS']
    VerbList = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    ADJList = ['JJ', 'JJR', 'JJS']
    ADVList = ['RB', 'RBR', 'RBS']
    NN = []
    VB = []
    ADJ = []
    ADV = []
    
    
    token = sent_tokenize(corpus)
    try:
        for i in token:
            words = word_tokenize(i)
            
            for tag in pos_tag(words):
                if tag[1] in NounList:
                    NN.append(tag[0])
                elif tag[1] in VerbList:
                    VB.append(tag[0])
                elif tag[1] in ADJList:
                    ADJ.append(tag[0])
                elif tag[1] in ADVList:
                    ADV.append(tag[0])
        
    except Exception as e:
        print(str(e))
    
    wordChoice(NN)
