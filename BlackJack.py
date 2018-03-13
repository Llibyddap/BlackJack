'''
Created on Nov 7, 2017

@author: bill
'''
import random

player = ''
house = ''

class Player(object):
    
    def __init__(self):
        self.hand = {}

    def name(self, name):
        self.name = name
                
    def bankroll(self, bankroll):
        self.bankroll = bankroll
        
    def add_money(self, add_money):
        self.bankroll += add_money
    
    def del_money(self, del_money):
        if self.bankroll - del_money < 0:
            print("You do not have enough money...")
        else:
            self.bankroll -= del_money
        
class House(object):
    
    name = "House"
    bankroll = 10000
    
    def __init__(self):
        self.hand = {}
        
    def add_money(self, add_money):
        self.bankroll += add_money
    
    def del_money(self, del_money):
        if self.bankroll - del_money < 0:
            print("The House cannot cover the bet...")
        else:
            self.bankroll -= del_money
    
    def hand(self, key1, val1, key2, val2):
        self.hand += {key1:val1, key2: val2}
        
class Deck(object):
    
    def __init__(self):
        self.cards = {'AH': (1,11), '2H':2, '3H':3, '4H':4, '5H':5, '6H':6, '7H':7, '8H':8, '9H':9, '10H':10, 'JH':10, 'QH':10, 'KH':10,
                     'AS': (1,11), '2S':2, '3S':3, '4S':4, '5S':5, '6S':6, '7S':7, '8S':8, '9S':9, '10S':10, 'JS':10, 'QS':10, 'KS':10,
                     'AD': (1,11), '2D':2, '3D':3, '4D':4, '5D':5, '6D':6, '7D':7, '8D':8, '9D':9, '10D':10, 'JD':10, 'QD':10, 'KD':10,
                     'AC': (1,11), '2C':2, '3C':3, '4C':4, '5C':5, '6C':6, '7C':7, '8C':8, '9C':9, '10C':10, 'JC':10, 'QC':10, 'KC':10,}
        
    def del_card(self,card):
        del self.cards[card]
    
def add_Player():   
    global player 
    while True:
        try:
            new_name = input("Please enter your name: ")
            new_bankroll = int(input("What is your starting cash balance: "))
            player = Player()
            player.name(new_name)
            player.bankroll(new_bankroll)
        except:
            print("Ooops... something went wrong")
        else:
            break
    
def add_House():
    global house
    house = House()    
    
def deal():
    i = 0
    while i != 2:  
        key, val = random.choice(list(deck.cards.items()))
        deck.cards.pop(key)
        player.hand[key]=val
        print(key, val)
        key, val = random.choice(list(deck.cards.items()))
        deck.cards.pop(key)
        house.hand[key]=val
        print(key, val)
        i += 1
    return()


def check_for_winner():
    # House check
    houseScore = 0
    for key, val in house.hand.items():
        if type(val) == tuple:
            print("There is an Ace: ", val)
        else:
            print("Just a card: ", val)
            houseScore += val
    print("House Score = ", str(houseScore))
    if houseScore > 21:
        game_over(player.name, "Busted")
    elif houseScore == 21:
        game_over(player.name, "Winner")

    #
    # Player check
    playerScore = 0
    for key, val in player.hand.items():
        if type(val) == tuple:
            print("There is an Ace: ", val)
        else:
            print("Just a card: ", val)
            playerScore += val
    print("Player Score = ", str(playerScore))
    if playerScore > 21:
        game_over(player.name, "Busted")
        return False
    elif playerScore == 21:
        game_over(player.name, "WON with 21!!!")
        return False

def game_over(player, status):
    print(player, " has ", status)
    return False
        
add_House()
add_Player()
print("Shuffling the deck...")
deck = Deck()        
print("Dealing...")
deal()
check_for_winner()
while True:
    print("Here is the House current had:")
    for key, val in house.hand.items():
        print(key, val)
    print("Here is your current hand:")
    for key, val in player.hand.items():
        print(key, val)
    turn = input("would you like a card: ")
    if turn == 'yes':
        key, val = random.choice(list(deck.cards.items()))
        deck.cards.pop(key)
        print(key, val)
        player.hand[key] = val
        if check_for_winner() == False:
            break
    else:
        pass



print(player.name)        
print(player.bankroll)

print("")

for key, val in player.hand.items():
    print(key, val)

print("")

for key, val in house.hand.items():
    print(key, val)



'''
deck = Deck()
for key, val in deck.cards.items():
    print(key, val)

print(" break ")

key, val = random.choice(list(deck.cards.items()))

print(key, val)

print (" break ")

deck.del_card('AH')
    
for key, val in deck.cards.items():
    print(key, val)
'''