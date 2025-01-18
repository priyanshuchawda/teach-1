import random

choices = ['rock', 'paper', 'scissors']
user = input("rock/paper/scissors: ").lower()
while user not in choices:
    user = input("Invalid choice!, rock/paper/scissors: ").lower()

computer = random.choice(choices)
print(f"You chose: {user}\nComputer chose: {computer}")

if user == computer:
    print("Tie!")
elif (user, computer) in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
    print("You win!")
else:
    print("Computer wins!")
