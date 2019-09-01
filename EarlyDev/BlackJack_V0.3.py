import random
import time
import sys
from os import system

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

def dealerBlackjack(dealerHand, playerHand):
    if dealerHand == 21:
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
                    game(bank, winnings, turns)

def decision(playerHand, dealerHand, bank, winnings, bet):
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            playerHand = playerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            playerBust(playerHand, bank, winnings, bet)
            playerSafe(dealerHand, playerHand)
            playerBlackjack(playerHand, bank, winnings, bet)
        elif option == "2":
            dealerHand = dealerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            time.sleep(1)
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))    
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has won! You have lost :(")
                            playerLost(bank, winnings, bet)
                            time.sleep(1)
                            again = input("\nTry Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                game(bank, winnings, turns)
                        elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            again = input("Try Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                game(bank, winnings, turns)
                    elif dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("\nDealer has won! You have lost :(")
                        bank -= bet
                        winnings -= bet
                        print("\nYour Bank: {}".format(bank))
                        print("Your Winnings: {}".format(winnings))
                        time.sleep(1)
                        again = input("\nTry Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            game(bank, winnings, turns)
                    elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            again = input("\nTry Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                game(bank, winnings, turns)
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has won! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        game(bank, winnings, turns)
                elif dealerHand > 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has busted! You have won :)")
                    bank += bet
                    winnings += bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        game(bank, winnings, turns)
                elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        game(bank, winnings, turns)
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                bank -= bet
                winnings -= bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game(bank, winnings, turns)
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has busted! You have won :)")
                bank += bet
                winnings += bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    game(bank, winnings, turns)
            elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("Try Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        game(bank, winnings, turns)
        elif option != "1" or "2":
            print("\nOnly Choose 1 or 2.")
            time.sleep(1.5)
            decision(playerHand, dealerHand, bank, winnings, bet)

def game(bank, winnings):
    system("cls")
    suits = ranks()
    global dealerHand
    global playerHand
    print("\nCurrent bank balance: {}".format(bank))
    print("Current Winnings: {}".format(winnings))
    dealerHand = int(random.choice(suits)) 
    playerHand = int(random.choice(suits)) + int(random.choice(suits))



    print("\nWelcome To Conors's Blackjack! Version 3.0")
    
    time.sleep(2)
    
    #Bet System
    bet = int(input("Bet amount: "))
    if bet > bank:
        print("\nBet amount more than what you have. Try again!")
        time.sleep(1)
        game(bank, winnings, turns)
    else:
        #Options Begin
        time.sleep(1)
        print("\nDealer Hand: {}".format(dealerHand))
        time.sleep(1)
        print("Player Hand: {}".format(playerHand))
        time.sleep(1)
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            playerHand = playerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            playerBust(playerHand, bank, winnings, bet)
            playerSafe(dealerHand, playerHand)
            playerBlackjack(playerHand, bank, winnings, bet)
        elif option == "2":
            dealerHand = dealerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            time.sleep(1)
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))    
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has won! You have lost :(")
                            playerLost(bank, winnings, bet)
                            time.sleep(1)
                            again = input("\nTry Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                game(bank, winnings, turns)
                        elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            again = input("Try Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                
                                game(bank, winnings, turns)
                    elif dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("\nDealer has won! You have lost :(")
                        bank -= bet
                        winnings -= bet
                        print("\nYour Bank: {}".format(bank))
                        print("Your Winnings: {}".format(winnings))
                        time.sleep(1)
                        again = input("\nTry Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            
                            game(bank, winnings, turns)
                    elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            again = input("\nTry Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                
                                game(bank, winnings, turns)
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has won! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        
                        game(bank, winnings, turns)
                elif dealerHand > 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has busted! You have won :)")
                    bank += bet
                    winnings += bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        
                        game(bank, winnings, turns)
                elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        
                        game(bank, winnings, turns)
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                bank -= bet
                winnings -= bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    
                    game(bank, winnings, turns)
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has busted! You have won :)")
                bank += bet
                winnings += bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    
                    game(bank, winnings, turns)
            elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("Try Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        
                        game(bank, winnings, turns)
        elif option != "1" or "2":
            print("\nOnly Choose 1 or 2.")
            time.sleep(1.5)
            decision(playerHand, dealerHand, bank, winnings, bet)




def playerBust(playerHand, bank, winnings, bet):
    if playerHand > 21:
            print("\nYou busted!")
            bank = bank - bet
            winnings = winnings - bet
            print("\nYour Bank: {}".format(bank))
            print("Your Winnings: {}".format(winnings))
            playAgain()


def playerSafe(dealerHand, playerHand):
    if playerHand < 21:
            decision(playerHand, dealerHand, bank, winnings, bet)


def playerBlackjack(playerHand, bank, winnings, bet):
    if playerHand == 21:
            print("Blackjack!")
            bank += bet + bet/2
            winnings += bet + bet/2
            print("\nYour Bank: {}".format(bank))
            print("Your Winnings: {}".format(winnings))
            again = input("\nTry Again? (1/2)?")
            if again.isdigit() == False:
                quit()
            elif int(again) != 1:
                quit()
            elif int(again) == 1:
                game(bank, winnings, turns) 

def playAgain():
    again = input("\Play Again? (1/2)?")
    if again.isdigit() == False:
        quit()
    elif int(again) != 1:
        quit()
    elif int(again) == 1:
        game(bank, winnings, turns)

if __name__ == "__main__":
    system("cls")
    suits = ranks()
    turns = 0
    turn = list(range(1,100))
    global dealerHand
    global playerHand
    bank = int(input("\nHow much $ do you have? "))
    winnings = 0
    dealerHand = int(random.choice(suits)) 
    playerHand = int(random.choice(suits)) + int(random.choice(suits))



    print("\nWelcome To Conors's Blackjack! Version 3.0")
    print(turns)
    print('\nRound {}'.format(turn[turns]))
    
    time.sleep(2)
    
    #Bet System
    bet = int(input("Bet amount: "))
    if bet > bank:
        print("\nBet amount more than what you have. Try again!")
        time.sleep(1)
        game(bank, winnings, turns)
    else:
        #Options Begin
        time.sleep(1)
        print("\nDealer Hand: {}".format(dealerHand))
        time.sleep(1)
        print("Player Hand: {}".format(playerHand))
        time.sleep(1)
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            playerHand = playerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            playerBust(playerHand, bank, winnings, bet)
            playerSafe(dealerHand, playerHand)
            playerBlackjack(playerHand, bank, winnings, bet)
        elif option == "2":
            dealerHand = dealerHand + int(random.choice(suits))
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            time.sleep(1)
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))    
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has won! You have lost :(")
                            playerLost(bank, winnings, bet)
                            time.sleep(1)
                            again = input("\nTry Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                game(bank, winnings, turns)
                        elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            again = input("Try Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                
                                game(bank, winnings, turns)
                    elif dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("\nDealer has won! You have lost :(")
                        bank -= bet
                        winnings -= bet
                        print("\nYour Bank: {}".format(bank))
                        print("Your Winnings: {}".format(winnings))
                        time.sleep(1)
                        again = input("\nTry Again? (1/2)?")
                        if again.isdigit() == False:
                            quit()
                        elif int(again) != 1:
                            quit()
                        elif int(again) == 1:
                            
                            game(bank, winnings, turns)
                    elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            again = input("\nTry Again? (1/2)?")
                            if again.isdigit() == False:
                                quit()
                            elif int(again) != 1:
                                quit()
                            elif int(again) == 1:
                                
                                game(bank, winnings, turns)
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has won! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        
                        game(bank, winnings, turns)
                elif dealerHand > 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has busted! You have won :)")
                    bank += bet
                    winnings += bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        
                        game(bank, winnings, turns)
                elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("\nTry Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        
                        game(bank, winnings, turns)
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                bank -= bet
                winnings -= bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    
                    game(bank, winnings, turns)
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has busted! You have won :)")
                bank += bet
                winnings += bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                again = input("Try Again? (1/2)?")
                if again.isdigit() == False:
                    quit()
                elif int(again) != 1:
                    quit()
                elif int(again) == 1:
                    
                    game(bank, winnings, turns)
            elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    again = input("Try Again? (1/2)?")
                    if again.isdigit() == False:
                        quit()
                    elif int(again) != 1:
                        quit()
                    elif int(again) == 1:
                        
                        game(bank, winnings, turns)
        elif option != "1" or "2":
            print("\nOnly Choose 1 or 2.")
            time.sleep(1.5)
            decision(playerHand, dealerHand, bank, winnings, bet)



    

    
    