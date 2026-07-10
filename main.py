import art
import random
import os

print (art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        return score - 10
    else:
        return score

# players choice
play = input("DO YOU WANT TO PLAY A GAME OF BLACK JACK??? 'y' for yes, 'n' for no: ").lower()

while True:
    while play != "y" and play != "n":
        print("Sorry only type y or n")
        play = input("'y', 'n': ").lower()

# cards are dealt / shows players hand and score / shows dealer single card score
    if play == "y":
        print("Lets PLay")

        user_hand = [deal_card(), deal_card()]
        user_score = calculate_score(user_hand)
        dealer_hand = [deal_card(), deal_card()]
        dealer_score = calculate_score(dealer_hand)

        print(f"your cards: {user_hand}, score: {user_score}")
        print(f"dealer card {dealer_hand[0]}")

# checks player & dealer hand for blackjack / if no blackjack then game continues
        if dealer_score == 21:
            if user_score == 21:
                print(
                    f"Lame!! Both hit blackjack, dealer cards: {dealer_hand}, delaer score: {dealer_score} wins by default...")
                print(f" your cards: {user_hand}, your score: {user_score}")
            else:
                print("BOOOO!!!!! Dealer hit Black Jack (; ;)")
                print(f"dealer cards: {dealer_hand}, dealer score: {dealer_score}")
                print(f"your cards: {user_hand}, your score: {user_score}")
        elif dealer_score != 21 and user_score == 21:
            print(f"Hell Yeah!!! BlackJack!!! YOU WIN!!! your cards: {user_hand}, your score: {user_score}")
            print(f"dealer's cards: {dealer_hand}, dealer's score: {dealer_score} ")
        else:
            user_choice = input("Do you want to draw another card? 'y' or 'n'?: ")

# draw a card / calculates score / bust check
            while user_choice == "y":
                user_hand.append(deal_card())
                user_score = calculate_score(user_hand)
                if user_score > 21:
                    print(f"Bust!!! YOU LOST!!! score: {user_score}")
                    break
                else:
                    print(f"your cards: {user_hand}, score: {user_score}")
                    user_choice = input("Do you want to draw another card? 'y' or 'n'?: ")

# checks player score / calculates dealer score / dealer draws / dealer bust check
            if user_score <= 21:
                dealer_score = calculate_score(dealer_hand)
                while dealer_score <= 16:
                    dealer_hand.append(deal_card())
                    dealer_score = calculate_score(dealer_hand)
                    if dealer_score > 21:
                        print(f"Dealer Busts!!! You win!!! dealer score: {dealer_score}")
                        break
                    else:
                        print(f"dealer cards: {dealer_hand}, dealer score: {dealer_score}")

# win / lose / tie
                if dealer_score <= 21:
                    if user_score > dealer_score:
                        print(f"YOU WIN!!! your cards: {user_hand}, your score: {user_score}")
                        print(f"Dealer LOSES!! dealer cards: {dealer_hand}, dealer score: {dealer_score}")
                    elif user_score == dealer_score:
                        print("its a Tie!")
                        print(f"dealer cards: {dealer_hand}, dealer score: {dealer_score}")
                        print(f"you lose. your cards: {user_hand}, your score: {user_score}")
                    else:
                        print(f"Dealer wins. dealer cards: {dealer_hand}, dealer score: {dealer_score}")
                        print(f"you lose. your cards: {user_hand}, your score: {user_score}")

# if you dont want to play
    elif play == "n":
        print("ok maybe next time")
        break

# play again?
    play = input("Do you want to play again? 'y' or 'n': ").lower()
    while play != "y" and play != "n":
        print("Sorry only type y or n")
        play = input("'y', 'n': ").lower()

    if play == "n":
        print("Cool, thanks for playing. ^^")
        break

# clears console 
    os.system("cls")