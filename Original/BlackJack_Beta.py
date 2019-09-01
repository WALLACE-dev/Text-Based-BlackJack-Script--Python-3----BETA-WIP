import random
import time
import sys

class Card:

    def __init__( self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__( self ):
        return self.rank + " of " + self.suit


class Deck:

    def __init__( self ):
        self.contents = []
        self.contents = [Card(rank, suit) for rank in ranks() for suit in suits() ]
        random.shuffle(self.contents)

def ranks():
    ranks = [ "1", "2", "3", "4", "5", "6", "7","8", "9", "10", "10", "10", "10" ]
    return ranks

def suits():
    suits = [ "Clubs", "Diamonds", "Hearts", "Spades" ]
    return suits

def randy():
    randy = random

def decision(playerHand, dealerHand):
    option = input("\n(1) Hit \n(2) Stand\nChoice: ")
    if option == "1":
        playerHand = playerHand + int(random.choice(suits))
        print("\nDealer: {}".format(dealerHand))
        print("Player: {}".format(playerHand))
        if playerHand > 21:
            print("You busted!")
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
        elif playerHand < 21:
            decision(playerHand, dealerHand)
        elif playerHand == 21:
            print("Blackjack!")
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
    elif option == "2":
        dealerHand = dealerHand + int(random.choice(suits))
        print("\nDealer: {}".format(dealerHand))
        print("Player: {}".format(playerHand))
        time.sleep(1)
        if dealerHand < 21 and dealerHand < playerHand:
            dealerHand = dealerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    if dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("Dealer has won! You have lost :(")
                        time.sleep(1)
                        again = input("Try Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            game()
                    elif dealerHand > 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("Dealer has lost! You have won :)")
                        time.sleep(1)
                        again = input("Try Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            game()
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has won! You have lost :(")
                    time.sleep(1)
                    again = input("Try Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        game()
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has lost! You have won :)")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
            elif dealerHand == 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
        elif dealerHand > playerHand and dealerHand < 21:
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            print("Dealer has won! You have lost :(")
            time.sleep(1)
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
        elif dealerHand > 21:
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            print("Dealer has busted! You have won :)")
            time.sleep(1)
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
    elif option != "1" or "2":
        print("\nOnly Choose 1 or 2.")
        time.sleep(1.5)
        decision(playerHand, dealerHand)
    

def game():
    suits = ranks()
    turn = 0
    global dealerHand
    global playerHand
    dealerHand = int(random.choice(suits)) 
    playerHand = int(random.choice(suits)) + int(random.choice(suits))


    print("\nWelcome To Conors's Blackjack! Version 1.0")
    print('\nRound {}'.format(turn))
    print("\nDealer Hand: {}".format(dealerHand))
    print("Player Hand: {}".format(playerHand))
    
    time.sleep(1)
    
    option = input("\n(1) Hit \n(2) Stand\nChoice: ")
    if option == "1":
        playerHand = playerHand + int(random.choice(suits))
        print("\nDealer: {}".format(dealerHand))
        print("Player: {}".format(playerHand))
        if playerHand > 21:
            print("You busted!")
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
        elif playerHand < 21:
            decision(playerHand, dealerHand)
        elif playerHand == 21:
            print("Blackjack!")
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
    elif option == "2":
        dealerHand = dealerHand + int(random.choice(suits))
        print("\nDealer: {}".format(dealerHand))
        print("Player: {}".format(playerHand))
        time.sleep(1)
        if dealerHand < 21 and dealerHand < playerHand:
            dealerHand = dealerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    if dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("Dealer has won! You have lost :(")
                        time.sleep(1)
                        again = input("Try Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            game()
                    elif dealerHand > 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("Dealer has lost! You have won :)")
                        time.sleep(1)
                        again = input("Try Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            game()
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has won! You have lost :(")
                    time.sleep(1)
                    again = input("Try Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        game()
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has lost! You have won :)")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
            elif dealerHand == 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
        elif dealerHand > playerHand and dealerHand < 21:
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            print("Dealer has won! You have lost :(")
            time.sleep(1)
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
        elif dealerHand > 21:
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            print("Dealer has busted! You have won :)")
            time.sleep(1)
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
    elif option != "1" or "2":
        print("\nOnly Choose 1 or 2.")
        time.sleep(1.5)
        decision(playerHand, dealerHand)


if __name__ == "__main__":
    suits = ranks()
    turn = 0
    global dealerHand
    global playerHand
    dealerHand = int(random.choice(suits)) 
    playerHand = int(random.choice(suits)) + int(random.choice(suits))


    print("\nWelcome To Conors's Blackjack! Version 1.0")
    print('\nRound {}'.format(turn))
    print("\nDealer Hand: {}".format(dealerHand))
    print("Player Hand: {}".format(playerHand))
    
    time.sleep(1)
    
    option = input("\n(1) Hit \n(2) Stand\nChoice: ")
    if option == "1":
        playerHand = playerHand + int(random.choice(suits))
        print("\nDealer: {}".format(dealerHand))
        print("Player: {}".format(playerHand))
        if playerHand > 21:
            print("You busted!")  
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
        elif playerHand < 21:
            decision(playerHand, dealerHand)
        elif playerHand == 21:
            print("Blackjack!")
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
    elif option == "2":
        dealerHand = dealerHand + int(random.choice(suits))
        print("\nDealer: {}".format(dealerHand))
        print("Player: {}".format(playerHand))
        time.sleep(1)
        if dealerHand < 21 and dealerHand < playerHand:
            dealerHand = dealerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    if dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("Dealer has won! You have lost :(")
                        time.sleep(1)
                        again = input("Try Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            game()
                    elif dealerHand > 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("Dealer has busted! You have won :)")
                        time.sleep(1)
                        again = input("Try Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            game()
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has won! You have lost :(")
                    time.sleep(1)
                    again = input("Try Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        game()
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has busted! You have won :)")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
            elif dealerHand == 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has blackjack! You have lost :(")
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game()
        elif dealerHand > playerHand and dealerHand < 21:
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            print("Dealer has won! You have lost :(")
            time.sleep(1)
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
        elif dealerHand > 21:
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            print("Dealer has busted! You have won :)")
            time.sleep(1)
            again = input("Try Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game()
    elif option != "1" or "2":
        print("\nOnly Choose 1 or 2.")
        time.sleep(1.5)
        decision(playerHand, dealerHand)



    

    
    