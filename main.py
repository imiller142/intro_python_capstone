import random

# for card generation
suits = ['hearts', 'diamonds', 'spades', 'clubs']
values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

#define player class
class Player:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand =  []


#card class
class Card:



    def __init__(self, suit, value):
        self.suit = suit
        self.title = value

    def __repr__(self):
        return f'{self.title} of {self.suit}'
    
    def return_value(self):
        pass


def create_deck():
    global deck
    deck = [Card(suit, value) for suit in suits for value in values]

def check_value(card):
    if type(card.title) == int:
        return 

create_deck()
for card in deck:
    print(check_value(card))