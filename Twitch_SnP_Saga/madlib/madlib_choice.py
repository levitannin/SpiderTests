#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:44:32 2020

This module will hold the madlib that we'll be working with, unless we bring
in multiple madlibs to choose between.  That may extend it!

There are a few functions which will work to pull a word out of the parts of 
speech lists we made in madlib_PoS at random to fill in our madlib as necessary.

Madlibs for testing brought to us by Google and:
    https://www.it.iitb.ac.in/~vijaya/ssrvm/worksheetscd/getWorksheets.com/Language%20Arts/madlibsdoc.pdf

@author: levitannin
"""
from random import *

def wordChoice(PoS_List):
    
    r = randint(1, len(PoS_List))
    word = PoS_List[r]
    #print(r, word)
    
    return word

def MonkeyKing(NN, ADJ, ADV, VB):
    
    print("This Madlib is called: 'The Monkey King!'\n")
    
    verb = wordChoice(VB)
    noun = wordChoice(NN)
    adjective = wordChoice(ADJ)
    adverb = wordChoice(ADV)
    
    print("The day I saw the Monkey King ", verb, " was one of the most " \
          "interesting days of the year.  After he did that, the king played " \
              "chess on his brother's ", noun, " and then combed his ", adjective, 
              "hair with a comb made out of old fish bones.  Later that same " \
                  "day, I saw the Monkey King dance ", adverb, "in front of " \
                      "an audience of kangaroos and wombats.")

def DisneyTrip(NN, ADJ, VB):
    
    Vehicles = [
        "Suspension Railway",
        "Coco Taxi",
        "Monte Toboggan",
        "Bamboo Train",
        "Maglev",
        "DUKW",
        "Dog Sleds",
        "Gondola",
        "Barco de Totora",
        "Underground Funicular",
        "Reindeer Sled",
        "Felucca Boats"
        ]
    Disney = [
        "Darla",
        "Sully",
        "Mary Poppins",
        "Elsa",
        "Anna",
        "Minnie Mouse",
        "Tinker Bell",
        "Fawn",
        "the Incredibles",
        "Lilo",
        "Stitch",
        "Woody",
        "Buzz Lightyear",
        "Lizzie",
        "Nemo",
        "Dory",
        "Marlin",
        "Kuzco",
        "Alice"
        "Mad Hatter",
        "Big Hero 6",
        "Powerline",
        "Dalmations",
        "Oozma Kappa Fraternity",
        "the Muses",
        "Aliens",
        "Hannah Montana",
        "Proto Zoa",
        "Belle",
        "the Cheetah Girls",
        "Maleficent",
        "Penny Proud"
        ]
    verb = []
    noun = []
    adjective = []
    
    friend = str(input("What is a friend's name for the story?"))
    n = randint(1, 100000)
    vehicle = wordChoice(Vehicles)
    disney = wordChoice(Disney)
    i = 0
    while(i < 6):
        v = wordChoice(VB)
        verb.append(v)
        i += 1
    i = 0
    while(i < 3):
        n = wordChoice(NN)
        noun.append(n)
        i += 1
    i = 0
    while(i < 5):
        adj = wordChoice(ADJ)
        adjective.append(adj)
        i += 1
    
    print("Last month, I went to Disney World with ", friend, ". We traveled " \
          "for ", n, " by ", vehicle, ". Finally, we arrived and it was very ",
          adjective[1], ".  There were also people dressed up in ", disney, 
          "costumes. \n\n I wish it had been more ", adjective[2], ", but we ", 
          verb[1], " anyway.  We also went on a(n)", adjective[3],
          " ride called Magic ", noun[1], ". ", friend, " nearly fell off a ride" \
              " and had to be ", verb[2], ".  Later, we went to the hotel and ",
              verb[3], ".  Next year, I want to go to (the)", noun, " where we can",
              verb[4], ".")
    

def GreatToy(NN, ADJ, ADV, VB):
    """There is a new toy on the market that has everyone saying 
    ____________(exclamation)! It is called the ____________(sound) 
    ____________(adjective) ____________(noun) box, and will be in stores in 
    ____________(a month). The ____________(sound)  ____________(adjective) 
    ____________(noun) box is a new gadget that  lets you do just about 
    anything! It ____________(verb)s, it ____________(verb)s, and it even 
    serves ____________(a beverage)! It is easy to operate and requires no 
    instructions!  You can also have it custom made any size up to 
    ____________(number) inches or a  ____________ (color) to glow in the  
    dark at no extra charge! The original product is pocket-sized and 
    ____________ (color). There are ____________(number) jacks on the  
    product for 6V DC power and for upgrades and add-ons. You can add  
    head-phones, ____________(plural noun) monitors, 
    ____________(plural  noun), and more! It’s possible to use them all at the 
    same time! """

def BigMacWho(NN, ADJ, ADV, VB):
    """Big Mc_______________(a last name) had a _______________(noun), 
    ____(a letter)- ______(3 letter noun), ____(a letter)- _____(3 letter noun) 
    O. On this _______________(noun) he had some _______________(plural  noun),
    ____(a letter) -3 ________(3 letter noun),____(a letter)-________(3 letter 
    noun) O. With a __________(type of sound)-__________(type of sound) here, 
    and a __________(type of sound)-__________(type of sound) there, everywhere 
    a __________(type of sound)-__________(type of sound)  
    ____(a letter)-  ________(3 letter noun), 
    ____(a letter)-________(3 letter noun) O."""

def VideoGame(NN, ADJ, ADV, VB):
    """I,  the _______________(adjective) and __________(adjective)
    _______________(a first name) has _______________(past tense verb) 
    _______________(a first name)'s _______________(adjective)  
    sister and plans to steal her _______________(adjective) 
    _______________(plural noun)! What are a ________(large  animal) 
    and backpacking __________(small animal) to do?  
    Before you can help _______________(a girl's name),  
    you'll have to collect the ___________(adjective)  
    _______________(plural noun) and _____________(adjective)  
    _______________(plural noun) that open up the  _______________(number 1-50)
    worlds connected to a _______________(first name's) lair. 
    There are _______________(number) _______________(plural noun) 
    and  _______________(number) _______________(plural noun) in the game, 
    along with hundreds of other goodies for you to find"""

def Jungle(NN, ADJ, ADV, VB):
    """I walk through the color jungle. I take out my _______________(adjective)
    canteen. There's a ________(adjective) parrot with a ______________(adjective)
    _______________(noun) in his mouth right there in front of me in the 
    _________(adjective) trees! I gaze at his __________(adjective) 
    _______________(noun). A sudden sound awakes me from my daydream! 
    A panther’s _______________(verb) in front of my head! I 
    _______________(verb) his _______________(adjective)breath. 
    I remember I have a packet of _________(noun)that makes go into a deep 
    slumber! I __________(verb)it away from me in front of the 
    _______________(noun).Yes he's eating it! I _______________(verb) away 
    through the ____________(adjective) jungle. I meet my parents at the tent. 
    Phew! It’s been an exciting day in the jungle."""

def FirstDaySchool(NN, ADJ, ADV, VB):
    """One very nice morning near the end of summer, my mother woke me up at 
    4:00 A.M. and said, "Wake up and smell the grass, sleepy head! Today is 
    your first day of school and you can't be late." I groaned in my bed for 
    twenty seconds, but eventually I got dressed. I wore a blue and white 
    striped, long sleeve _______________(noun) with a collar on it, a red tie, 
    dark gray pants, white socks, black shoes, and a(n) 
    _______________(adjective) hat. In ten minutes I made lunch and ate my 
    breakfast. _______________(number)minutes later, the bus came. A few 
    minutes later, I was at school.  In school, I met two really 
    _______________(adjective) kids. All of us became friends very fast. That 
    day we had Science, and luckily my friends and I were at the same 
    _______________(noun) .My friends' names are _______________(proper noun) 
    and _______________(proper noun). In Math we weren't together, and that 
    really bugged me. We learned what _______________(plural noun) were, and 
    when to use them. At snack and recess, we played a game  together. It was 
    extremely fun. At P. E., we were ____________(-ing verb) off of the ropes 
    onto _______________(plural noun). I thought it was a very 
    _______________(adjective) idea. In swimming class, we needed to swim 
    extremely _______________(adverb), or else we would have to swim longer.  
    Before I knew it, school was over. I grabbed all my belongings and put 
    them into my backpack. In two minutes, the bus came. As I stepped into the 
    bus I shouted, "Goodbye, adios amigos, and shalom," to my friends. Then I 
    went into the bus. In a flash, I was back home. This day was an extremely 
    exciting day!"""   
    
def Arcade(NN, ADJ, ADV, VB):
    """When I go to the arcade with my ____________ (plural noun) there are 
    lots of games to play. I spend lots of time there with my friends. In the 
    game X-Men you can be different ____________ (plural noun). The point of 
    the game is to ____________(verb) every robot. You also need to save people. 
    Then you can go to the next level.  In the game Star Wars you are Luke 
    Skywalker and you try to destroy every ____________(noun). In a car 
    racing/motorcycle racing game you need to beat every computerized vehicle 
    that you are ____________ (-ing verb) against.  There are a whole lot of 
    other cool games. When you play some games you win 
    ____________ (plural noun) for certain scores. Once you're done you can 
    cash in your tickets to get a big ______(noun). You can save your 
    ____________ (plural noun) for another time. When I went to this arcade I 
    didn't believe how much fun it would be. So far I have had a lot of fun 
    every time I've been to this great arcade!"""

def FunPark(NN, ADJ, ADV, VB):
    """Today, my fabulous  camp group went to a (an) ____________ (adjective) 
    amusement park. It was a fun park with lots of cool 
    ____________ (plural noun) and enjoyable play structures. When we got 
    there, my kind counselor shouted loudly, "Everybody off the 
    ____________ (noun)." We all pushed out in a terrible hurry. My counselor 
    handed out yellow tickets, and we scurried in. I was so excited! I couldn't
    figure out what exciting thing to do first. I saw a scary roller coaster I 
    really liked so, I ____________ (adverb) ran over to get in the long line 
    that had about ____________ (number) people in it. When I finally got on 
    the roller coaster I was ____________ (past tense verb). In fact I was so 
    nervous my two knees were knocking together. This was the 
    ____________ (-est adjective) ride I had ever been on! In about two minutes
    I heard the crank and grinding of the gears. That’s when the ride began! 
    When I got to the bottom, I was a little ____________ (past tense verb) 
    but I was proud of myself. The rest of the day went ____________ (adverb). 
    It was a(n) ____________ (adjective) day at the fun park."""

def Zoo(NN, ADJ, ADV, VB):
    """Today I went to the zoo. I saw a(n) ___________(adjective)
    _____________(Noun) jumping up and down in its tree.  He 
    _____________(verb, past tense) __________(adverb)through the large tunnel 
    that led to its _______(adjective) __________(noun). I got some peanuts 
    and passed  them through the cage to a gigantic gray _______(noun)towering 
    above my head. Feeding that animal made  me hungry. I went to get a 
    __________(adjective) scoop  of ice cream. It filled my stomach. Afterwards
    I had to __________(verb) __________ (adverb) to catch our bus.  When I got
    home I __________(verb, past tense)my  mom for a __________(adjective) day 
    at the zoo."""
    
def MadlibMenu(NN, ADJ, ADV, VB):
    print("Welcome to the Madlib Menu!  Please select Madlib " \
          "you want to fill out: \n" \
              "\t1 -- Monkey King\n" \
                  "\t2 -- My Trip to Disney World!\n" \
                      "\t3 -- The Great New Toy!\n" \
                          "\t4 -- Big Mac Who?\n" \
                              "\t5 -- Make me a Video Game!\n" \
                                  "\t6 -- In the Jungle!\n" \
                                      "\t7 -- The First Day of School\n" \
                                          "\t8 -- At the Arcade\n" \
                                              "\t9 -- The Fun Park!\n" \
                                                  "\t10 -- A Day at the Zoo!\n")
    
    choice = int(input("Input the numeric value for your choice: "))
    
    if (choice == 1): MonkeyKing(NN, ADJ, ADV, VB)
    elif(choice == 2): DisneyTrip(NN, ADJ, VB)
    elif(choice == 3): GreatToy(NN, ADJ, ADV, VB)
    elif(choice == 4): BigMacWho(NN, ADJ, ADV, VB)
    elif(choice == 5): VideoGame(NN, ADJ, ADV, VB)
    elif(choice == 6): Jungle(NN, ADJ, ADV, VB)
    elif(choice == 7): FirstDaySchool(NN, ADJ, ADV, VB)
    elif(choice == 8): Arcade(NN, ADJ, ADV, VB)
    elif(choice == 9): FunPark(NN, ADJ, ADV, VB)
    elif(choice == 10): Zoo(NN, ADJ, ADV, VB)
    else:
        print("ERROR: Invalid Input")
        MadlibMenu(NN, ADJ, ADV, VB)
