#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:13:05 2021

@author: Yxzhang
"""

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    # Overriding
    # Less than
    def __lt__(self, card):
        return self.rank < card.rank
    
    # Less than or equal to
    def __lte__(self, card):
        return self.rank <= card.rank
    
    # Greater than
    def __gt__(self, card):
        return self.rank > card.rank
    
    # Greater than or equal to
    def __gte__(self, card):
        return self.rank >= card.rank
    
    # Equal to
    def __eq__(self, card):
        return self.rank == card.rank
    
    # Not equal to
    def __neq__(self, card):
        return self.rank != card.rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
        
suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
deck = []

# Nested for-loop
for suit in suits:
    for rank in range(2, 11):
        deck.append(Card(suit, rank))


random.shuffle(deck)
    

# WAR
# player1 = deck[:int(len(deck) / 2)]
# player2 = deck[int(len(deck) / 2):]

player1 = [Card('Clubs', 4), Card('Diamonds', 3), Card('Hearts', 8), Card('Hearts', 10), Card('Clubs', 7)]
player2 = [Card('Hearts', 4), Card('Diamonds', 4), Card('Hearts', 5), Card('Hearts', 6), Card('Clubs', 2)]

def print_deck(deck):
    for card in deck:
        print(card)

def play_turn():
    print(f'{player1[0]}, {player2[0]}')
    print(len(player1))
    print(len(player2))
    
    if player1[0] > player2[0]:
        print(f'{player1[0]} > {player2[0]}')
        player1.append(player2[0])
        player2.remove(player2[0])
        
    elif player1[0] < player2[0]:
        print(f'{player1[0]} < {player2[0]}')
        player2.append(player1[0])
        player1.remove(player1[0])
    
    elif player1[0] == player2[0]:
        play_war()
        
    print("#### Player1 ####")
    print_deck(player1)
    print("\n\n#### Player2 ####")
    print_deck(player2)

def play_war():
    war_card = 0
    print('Its WAR!')
    while player1[war_card] == player2[war_card]:
        if player1[war_card + 4] > player2[war_card + 4]:
            for card in player2[0:war_card + 4]:
                player1.append(card)
                player2.remove(card)
                
        elif player1[war_card + 4] < player2[war_card + 4]:
            for card in player1[0:war_card + 4]:
                player2.append(card)
                player1.remove(card)
                
        else:
            war_card += 4

print("#### Player1 ####")
print_deck(player1)
print("\n\n#### Player2 ####")
print_deck(player2)
while len(player1) > 0 and len(player2) > 0:
    play_turn()
    input()