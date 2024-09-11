import random

while True:
    user = input("Enter a choice (Rock, Paper, Scissors): ")
    possibilities = ["Rock", "Paper", "Scissors"]
    computer = random.choice(possibilities)
    print(f"\nYou choose {user},computer choose {computer}.\n")

    if user == computer:
        print(f"Both the players selected {user}. It's a tie!")
    elif user == "Rock":
        if computer == "Scissors":
            print(f"Rock vs Scissors ~> Rock wins")
        else:
            print("Rock vs Paper ~> Paper wins")

    elif user == "Paper":
        if computer == "Rock":
            print("Paper vs Rock ~> Paper wins")
        else:
            print("Paper vs Scissors ~> Scissors wins")
    elif user == "Scissors":
        if computer == "Paper":
            print("Scissors vs Paper ~> Scissors wins")

        else:
            print("Rock vs Scissors ~> Rock wins")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
            
