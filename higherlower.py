
import random

score = 0

people = {
    'Emma Watson, an actress from United Kingdom': 73_007_098,
    'Cristiano Ronaldo, a footballer from Portugal': 629_000_000,
    'Selena Gomez, a singer and actress from United States': 429_000_000,
    'Lionel Messi, a footballer from Argentina': 504_000_000,
    'Taylor Swift, a singer-songwriter from United States': 282_000_000,
    'Dwayne Johnson, an actor and wrestler from United States': 397_000_000,
    'Kylie Jenner, a model and entrepreneur from United States': 400_000_000,
    'Kim Kardashian, a media personality from United States': 364_000_000,
    'Virat Kohli, a cricketer from India': 269_000_000,
    'Zendaya, an actress and singer from United States': 184_000_000,
    'Billie Eilish, a singer-songwriter from United States': 111_000_000,
    'Shakira, a singer from Colombia': 92_000_000,
    'David Beckham, a footballer from United Kingdom': 87_000_000,
    'Priyanka Chopra, an actress from India': 90_000_000,
    'Chris Hemsworth, an actor from Australia': 58_000_000,
    'Sachin Tendulkar, a cricketer from India': 51_000_000,
    'Apple, a technology brand from United States': 34_000_000,
    'Google, a technology brand from United States': 39_000_000,
    'NASA, a space agency from United States': 92_000_000,
    'Nike, a sportswear brand from United States': 320_000_000,
    'Adidas, a sportswear brand from Germany': 30_000_000,
    'Louis Vuitton, a luxury brand from France': 55_000_000,
    'Gucci, a luxury brand from Italy': 52_000_000,
    'Samsung, a technology brand from South Korea': 25_000_000,
    'Coca-Cola, a beverage brand from United States': 3_500_000,
    'Netflix, a streaming brand from United States': 44_000_000,
    'Marvel, an entertainment brand from United States': 66_000_000,
}



keys = list(people.keys())
first_key = random.choice(keys)
keys.remove(first_key)


while True:
    second_key = random.choice(keys)
    while second_key == first_key:
        second_key = random.choice(keys)
    
    print(f"A: {first_key}")

    print(f"B: {second_key}")

    first_name = first_key.split(',')[0]
    second_name = second_key.split(',')[0]

    choice = input(f"Does {first_name} have more followers or {second_name} (Enter 'A' or 'B'): \n- ").lower()
    while choice not in ['a', 'b']:
        
        print("Sorry, invalid answer, type 'A' or 'B': ")
        choice = input("- ").lower()

    correct = max(people[first_key], people[second_key])

    # 'a' --> first_key
    guess = first_key if choice == 'a' else second_key

    if people[guess] == correct:
        print("Congratulations! You may continue...\n")
        score += 1
        first_key = guess
        keys.remove(second_key)

    else:
        print("Wrong, Game Over!")
        print(f"Your score is {score}")
        break
    
    if len(keys) == 0:
        print("Nice job, you've made it to the end!")
        print(f"Your score is {score}")
        break