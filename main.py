import random

# for card generation
suits = ['hearts', 'diamonds', 'spades', 'clubs']
values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

#define player class
class Player:

    def __init__(self, name, money):
        self.name = name
        self.money = int(money)
        self.hand =  []

class Dealer:

    def __init__(self):
        self.hand = []


#card class
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.title = value
        self.value = 0

    def __repr__(self):
        return f'{self.title} of {self.suit}'

    def return_value(self):
        if type(self.title) == int:
            self.value = self.title
        elif self.title == 'jack' or self.title == 'queen' or self.title == 'king':
            self.value = 10
        elif self.title == 'ace':
            self.value = 1
        return self.value

dealer = Dealer()

def create_deck():
    deck = [Card(suit, value) for suit in suits for value in values]
    return deck


#player = Player(input("What is your name? "), input("How much money will you be playing with? "))
player = Player('ian', 100)
ace = Card('Clear', 'ace')
player.hand.append(ace)
def play_round():

    current_deck = create_deck()

    #function to get the current bet and check if its valid
    def get_current_bet():
        current_bet = 0
        valid_bet = False
        while not valid_bet:
            current_bet = int(input('How much do you want to bet this round? '))
            if player.money - current_bet >= 0:
                player.money = player.money - current_bet
                valid_bet = True
            else:
                print('Sorry that is an invalid amount.')
        return current_bet
    current_bet = get_current_bet()


    #will deal the cards to the instanced hands.
    def deal():

        player.hand.append(current_deck.pop(random.randint(0, len(current_deck))))
        dealer.hand.append(current_deck.pop(random.randint(0, len(current_deck))))
        player.hand.append(current_deck.pop(random.randint(0, len(current_deck))))
        dealer.hand.append(current_deck.pop(random.randint(0, len(current_deck))))

    def sum_hand(hand):
        total = 0
        has_ace = False
        for card in hand:
            if card.title == 'ace':
                has_ace = True
            total += card.return_value()
        if has_ace == True:
            if total <= 21 and total + 10  <= 21:
                total += 10
        return total




    deal()
    print(f'You currently have the {player.hand[0]} and the {player.hand[1]} {player.hand[2]} for a total of {sum_hand(player.hand)}')
    print(f'The dealer is currently showing the {dealer.hand[1]}')

play_round()
