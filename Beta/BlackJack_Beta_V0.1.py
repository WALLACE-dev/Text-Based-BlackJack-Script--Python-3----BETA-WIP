import random
import time
import sys
import os

def cards():
    cards = [1,2,3,4,5,6,7,8,9,10,10,10]
    return cards
#BlackJack or 21 Game
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
        elif int(again) == 1:
            game(bank, winnings)
        elif int(again) == 2:
                cashout(bank, winnings)

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

def game(bank, winnings):
    cards = [1,2,3,4,5,6,7,8,9,10,10,10]
    dealerCards = []
    playerCards = []
    time.sleep(1.5)
    print("\nBank: {}".format(bank))
    print("Winnings: {}".format(winnings))

    bet = int(input("\nBet amount: "))
    if bet > bank:
        print("\nBet amount more than what you have. Try again!")
        time.sleep(1)
        game(bank, winnings)
    else:
        #Deal Hands
        while len(dealerCards) != 2:
            if len(dealerCards) < 2:
                dealerCards.append(random.choice(cards))
            if len(dealerCards) == 2:
                print("\nDealer: [{}, X]".format(dealerCards[0]))
            if len(dealerCards) > 2:
                print("\nDealer: {} ".format(dealerCards))
            
        #Play Hand    
        while len(playerCards) != 2:
            if len(playerCards) < 2:
                playerCards.append(random.choice(cards))
            if len(playerCards) >= 2:
                print("Player has {} ".format(playerCards))


        #Sum of Dealer Cards
        if sum(dealerCards) == 21:
            print("Dealer has Blackjack and wins!")
            bank -= bet
            winnings -= bet
            playAgain(again, winnings)
        elif sum(dealerCards) > 21:
            print("Dealer has busted!")
            bank += bet
            winnings += bet
            playAgain(bank, winnings)

        #Sum of Player Cards
        while sum(playerCards) < 21:
            action_taken = input("\n(1)Hit\n(2)Stay\n(1/2)  ")
            if str(action_taken) == "1":
                playerCards.append(random.choice(cards))
                print("\nPlayer: {} \nHand: {}".format(sum(playerCards), playerCards))
            elif str(action_taken) == "2":
                print("\nDealer: {} \nHand: {}".format(sum(dealerCards), dealerCards))
                print("\nPlayer: {} \nHand: {}".format(sum(playerCards), playerCards))
                if sum(dealerCards) > sum(playerCards):
                    time.sleep(1.5)
                    print("Dealer has won! You have lost $")
                    bank -= bet
                    winnings -= bet
                    time.sleep(1.5)
                    playAgain(bank, winnings)
                else:
                    while sum(dealerCards) < sum(playerCards):
                        time.sleep(1.5)
                        dealerCards.append(random.choice(cards)) 
                        print("\nDealer: {} \nHand: {}".format(sum(dealerCards), dealerCards))
                        print("\nPlayer: {} \nHand: {}".format(sum(playerCards), playerCards))
                        if sum(dealerCards) > 21:
                            time.sleep(1.5)
                            print("Dealer has busted! You gained $")
                            bank += bet
                            winnings += bet
                            time.sleep(1.5)
                            playAgain(bank, winnings)
                        elif sum(dealerCards) == 21:
                            time.sleep(1.5)
                            print("Dealer has blackjack! You lost $")
                            bank -= bet
                            winnings -= bet
                            time.sleep(1.5)
                            playAgain(bank, winnings)
                        elif sum(dealerCards) > sum(playerCards):
                            time.sleep(1.5)
                            print("Dealer has won! You have lost $")
                            bank -= bet
                            winnings -= bet
                            time.sleep(1.5)
                            playAgain(bank, winnings)
                        elif sum(dealerCards) == sum(playerCards) and sum(dealerCards) > 16:
                            time.sleep(1.5)
                            print("You have pushed! Reset.")
                            time.sleep(1.5)
                            playAgain(bank, winnings)
        if sum(playerCards) > 21:
            time.sleep(1.5)
            print("You have busted! You lost $")
            bank -= bet
            winnings -= bet
            time.sleep(1.5)
            playAgain(bank, winnings)
        elif sum(playerCards) == 21:
            time.sleep(1.5)
            print("You have blackjack! You gained $")
            bank += bet
            winnings += bet
            time.sleep(1.5)
            playAgain(bank, winnings)
    
if __name__ == "__main__":
    bank = int(input("\nHow much $ do you have? "))
    winnings = 0
    cards = cards()
    dealerCards = []
    playerCards = []
    print("Welcome to WALLACES BlackJack Beta Version 0.5")
    
    print("\nBank: {}".format(bank))
    print("Winnings: {}".format(winnings))

    bet = int(input("\nBet amount: "))
    if bet > bank:
        print("\nBet amount more than what you have. Try again!")
        time.sleep(1)
        game(bank, winnings)
    else:
        #Deal Hands
        while len(dealerCards) != 2:
            if len(dealerCards) < 2:
                dealerCards.append(random.choice(cards))
            if len(dealerCards) == 2:
                print("\nDealer: [{}, X]".format(dealerCards[0]))
            if len(dealerCards) > 2:
                print("\nDealer: {} ".format(dealerCards))
            
        #Play Hand    
        while len(playerCards) != 2:
            if len(playerCards) < 2:
                playerCards.append(random.choice(cards))
            if len(playerCards) >= 2:
                print("Player has {} ".format(playerCards))


        #Sum of Dealer Cards
        if sum(dealerCards) == 21:
            print("Dealer has Blackjack and wins!")
            bank -= bet
            winnings -= bet
            playAgain(again, winnings)
        elif sum(dealerCards) > 21:
            print("Dealer has busted!")
            bank += bet
            winnings += bet
            playAgain(bank, winnings)

        #Sum of Player Cards
        while sum(playerCards) < 21:
            action_taken = input("\n(1)Hit\n(2)Stay\n(1/2)  ")
            if str(action_taken) == "1":
                playerCards.append(random.choice(cards))
                print("\nPlayer: {} \nHand: {}".format(sum(playerCards), playerCards))
            elif str(action_taken) == "2":
                print("\nDealer: {} \nHand: {}".format(sum(dealerCards), dealerCards))
                print("\nPlayer: {} \nHand: {}".format(sum(playerCards), playerCards))
                if sum(dealerCards) > sum(playerCards):
                    time.sleep(1.5)
                    print("Dealer has won! You have lost $")
                    bank -= bet
                    winnings -= bet
                    time.sleep(1.5)
                    playAgain(bank, winnings)
                else:
                    while sum(dealerCards) < sum(playerCards):
                        time.sleep(1.5)
                        dealerCards.append(random.choice(cards)) 
                        print("\nDealer: {} \nHand: {}".format(sum(dealerCards), dealerCards))
                        print("\nPlayer: {} \nHand: {}".format(sum(playerCards), playerCards))
                        if sum(dealerCards) > 21:
                            time.sleep(1.5)
                            print("Dealer has busted! You gained $")
                            bank += bet
                            winnings += bet
                            time.sleep(1.5)
                            playAgain(bank, winnings)
                        elif sum(dealerCards) == 21:
                            time.sleep(1.5)
                            print("Dealer has blackjack! You lost $")
                            bank -= bet
                            winnings -= bet
                            time.sleep(1.5)
                            playAgain(bank, winnings)
                        elif sum(dealerCards) > sum(playerCards):
                            time.sleep(1.5)
                            print("Dealer has won! You have lost $")
                            bank -= bet
                            winnings -= bet
                            time.sleep(1.5)
                            playAgain(bank, winnings)
                        elif sum(dealerCards) == sum(playerCards) and sum(dealerCards) > 16:
                            time.sleep(1.5)
                            print("You have pushed! Reset.")
                            time.sleep(1.5)
                            playAgain(bank, winnings)
        if sum(playerCards) > 21:
            time.sleep(1.5)
            print("You have busted! You lost $")
            bank -= bet
            winnings -= bet
            time.sleep(1.5)
            playAgain(bank, winnings)
        elif sum(playerCards) == 21:
            time.sleep(1.5)
            print("You have blackjack! You gained $")
            bank += bet
            winnings += bet
            time.sleep(1.5)
            playAgain(bank, winnings)
