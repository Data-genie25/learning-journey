import random

choice = ["rock", "paper", "scissors"]
comp_choice = random.choice(["rock", "paper", "scissors"])

print("Welcome to the game of rsp!")
choice = input("What's your choice??\n")

if comp_choice == choice:
    print("Awww it's a tie!\n")
elif choice == "rock":
    if comp_choice == "scissors":
        print(choice, f"x {comp_choice}! \n")
        print("You win!")
    if comp_choice == "paper":
        print(choice, f"x {comp_choice}! \n")
        print("You lose :C")
elif choice == "scissors":
    if comp_choice == "rock":
        print(choice, f"x {comp_choice}! \n")
        print("You win!")
    if comp_choice == "paper":
        print(choice, f"x {comp_choice}! \n")
        print("You win!")
elif choice == "paper":
    if comp_choice == "scissors":
        print(choice, f"x {comp_choice}! \n")
        print("You win!")
    if comp_choice == "rock":
        print(choice, f"x {comp_choice}! \n")
        print("You lose!")
