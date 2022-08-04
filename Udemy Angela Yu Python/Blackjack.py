import random
import os
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    return random.choice(cards) #select random number from the list.

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if 11 in cards and 10 in cards and len(cards) == 2: #if 11 and 10 are in the cards, and if there are max of 2 cards(numbers), then return 0 = blackjack.
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21: #if there is an 11 in the cards and sum in the cards is over 21, then remove 11 and add 1 instead.
        cards.remove(11)
        cards.append(1)

    return sum(cards) #return sum of cards.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score): #compare score.
    
    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose. Computer has blackjack."
    elif user_score == 0:
        return "You win with a blackjack."
    elif user_score > 21:
        return "You went over 21, you lose."
    elif computer_score > 21:
        return "Computer went over 21, you win."
    elif user_score > computer_score:
        return "You win with highest score."
    else:
        return "Computer wins with highest score."

def play_game():
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = [] #store user's card in this list.
    computer_cards = [] #store computer's card in this list.
    game_active = True

    for _ in range(2): #draw two cards.
        user_cards.append(deal_card()) #add to the list user_cards.
        computer_cards.append(deal_card()) #add to the list computer_cards.

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while game_active:
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards}, score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_active = False
        else:
            #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            another_card = input("Do you want to draw another card?")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_active = False

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print("\nResults:")
    print(f"Your final cards {user_cards}, final score: {user_score}")
    print(f"Computer's final cards {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of blackjack? Type 'y or 'n': ") == 'y':
    os.system('cls')
    play_game()