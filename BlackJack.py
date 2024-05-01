import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11, "Acee":1}
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

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.cards = []

    def hit(self,card):
        self.cards.append(card)

    def Stay(self):
        pass

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal accepted")
        else:
            return False

    def deposit(self,amount):
        self.balance += amount
        print("Money deposited")        


      


