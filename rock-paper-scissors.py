import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    #To ensure player picks an option from the list, introduce a "while" loop
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()


    #Next, specify the win, lose or tie conditions
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    Rematch = input("Would you like to play again? (yes/no): ").lower()

    if Rematch != "yes":
        break
print("Thank you for playing. Goodbye!")

