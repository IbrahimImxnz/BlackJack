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

class Split(Player):
    def __init__(self,cards):
         self.cards = cards

    def __str__(self):
        for i in self.cards:
            return i   
                                           
def hit(object,object2,object3,object4,object5):
    object5 += 1
    object.hit(object3.deal_one())
    object.Ace()
    print(f"The card that you got was: {object.cards[object5]}")
    if object.sum() == 21:
        print("BLACKJACK! Player wins double his bet back!")
        object.deposit(object4*2)
        return True
    
    if object.sum() > 21:
        print("Bust! Player loses his bet")
        return True
    elif object.sum() < 21:
        object2.hit(object3.deal_one()) 
    
        print(f"Dealer's face down card was: {object2.cards[1]}")

        x = 1
        
        while True:
            if object2.sum() < 17:
                object2.hit(object3.deal_one())
                object2.Ace()
                x += 1
                print(f"Dealer got this card: {object2.cards[x]}")
                continue    
            else:
                break
                

        if object2.sum() > 21:
            print("Dealer busted! Player gets double bet back")
            object.deposit(object4*2)
            return True

def stay(object1,object2,object3,object4):
    index = 2
    if index > len(object2.cards):
        object2.hit(object3.deal_one()) 
        print(f"Dealer's face down card was: {object2.cards[1]}")

    x = 1

    while True:
            if object2.sum() < 17:
                object2.hit(object3.deal_one())
                object2.Ace()
                x += 1
                print(f"Dealer got this card: {object2.cards[x]}")
                continue    
            else:
                break
    print(object1.sum())
    print(object2.sum())        

    

    if object2.sum() > 21:
            print("Dealer busted! Player gets double bet back")
            object1.deposit(object4*2)
            return True
    elif object1.sum() > object2.sum():
            print("Player wins double his bet back!")
            object1.deposit(object4*2)
            return True
    else:
            print("Dealer Wins! Players loses his bet")
            return True  

def double_down(object1,object2,object3,object4,object5):
    if object1.balance >= object3:
        print("Bet will be doubled!")
        object1.balance -= object3
        object1.hit(object2.deal_one())
        object1.Ace()
        print(f"The card that you got was: {object1.cards[object4]}")
        if object1.sum() == 21:
            print("BLACKJACK! Player wins double his bet back!")
            object1.deposit(object3*4)
            return True
        if object1.sum() > 21:
            print("Bust! Player loses his bet")
            return True
        elif object1.sum() < 21:
            object5.hit(object2.deal_one()) 
            print(f"Dealer's face down card was: {object5.cards[1]}")
            x = 1
            while True:
                if object5.sum() < 17:
                    object5.hit(object2.deal_one())
                    object5.Ace()
                    x += 1
                    print(f"Dealer got this card: {object5.cards[x]}")
                    continue    
                else:
                    break
            if object5.sum() > 21:
                print("Dealer busted! Player gets double bet back")
                object1.deposit(object3*4)
                return True
            elif object1.sum() > object5.sum():
                print("Player wins double his bet back!")
                object1.deposit(object3*4)
                return True
            else:
                print("Dealer Wins! Players loses his bet")
                return True  
    else:
        print("You do not have enough money to double down!")
         
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
        y = 1
        game_further = True
        while game_further:    
            choice = input("Would you like to hit, stay, double down, split or surrender? ")
            if choice == "double down":
                if double_down(player,deck,bet,y,dealer):
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

            elif choice == "split":
                 if player.cards[0].value == player.cards[1].value:
                      print("You will have two separate hands now! and a new bet with same amount will be placed")
                      if player.balance >= bet:
                           player.balance -= bet
                           player.hit(deck.deal_one())
                           player.hit(deck.deal_one())
                           split1 = Split(player.balance,[player.card[0],player.card[2]]) 
                           split2 = Split(player.balance,[player.card[1],player.card[3]])
                           print(f"Player's first hand consists of: {split1}")
                           print(f"Player's second hand consists of: {split2}")
                           if split1.sum() == 21:
                                print("BLACKJACK! you get double your bet back!")
                                player.deposit(bet*2)
                          # else:
                                choicex = input("Would you like to hit, stay, double down or surrender?")
                              #  while True:
                             #       if choicex == "hit":
                                         
                                              
                          # if split2.sum() == 21:
                           #     print("BLACKJACK! you get double your bet back!")
                            #    player.deposit(bet*2)     
                                
            elif choice == "surrender":
                print("You surrendered and half your bet will return to your balance you COWARD")
                player.deposit(bet*1/2)
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
                if hit(player,dealer,deck,bet,y):
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
                if stay(player,dealer,deck,bet):  
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
                                  
                

            





