import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_hand(values):
    return [random.choice(values), random.choice(values)]

def calculate_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        hand = [1 if card == 11 else card for card in hand]
        score = sum(hand)
    return score

user_hand = deal_hand(cards)
computer_hand = deal_hand(cards)


while True:
    clear()
    print(f"Your cards: {user_hand} | Your score: {calculate_score(user_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")
    
    action = input("Type 'y' to get another card, 'n' to pass: ").lower()
    
    if action == 'y':
        user_hand.append(random.choice(cards))
        if calculate_score(user_hand) > 21:
            print("You went over 21! You lose.")
            break
    elif action == 'n':
        break
    else:
        print("Invalid input. Please type 'y' or 'n'.")

# After user finishes their turn
user_score = calculate_score(user_hand)
if user_score > 21:
    print("You went over 21! You lose.")
else:
    # Computer's turn: draw until score >= 17
    while calculate_score(computer_hand) < 17:
        computer_hand.append(random.choice(cards))
    computer_score = calculate_score(computer_hand)
    print(f"Computer's final hand: {computer_hand} | Computer's score: {computer_score}")

    # Decide winner
    print(f"Your final hand: {user_hand} | Your score: {user_score}")
    if computer_score > 21:
        print("Computer went over 21! You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a draw!")

