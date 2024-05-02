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
choices = True

while game_on: 
    deck = Deck()
    deck.shuffle()
    balance = int(input("How much is your balance?"))
    player = Player(balance)
    dealer = Player(0)

    bet = int(input("How much would you like to bet?"))

    betting_amount = player.withdraw(bet)

    for i in range(2):
        player.hit(deck.deal_one())

    print(f"Player's 2 cards are: {player.cards[0]} and {player.cards[1]}")    

    dealer.hit(deck.deal_one())    
    
    print(f"Dealer's face up card is: {dealer.cards[0]}")
        
    if player.cards[0].value + player.cards[1].value == 21:
        dealer.hit(deck.deal_one())
        print(f"Dealer's face down card was: {dealer.cards[1]}")

        if dealer.cards[0].value + dealer.cards[1].value == 21:
            print("Push! You did not lose your bet, but you did not win the game!")
            player.deposit(betting_amount)
        elif dealer.cards[0].value + dealer.cards[1].value != 21: 
            print("BLACKJACK! You get double your bet back!")
            player.deposit(betting_amount*2)     
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
    elif player.cards[0].value + player.cards[1].value != 21:
        play = True
        while play:
            choice = input("Would you like to hit or stay")
            if choice == "hit":
                player.hit(deck.deal_one())
                print(f"The card that you got was: {player.cards[2]}")
                if player.cards[0].value + player.cards[1].value + player.cards[2].value == 21:
                    print("BLACKJACK! Player wins double his bet back!")
                    player.deposit(betting_amount*2)
                
                if player.cards[0].value + player.cards[1].value + player.cards[2].value > 21:
                    print("Bust! Player loses his bet")
                elif player.cards[0].value + player.cards[1].value + player.cards[2].value < 21:
                    dealer.hit(deck.deal_one()) 
                
                    print(f"Dealer's face down card was: {dealer.cards[1]}")

                    sum = 0
                    for i in dealer.cards:
                        sum += dealer.cards[i].value

                    if sum < 17:    
                        while sum < 17:
                            dealer.hit(deck.deal_one())
                            for i in dealer.cards:
                                sum += dealer.cards[i].value

                            for i in dealer.cards:
                                print(f"Dealer's pulled card is: {dealer.cards[i]}")

                    if sum > 21:
                        print("Dealer busted! Player gets double bet back")
                        player.deposit(betting_amount*2)
                    elif player.cards[0].value + player.cards[1].value + player.cards[2].value > sum:
                        print("Player wins double his bet back!")
                        player.deposit(betting_amount*2)
                    else:
                        print("Dealer Wins! Players loses his bet")    

            elif choice == "stay":
                dealer.hit(deck.deal_one()) 
                print(f"Dealer's face down card was: {dealer.cards[1]}")
                sum = 0
                for i in dealer.cards:
                    sum += dealer.cards[i].value

                if sum < 17:    
                        while sum < 17:
                            dealer.hit(deck.deal_one())
                            for i in dealer.cards:
                                sum += dealer.cards[i].value

                            for i in dealer.cards:
                                print(f"Dealer's pulled card is: {dealer.cards[i]}")
                if sum > 21:
                        print("Dealer busted! Player gets double bet back")
                        player.deposit(betting_amount*2)
                elif player.cards[0].value + player.cards[1].value > sum:
                        print("Player wins double his bet back!")
                        player.deposit(betting_amount*2)
                else:
                        print("Dealer Wins! Players loses his bet")  
            else:
                 print("Please pick hit or stay")            
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
                

            





