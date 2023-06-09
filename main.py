import random
import time

# for card generation
suits = ['hearts', 'diamonds', 'spades', 'clubs']
values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

#define player class
class Player:

    def __init__(self, name, money):
        self.name = name
        self.money = int(money)
        self.hand =  []
        self.play_state = True
        self.current_bet = 0

class Dealer:

    def __init__(self):
        self.hand = []
        self.name = 'The Dealer'

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
def play_round():
    player.current_bet = 0

    current_deck = []
    current_deck = create_deck()
    time.sleep(2)
    player.hand = []
    dealer.hand = []
    #function to get the current bet and check if its valid
    def get_current_bet():
        valid_bet = False
        while not valid_bet:
            current_bet = int(input(f' You currently have {player.money} dollars. How much do you want to bet this round? '))
            time.sleep(1)
            if player.money - current_bet >= 0:
                valid_bet = True
            else:
                print('Sorry that is an invalid amount.')
        return current_bet
    
    player.current_bet = get_current_bet()

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

    #Does player want to hit or stay or double down


    def hit(hand):
        hand.hand.append(current_deck.pop(random.randint(0, len(current_deck))))
        print(f'{hand.name} was dealt a {hand.hand[-1]} for a hand total of {sum_hand(hand.hand)}')

    #this is the player move set
    def move_set():
        turn_over = False
        decision = input("Do you want to hit stand or double down? ")

        time.sleep(1)
            #loop to check players move. Lots of comparatives to see if hand ever enters bust state.
        if decision.lower() == 'hit':
            hit(player)
            if sum_hand(player.hand) > 21:
                turn_over = True
            elif sum_hand(player.hand) < 21:
                while not turn_over:
                    question = input('Would you like to hit or stand? ')
                    time.sleep(1)
                    if question.lower() == 'hit': 
                        hit(player)
                        if sum_hand(player.hand) > 21:
                            print(f'You were dealt a {player.hand[-1]}')
                            turn_over = True
                else:
                    turn_over = True
        elif decision.lower() == 'double down':
            hit(player)
            player.current_bet = player.current_bet * 2
        
        else:
            return

    def dealer_move():
        print(f'The dealer reveals their cards showing a {dealer.hand[0]} and a {dealer.hand[1]} for a total of {sum_hand(dealer.hand)}')
        time.sleep(1)
        while sum_hand(dealer.hand) <= 16 and sum_hand(player.hand) < 21:
            print(f'The dealer has 16 or less so the they hit.')
            hit(dealer)
            time.sleep(1)

        #compare hands
    def hand_compare(phand, dhand):
        if sum_hand(phand) >= sum_hand(dhand) and sum_hand(phand) <= 21:
            player.money += player.current_bet * 2
            return 'You have won this round'
        elif sum_hand(phand) < sum_hand(dhand) and sum_hand(dhand) <= 21:
            player.money -= player.current_bet
            return 'You have lost'
        elif sum_hand(dhand) > 21 :
            player.money += player.current_bet
            return 'The dealer has busted. You win this round.'
        else:
            player.money -= player.current_bet
            return 'Bust! you have lost this round'
    
    
    deal()
    print(f'You currently have the {player.hand[0]} and the {player.hand[1]} for a total of {sum_hand(player.hand)}')
    print(f'The dealer is currently showing the {dealer.hand[1]}')

 
    move_set()
    dealer_move()
    time.sleep(2)
  
    print(hand_compare(player.hand, dealer.hand) + f' you had a total of {sum_hand(player.hand)} while the dealer had {sum_hand(dealer.hand)} you now have {player.money} dollars left.')

def game():
    10
    while player.play_state == True:
        play_round()
        if player.money <= 0:
            print('You are out of money. Come back with more money to play again.')
            player.play_state = False
        play_again = input('Would you like to play another round? ')
        if play_again.lower() == 'no':
            player.play_state = False

game()