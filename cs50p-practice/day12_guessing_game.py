import random

target = random.randint(1, 100)
guess = int(input("Guess the number (1-100): "))

while guess != target:
    if guess < target:
        print("Higher!")
    elif guess > target:
        print("Lower!")
    
    guess = int(input("Guess again: "))

print("It's a match!")

