import random

target = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number (1-100): "))
        break
    except ValueError:
        print("Please enter a valid number.")

while guess != target:
    if guess < target:
        print("Higher!")
    elif guess > target:
        print("Lower!")
    
    while True:
        try:
            guess = int(input("Guess again: "))
            break
        except ValueError:
            print("Please enter a valid number.")

print("It's a match!")

#day12_guessing_game.py

