#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:12:16 2021

@author: Yxzhang
"""

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        # HINT: You may need to add some new variables here to keep track of ACES...hmmmmmm

    
    def add_card(self, card):
        if card.rank == 'A':
            self.aces += 1
        self.cards.append(card)
        self.value += card.get_value()
        if self.value > 21 and self.aces >= 1:
            self.value -= 10
            self.aces -= 1
        # You will need to figure out how to figure out if there are any ACES that can be converted to a 1 instead of an 11 (this will be challenging!)

    def get_cards_str(self):
        s = '['
        for i, card in enumerate(self.cards):
            s += str(card)
            if i < len(self.cards) - 1:
                s += ', '
        s += ']'
        return s

