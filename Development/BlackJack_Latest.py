import random
import time
import sys
from os import system
from random import shuffle

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
    ranks = [ "1", "2", "3", "4", "5", "6", "7","8", "9", "10", "10", "10"]
    return ranks

def cards():
    cards = [ "Clubs ♠", "Diamonds ♦", "Hearts ♥", "Spades ♣", "Clubs ♠", "Diamonds ♦", "Hearts ♥", "Spades ♣","Clubs ♠", "Diamonds ♦", "Hearts ♥", "Spades ♣"]
    return cards

def randy():
    randy = random

def decision(playerHand, dealerHand, bank, winnings, bet, count):
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            optionOne(playerHand, dealerHand, bank, winnings, bet, count)
        elif option == "2":
            dealerHand = dealerHand + int(random.choice(suits))
            time.sleep(1)
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                time.sleep(1)
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand)) 
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    time.sleep(1)
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))   
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        time.sleep(1)
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                        elif dealerHand > 21:
                            bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                    elif dealerHand > playerHand and dealerHand < 21:
                        bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                        time.sleep(1)
                        playAgain(bank, winnings, count)
                    elif dealerHand > 21:
                            bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                elif dealerHand > playerHand and dealerHand < 21:
                    bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
                elif dealerHand > 21:
                    bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
                elif dealerHand == 21:
                    bank, winnings, count = dealerBlackJack(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
            elif dealerHand > playerHand and dealerHand < 21:
                bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                time.sleep(1)
                playAgain(bank, winnings, count)
            elif dealerHand > 21:
                bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                time.sleep(1)
                playAgain(bank, winnings, count)
            elif dealerHand == 21:
                    bank, winnings, count = dealerBlackJack(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
        elif option != "1" or "2":
            print("\nOnly Choose 1 or 2.")
            time.sleep(1.5)
            decision(playerHand, dealerHand, bank, winnings, bet, count)


def displayBank(bank, winnings):
    print("\nCurrent bank balance: {}".format(bank))
    print("Current Winnings: {}".format(winnings))

def displayCount(count):
    print("Round: {}".format(count))
    
    

def game(bank, winnings, count):
    system("cls")
    global dealerHand
    global playerHand
    displayBank(bank, winnings)
    dealerHand = int(random.choice(suits)) 
    playerHand = int(random.choice(suits)) + int(random.choice(suits))

    print("\nWelcome To Conors's Blackjack! Version 0.8")
    displayCount(count)
    time.sleep(2)
    
    #Bet System
    bet = int(input("Bet amount: "))
    if bet > bank:
        print("\nBet amount more than what you have. Try again!")
        time.sleep(1)
        game(bank, winnings, count)
    else:
        #Options Begin
        time.sleep(1)
        print("\nDealer Hand: {}".format(dealerHand))
        time.sleep(1)
        print("Player Hand: {}".format(playerHand))
        time.sleep(1)
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            optionOne(playerHand, dealerHand, bank, winnings, bet, count)
        elif option == "2":
            dealerHand = dealerHand + int(random.choice(suits))
            time.sleep(1)
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                time.sleep(1)
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand)) 
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    time.sleep(1)
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))   
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        time.sleep(1)
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                        elif dealerHand > 21:
                            bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                    elif dealerHand > playerHand and dealerHand < 21:
                        bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                        time.sleep(1)
                        playAgain(bank, winnings, count)
                    elif dealerHand > 21:
                            bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                elif dealerHand > playerHand and dealerHand < 21:
                    bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
                elif dealerHand > 21:
                    bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
                elif dealerHand == 21:
                    bank, winnings, count = dealerBlackJack(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
            elif dealerHand > playerHand and dealerHand < 21:
                bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                time.sleep(1)
                playAgain(bank, winnings, count)
            elif dealerHand > 21:
                bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                time.sleep(1)
                playAgain(bank, winnings, count)
            elif dealerHand == 21:
                    bank, winnings, count = dealerBlackJack(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
        elif option != "1" or "2":
            print("\nOnly Choose 1 or 2.")
            time.sleep(1.5)
            decision(playerHand, dealerHand, bank, winnings, bet, count)



def playerBust(playerHand, dealerHand, bank, winnings, bet, count):
            time.sleep(1.5)
            print("\nYou busted!")
            bank = bank - bet
            winnings = winnings - bet
            count += 1
            time.sleep(1.5)
            print("\nYour Bank: {}".format(bank))
            print("Your Winnings: {}".format(winnings))
            time.sleep(1.5)
            playAgain(bank, winnings, count)


def playerSafe(dealerHand, playerHand, bank, winnings, bet, count):
            decision(playerHand, dealerHand, bank, winnings, bet, count)


def playAgain(bank, winnings, count):
    if bank == 0:
        time.sleep(2)
        print("You are out of funds.")
        time.sleep(1.5)
        cashout(bank, winnings, count)
    else:
        again = input("\n(1)Next Round\n(2)CashOut\n(1/2) ")
        if again.isdigit() == False:
            quit()
        elif int(again) == 1:
            game(bank, winnings, count)
        elif int(again) == 2:
            cashout(bank, winnings, count)

def optionOne(playerHand, dealerHand, bank, winnings, bet, count):
        playerHand = playerHand + int(random.choice(suits))
        print("\nDealer: {}".format(dealerHand))
        print("Player: {}".format(playerHand))
        if playerHand > 21:
            bank, winnings, count = playerBust(dealerHand, playerHand, bank, winnings, bet, count)
            playAgain(bank, winnings, count)
        elif playerHand < 21:
            bank, winnings, count = playerSafe(dealerHand, playerHand, bank, winnings, bet, count)
            playAgain(bank, winnings, count)
        elif playerHand == 21:
            bank, winnings, count = playerBlackjack(dealerHand, playerHand, bank, winnings, bet, count)
            playAgain(bank, winnings, count)


def cashout(bank, winnings, count):
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


def dealerWin(dealerHand, playerHand, bank, winnings, bet, count):
    time.sleep(1.5)
    print("\nDealer: {}".format(dealerHand))
    print("Player: {}".format(playerHand))
    time.sleep(1.5)
    print("\nDealer has won! You have lost :(")
    bank -= bet
    winnings -= bet
    count += 1
    time.sleep(1.5)
    print("\nYour Bank: {}".format(bank))
    print("Your Winnings: {}".format(winnings))
    return bank, winnings, count

def playerWin(dealerHand, playerHand, bank, winnings, bet, count):
    print("\nDealer: {}".format(dealerHand))
    time.sleep(1.5)
    print("Player: {}".format(playerHand))
    time.sleep(1.5)
    print("Dealer has busted! You have won :)")
    bank += bet
    winnings += bet
    count += 1
    time.sleep(1.5)
    print("\nYour Bank: {}".format(bank))
    print("Your Winnings: {}".format(winnings))
    return bank, winnings, count

def dealerBlackJack(dealerHand, playerHand, bank, winnings, bet, count):
    time.sleep(1.5)
    print("\nDealer: {}".format(dealerHand))
    print("Player: {}".format(playerHand))
    time.sleep(1.5)
    print("\nDealer has blackjack! You have lost :(")
    bank -= bet
    winnings -= bet
    count += 1
    time.sleep(1.5)
    print("\nYour Bank: {}".format(bank))
    print("Your Winnings: {}".format(winnings))
    return bank, winnings, count


def playerBlackjack(dealerHand, playerHand, bank, winnings, bet, count):
        print("\nDealer: {}".format(dealerHand))
        time.sleep(1.5)
        print("Player: {}".format(playerHand))
        time.sleep(1.5)
        print("\nPlayer has blackjack! You have won :)")
        bank += bet + bet/2
        winnings += bet + bet/2
        count += 1
        time.sleep(1.5)
        print("\nYour Bank: {}".format(bank))
        print("Your Winnings: {}".format(winnings))
        return bank, winnings, count

def suitCombo():
    random.shuffle(suits)
    random.shuffle(ranks)
    towers = list(zip(suits, ranks))
    return towers


if __name__ == "__main__":
    system("cls")
    suits = ranks()
    global dealerHand
    global playerHand
    bank = int(input("\nHow much $ do you have? "))
    winnings = 0
    dealerHand = int(random.choice(suits)) 
    playerHand = int(random.choice(suits)) + int(random.choice(suits))
    counter = list(range(1,100))
    count = 1
    

    print("\nWelcome To Conors's Blackjack! Version 0.8")
    displayCount(count)
    
    #Bet System
    bet = int(input("Bet amount: "))
    if bet > bank:
        print("\nBet amount more than what you have. Try again!")
        time.sleep(1)
        game(bank, winnings, count)
    else:
        #Options Begin
        time.sleep(1)
        print("\nDealer Hand: {}".format(dealerHand))
        time.sleep(1)
        print("Player Hand: {}".format(playerHand))
        time.sleep(1)
        option = input("\n(1) Hit \n(2) Stand\nChoice: ")
        if option == "1":
            optionOne(playerHand, dealerHand, bank, winnings, bet, count)
        elif option == "2":
            dealerHand = dealerHand + int(random.choice(suits))
            time.sleep(1)
            print("\nDealer: {}".format(dealerHand))
            print("Player: {}".format(playerHand))
            if dealerHand < 21 and dealerHand <= playerHand:
                dealerHand = dealerHand + int(random.choice(suits))
                time.sleep(1)
                print("\nDealer: {}".format(dealerHand))
                print("Player: {}".format(playerHand)) 
                if dealerHand < 21 and dealerHand <= playerHand:
                    dealerHand = dealerHand + int(random.choice(suits))
                    time.sleep(1)
                    print("\nDealer: {}".format(dealerHand))
                    print("Player: {}".format(playerHand))   
                    if dealerHand < 21 or dealerHand <= playerHand:
                        dealerHand = dealerHand + int(random.choice(suits))
                        time.sleep(1)
                        print("\nDealer: {}".format(dealerHand))
                        print("Player: {}".format(playerHand))
                        if dealerHand > playerHand and dealerHand < 21:
                            bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                        elif dealerHand > 21:
                            bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                    elif dealerHand > playerHand and dealerHand < 21:
                        bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                        time.sleep(1)
                        playAgain(bank, winnings, count)
                    elif dealerHand > 21:
                            bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                            time.sleep(1)
                            playAgain(bank, winnings, count)
                elif dealerHand > playerHand and dealerHand < 21:
                    bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
                elif dealerHand > 21:
                    bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
                elif dealerHand == 21:
                    bank, winnings, count = dealerBlackJack(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)
            elif dealerHand > playerHand and dealerHand < 21:
                bank, winnings, count = dealerWin(dealerHand, playerHand, bank, winnings, bet, count)
                time.sleep(1)
                playAgain(bank, winnings, count)
            elif dealerHand > 21:
                bank, winnings, count = playerWin(dealerHand, playerHand, bank, winnings, bet, count)
                time.sleep(1)
                playAgain(bank, winnings, count)
            elif dealerHand == 21:
                    bank, winnings, count = dealerBlackJack(dealerHand, playerHand, bank, winnings, bet, count)
                    time.sleep(1)
                    playAgain(bank, winnings, count)        
        elif option != "1" or "2":
            print("\nOnly Choose 1 or 2.")
            time.sleep(1.5)
            decision(playerHand, dealerHand, bank, winnings, bet, count)



    

    
    