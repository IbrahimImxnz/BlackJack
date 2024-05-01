import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':[1,11]}
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

    def __init__(self, balance):
        self.balance = balance
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

game_on = True

while game_on: 
    deck = Deck()
    balance = int(input("How much is your balance?"))
    player = Player(balance)
    dealer = Player(0)

    bet = int(input("How much would you like to bet?"))

    betting_amount = player.withdraw(bet)

    for i in range(2):
        player.hit(deck.deal_one())
        dealer.hit(deck.deal_one())
        
    if player.cards[0] + player.cards[1] == 21 and dealer.cards[0] + dealer.cards[1] == 21:
        print("Push! You did not lose your bet, but you did not win the game!")
        player.deposit(betting_amount)
        choices = True
        while choices:
            choice = input("play again or quit?")
            if choice == "play again":
                choices = False
                continue
            elif choice == "quit":
                choices = False
                game_on = False
                break
            else:
                print("please type either play again or quit")




