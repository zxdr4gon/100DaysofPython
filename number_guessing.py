
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

input("'+' means go higher, '-' means go lower")

clear()

num = random.randint(1,100)

print("Pick a difficulty, 'easy' or 'hard'")

mode = input("- ")

attempts = 10 if mode == 'easy' else 5

game_over = False
hint = "-x-"

while not game_over:

    clear()
    print("Guess a number between 1-100")
    print(f"Hint: {hint}" if hint != '-x-' else "")
    print(f"You have {attempts} attempts.")

    guess = int(input(">>> "))


    if guess > num:
        print("Guess is a bit high, try again")
        hint = "-"
        attempts -= 1
    elif guess < num:
        print("Guess is too low, give it another shot")
        hint = "+"
        attempts -= 1

    elif guess == num:
        print("Yay! You have guessed the number! Good Job!")
        game_over = True

    if attempts <= 0:
        print("You have run out of attempts, you lose :(")
        game_over = True
    
    