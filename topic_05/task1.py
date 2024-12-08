import random

choices = ["stone", "scissor", "paper"]
rules = {"stone": "scissor", "scissor": "paper", "paper": "stone"}

while True:
    user = input("Your choice (stone, scissor, paper) or 'exit': ").lower()
    if user == "exit":
        break
    if user not in choices:
        print("Invalid choice, try again.")
        continue
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if user == computer:
        print("It's a tie!")
    elif rules[user] == computer:
        print("You win!")
    else:
        print("Computer wins!")