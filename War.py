import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
    

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.all_cards.append(card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()                

class Player:

    def __init__(self,name):

        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)    

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()

for item in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

counter = 0

while game_on:
    counter += 1
    print(f"Round {counter}")

    if len(player_one.all_cards) == 0:
        print("Player Two Wins!")
        game_on = False
        break

    
    if len(player_two.all_cards) == 0:
        print("Player One Wins!")
        game_on = False
        break

    player_one_cards = []
    player_two_cards = []

    player_one_cards.append(player_one.remove_card())
    player_two_cards.append(player_two.remove_card())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False   
        else:
            print("WAR!")
            if len(player_one.all_cards) < 3:
                print("Player one unable to declare war")
                print("Player two WINS!")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("Player two unable to declare war") 
                print("Player one WINS!")
                game_on = False
                break  
            else:
                for item in range(3):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card()) 


                     


