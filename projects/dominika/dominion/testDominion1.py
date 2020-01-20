# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:17 2020

@author: Antonio Dominikovic
"""


import Dominion
import testUtility
import random
from collections import defaultdict



#Get player names
player_names = testUtility.get_player_names()

#number of curses and victory cards
nV = testUtility.get_victory_cards(player_names)
nC = testUtility.get_curse_cards(player_names)

#Define box
box = testUtility.get_box(nV)

supply_order = testUtility.get_supply_order()

#Pick 10 cards from box to be in the supply.
boxlist = testUtility.get_random_box(box)
supply = testUtility.get_supply(box, boxlist)

#The supply always has these cards
testUtility.get_supply_quantity(supply, player_names, nV, nC)

#initialize the trash
trash = testUtility.get_trash()

#Costruct the Player objects
players = testUtility.get_players1(player_names)

#Play the game
testUtility.play_game(supply, supply_order, players, trash)

#Final score
testUtility.get_score(players)