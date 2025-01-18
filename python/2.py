import random

choices = ['rock', 'paper', 'scissors']
user = input("rock/paper/scissors: ").lower()
while user not in choices:
    user = input("Invalid choice! rock/paper/scissors: ").lower()
computer = random.choice(choices)
print(f"You chose: {user}\nComputer chose: {computer}")

winning_combos = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

if user == computer:
    print("Tie!")
    
elif winning_combos[user] == computer:
    print("You win!")
else:
    print("Computer wins!")