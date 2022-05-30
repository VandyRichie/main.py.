import random
while True:
 user_action = input("Enter a choice (R, P, S):")

#Computer choice
 possible_actions = ["R", "P", "S"]
 computer_action = random.choice(possible_actions)
 print(f"\nYou choose {user_action}, computer choose {computer_action}.\n")

#Find Winner
 if user_action == computer_action:
    print(f"Both players chose {user_action}. A tie!")
 elif user_action =="R":
    if computer_action == "S":
        print("R beats S ! you win!")
    else:
        print("P covers R ! You lose!")
 elif user_action == "P":
    if computer_action == "R":
        print("P covers R ! You win!")
    else:
        print("S cuts P ! You lose!")
 elif user_action == "S":
    if computer_action == "P":
        print("S cuts P ! You win!")
    else:
        print("R smashes Scissors! You lose!")

 play_again = input("Play again? (y/n):")
 if play_again.lower() != "y":
    break
print("Thanks for playing")