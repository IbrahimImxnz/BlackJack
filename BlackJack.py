import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}
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


    def deposit(self,amount):
        self.balance += amount
        print("Money deposited") 

    def sum(self):
        sum = 0
        for i in self.cards:
            sum += i.value 
        return sum       

    def Ace(self):
         sum_of = 0
         for i in self.cards:
              sum_of += i.value
         if sum_of >= 21:
              for i in self.cards:
                   if i.rank == "Ace":
                        i.value = 1 
                                   

game_on = True
choices = True

balance = int(input("How much is your balance? "))
player = Player(balance)
dealer = Player(0)

while game_on: 
    deck = Deck()
    player.cards = []
    dealer.cards = []
    deck.shuffle()
    print(f"Your balance is now: {player.balance}")
    

    while True:
        try:
            bet = int(input("How much would you like to bet? "))
        except ValueError:
             print("Please the bet must be an integer")
        else:
            if bet > player.balance:
                  print("You are BROKE! please pick lower amount to bet on") 
            else: 
                 player.balance -= bet 
                 break       


    for i in range(2):
        player.hit(deck.deal_one())

    print(f"Player's 2 cards are: {player.cards[0]} and {player.cards[1]}")    

    dealer.hit(deck.deal_one())    
    
    print(f"Dealer's face up card is: {dealer.cards[0]}")
        
    if player.sum() == 21:
        dealer.hit(deck.deal_one())
        print(f"Dealer's face down card was: {dealer.cards[1]}")

        if dealer.sum() == 21:
            print("Push! You did not lose your bet, but you did not win the game!")
            player.deposit(bet)
        elif dealer.sum() != 21: 
            print("BLACKJACK! You get double your bet back!")
            player.deposit(bet*2)     
        while True:
                try:
                    choice = input("play again or quit? ")
                except:
            
                    if choice != "play again" or "quit":
                        print("Please pick play again or quit")
                        
                else:
                       if choice == "quit":
                            game_on = False
                            break
                       elif choice == "play again":
                            break
                    
    else:
        y = 0
        game_further = True
        while game_further:    
            choice = input("Would you like to hit, stay, double down, split or surrender? ")
            if choice == "double down":
                if player.balance >= bet:
                    print("Bet will be doubled!")
                    player.balance -= bet
                    player.hit(deck.deal_one())
                    player.Ace()
                    print(f"The card that you got was: {player.cards[y]}")
                    if player.sum() == 21:
                        print("BLACKJACK! Player wins double his bet back!")
                        player.deposit(bet*4)
                        while True:
                            try:
                                choicesec = input("play again or quit? ")
                            except:
                        
                                if choicesec != "play again" or "quit":
                                    print("Please pick play again or quit")
                                    
                            else:
                                if choicesec == "quit":
                                        game_further = False
                                        game_on = False
                                        break
                                elif choicesec == "play again":
                                        game_further = False
                                        break
                    if player.sum() > 21:
                        print("Bust! Player loses his bet")
                        while True:
                            try:
                                choicesec = input("play again or quit? ")
                            except:
                        
                                if choicesec != "play again" or "quit":
                                    print("Please pick play again or quit")
                                    
                            else:
                                if choicesec == "quit":
                                        game_further = False
                                        game_on = False
                                        break
                                elif choicesec == "play again":
                                        game_further = False
                                        break
                    elif player.sum() < 21:
                        dealer.hit(deck.deal_one()) 
                        print(f"Dealer's face down card was: {dealer.cards[1]}")
                        x = 1
                        while True:
                            if dealer.sum() < 17:
                                dealer.hit(deck.deal_one())
                                dealer.Ace()
                                x += 1
                                print(f"Dealer got this card: {dealer.cards[x]}")
                                continue    
                            else:
                                break
                        if dealer.sum() > 21:
                            print("Dealer busted! Player gets double bet back")
                            player.deposit(bet*4)
                        elif player.sum() > dealer.sum():
                            print("Player wins double his bet back!")
                            player.deposit(bet*4)
                        else:
                            print("Dealer Wins! Players loses his bet")  
                        while True:
                            try:
                                choicesec = input("play again or quit? ")
                            except:
                        
                                if choicesec != "play again" or "quit":
                                    print("Please pick play again or quit")
                                    
                            else:
                                if choicesec == "quit":
                                        game_further = False
                                        game_on = False
                                        break
                                elif choicesec == "play again":
                                        game_further = False
                                        break
                 
                else:
                    print("You do not have enough money to double down!")
                    continue
            elif choice == "split":
                 if player.cards[0].value == player.cards[1].value:
                      pass 
            elif choice == "surrender":
                print("You surrendered and half your bet will return to your balance you COWARD")
                player.deposit(bet*0.5)
                while True:
                        try:
                            choicesec = input("play again or quit? ")
                        except:
                    
                            if choicesec != "play again" or "quit":
                                print("Please pick play again or quit")
                                
                        else:
                            if choicesec == "quit":
                                    game_further = False
                                    game_on = False
                                    break
                            elif choicesec == "play again":
                                    game_further = False
                                    break

            elif choice == "hit": 
                y += 1
                player.hit(deck.deal_one())
                player.Ace()
                print(f"The card that you got was: {player.cards[y]}")
                if player.sum() == 21:
                    print("BLACKJACK! Player wins double his bet back!")
                    player.deposit(bet*2)
                    while True:
                        try:
                            choicesec = input("play again or quit? ")
                        except:
                    
                            if choicesec != "play again" or "quit":
                                print("Please pick play again or quit")
                                
                        else:
                            if choicesec == "quit":
                                    game_further = False
                                    game_on = False
                                    break
                            elif choicesec == "play again":
                                    game_further = False
                                    break
                
                if player.sum() > 21:
                    print("Bust! Player loses his bet")
                    while True:
                        try:
                                choicesec = input("play again or quit? ")
                        except:
                        
                                if choicesec != "play again" or "quit":
                                    print("Please pick play again or quit")
                                    
                        else:
                                if choicesec == "quit":
                                        game_further = False
                                        game_on = False
                                        break
                                elif choicesec == "play again":
                                        game_further = False
                                        break
                elif player.sum() < 21:
                    dealer.hit(deck.deal_one()) 
                
                    print(f"Dealer's face down card was: {dealer.cards[1]}")

                    x = 1
                    
                    while True:
                        if dealer.sum() < 17:
                            dealer.hit(deck.deal_one())
                            dealer.Ace()
                            x += 1
                            print(f"Dealer got this card: {dealer.cards[x]}")
                            continue    
                        else:
                            break
                            

                    if dealer.sum() > 21:
                        print("Dealer busted! Player gets double bet back")
                        player.deposit(bet*2)
                        while True: 
                            try:
                                choicesec = input("play again or quit? ")
                            except:
                        
                                if choicesec != "play again" or "quit":
                                    print("Please pick play again or quit")
                                    
                            else:
                                if choicesec == "quit":
                                        game_further = False
                                        game_on = False
                                        break
                                elif choicesec == "play again":
                                        game_further = False
                                        break
            elif choice == "stay":
                index = 2
                if index > len(dealer.cards):
                    dealer.hit(deck.deal_one()) 
                    print(f"Dealer's face down card was: {dealer.cards[1]}")

                x = 1

                while True:
                        if dealer.sum() < 17:
                            dealer.hit(deck.deal_one())
                            dealer.Ace()
                            x += 1
                            print(f"Dealer got this card: {dealer.cards[x]}")
                            continue    
                        else:
                            break

               

                if dealer.sum() > 21:
                        print("Dealer busted! Player gets double bet back")
                        player.deposit(bet*2)
                elif player.sum() > dealer.sum():
                        print("Player wins double his bet back!")
                        player.deposit(bet*2)
                else:
                        print("Dealer Wins! Players loses his bet")  
                while True:
                            try:
                                choicesec = input("play again or quit? ")
                            except:
                        
                                if choicesec != "play again" or "quit":
                                    print("Please pick play again or quit")
                                    
                            else:
                                if choicesec == "quit":
                                        game_further = False
                                        game_on = False
                                        break
                                elif choicesec == "play again":
                                        game_further = False
                                        break
            else:
                print("Please pick one of the options!")        
                                  
                

            





