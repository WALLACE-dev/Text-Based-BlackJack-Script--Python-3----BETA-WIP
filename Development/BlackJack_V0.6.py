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

def decision(playerHand, dealerHand, bank, winnings, bet):
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            optionOne(playerHand, dealerHand, bank, winnings, bet)
        if option == "2":
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
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has won! You have lost :(")
                            bank -= bet
                            winnings -= bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                        elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                    elif dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("\nDealer has won! You have lost :(")
                        bank -= bet
                        winnings -= bet
                        print("\nYour Bank: {}".format(bank))
                        print("Your Winnings: {}".format(winnings))
                        time.sleep(1)
                        playAgain(bank, winnings)
                    elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has won! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
                elif dealerHand > 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has busted! You have won :)")
                    bank += bet
                    winnings += bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
                elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                bank -= bet
                winnings -= bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                playAgain(bank, winnings)
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has busted! You have won :)")
                bank += bet
                winnings += bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                playAgain(bank, winnings)
            elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
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



    print("\nWelcome To Conors's Blackjack! Version 5.0")
    
    time.sleep(2)
    
    #Bet System
    bet = int(input("Bet amount: "))
    if bet > bank:
        print("\nBet amount more than what you have. Try again!")
        time.sleep(1)
        game(bank, winnings)
    else:
        #Options Begin
        time.sleep(1)
        print("\nDealer Hand: {}".format(dealerHand))
        time.sleep(1)
        print("Player Hand: {}".format(playerHand))
        time.sleep(1)
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            optionOne(playerHand, dealerHand, bank, winnings, bet)
        if option == "2":
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
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has won! You have lost :(")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                        elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                    elif dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("\nDealer has won! You have lost :(")
                        bank -= bet
                        winnings -= bet
                        print("\nYour Bank: {}".format(bank))
                        print("Your Winnings: {}".format(winnings))
                        time.sleep(1)
                        playAgain(bank, winnings)
                    elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has won! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
                elif dealerHand > 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has busted! You have won :)")
                    bank += bet
                    winnings += bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
                elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                bank -= bet
                winnings -= bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                playAgain(bank, winnings)
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has busted! You have won :)")
                bank += bet
                winnings += bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                playAgain(bank, winnings)
            elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
        elif option != "1" or "2":
            print("\nOnly Choose 1 or 2.")
            time.sleep(1.5)
            decision(playerHand, dealerHand, bank, winnings, bet)


def playerBust(playerHand, bank, winnings, bet):
    if playerHand > 21:
            time.sleep(1.5)
            print("\nYou busted!")
            bank = bank - bet
            winnings = winnings - bet
            time.sleep(1.5)
            print("\nYour Bank: {}".format(bank))
            print("Your Winnings: {}".format(winnings))
            time.sleep(1.5)
            playAgain(bank, winnings)


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
            playAgain(bank, winnings)

def playAgain(bank, winnings):
    if bank == 0:
        time.sleep(2)
        print("You are out of funds.")
        time.sleep(1.5)
        cashout(bank, winnings)
    else:
        again = input("\n(1)Next Round\n(2)CashOut\n(1/2) ")
        if again.isdigit() == False:
            quit()
        elif int(again) != 1:
            quit()
        elif int(again) == 1:
            game(bank, winnings)
        elif int(again) == 2:
            cashout(bank, winnings)

def dealerDraw(dealerHand, playerHand):
    dealerHand = dealerHand + int(random.choice(suits))
    time.sleep(1)
    print("\nDealer: {}".format(dealerHand))
    print("Player: {}".format(playerHand))

def optionOne(playerHand, dealerHand, bank, winnings, bet):
        playerHand = playerHand + int(random.choice(suits))
        print("\nDealer: {}".format(dealerHand))
        print("Player: {}".format(playerHand))
        playerBust(playerHand, bank, winnings, bet)
        playerSafe(dealerHand, playerHand)
        playerBlackjack(playerHand, bank, winnings, bet)


def cashout(bank, winnings):
    print("\nYou have cashed out from Wally's Casino.")
    time.sleep(1.5)
    if winnings < 0:
        print("You have lost a total of ${} at the BlackJack table.".format(winnings))
        time.sleep(1.5)
        print("You left the casino broke as fuck.")
        time.sleep(1.5)
        print("\nThanks for playing!")
        time.sleep(2.5)
        quit()
    else:
        print("\nYou won a total of ${} at the BlackJack table.".format(winnings))
        time.sleep(1.5)
        print("You left the casino with ${} in your pocket.".format(bank))
        time.sleep(1.5)
        print("\nThanks for playing!")
        time.sleep(2.5)
        quit()



if __name__ == "__main__":
    system("cls")
    suits = ranks()
    global dealerHand
    global playerHand
    bank = int(input("\nHow much $ do you have? "))
    winnings = 0
    dealerHand = int(random.choice(suits)) 
    playerHand = int(random.choice(suits)) + int(random.choice(suits))



    print("\nWelcome To Conors's Blackjack! Version 6.0")
    
    time.sleep(2)
    
    #Bet System
    bet = int(input("Bet amount: "))
    if bet > bank:
        print("\nBet amount more than what you have. Try again!")
        time.sleep(1)
        game(bank, winnings)
    else:
        #Options Begin
        time.sleep(1)
        print("\nDealer Hand: {}".format(dealerHand))
        time.sleep(1)
        print("Player Hand: {}".format(playerHand))
        time.sleep(1)
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            optionOne(playerHand, dealerHand, bank, winnings, bet)
        if option == "2":
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
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has won! You have lost :(")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                        elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                    elif dealerHand > playerHand and dealerHand < 21:
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        print("\nDealer has won! You have lost :(")
                        bank -= bet
                        winnings -= bet
                        print("\nYour Bank: {}".format(bank))
                        print("Your Winnings: {}".format(winnings))
                        time.sleep(1)
                        playAgain(bank, winnings)
                    elif dealerHand > 21:
                            print("\nDealer: {}".format(dealerHand))
                            print("Player: {}".format(playerHand))
                            print("\nDealer has busted! You have won :)")
                            bank += bet
                            winnings += bet
                            print("\nYour Bank: {}".format(bank))
                            print("Your Winnings: {}".format(winnings))
                            time.sleep(1)
                            playAgain(bank, winnings)
                elif dealerHand > playerHand and dealerHand < 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has won! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
                elif dealerHand > 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has busted! You have won :)")
                    bank += bet
                    winnings += bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
                elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("\nDealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
            elif dealerHand > playerHand and dealerHand < 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has won! You have lost :(")
                bank -= bet
                winnings -= bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                playAgain(bank, winnings)
            elif dealerHand > 21:
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand))
                print("Dealer has busted! You have won :)")
                bank += bet
                winnings += bet
                print("\nYour Bank: {}".format(bank))
                print("Your Winnings: {}".format(winnings))
                time.sleep(1)
                playAgain(bank, winnings)
            elif dealerHand == 21:
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))
                    print("Dealer has blackjack! You have lost :(")
                    bank -= bet
                    winnings -= bet
                    print("\nYour Bank: {}".format(bank))
                    print("Your Winnings: {}".format(winnings))
                    time.sleep(1)
                    playAgain(bank, winnings)
        elif option != "1" or "2":
            print("\nOnly Choose 1 or 2.")
            time.sleep(1.5)
            decision(playerHand, dealerHand, bank, winnings, bet)



    

    
    