import random
choices = ['rock', 'paper', 'scissors']

user = input("rock/paper/scissors: ").lower()  #.lower() matlab ROck likh diya toh bhi apne aap rock ho jayaga 

# Check if the input is valid
while user not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")
    user = input("rock/paper/scissors: ").lower()

computer = random.choice(choices) #computer ramdom lega

print("You chose:", user)
print("Computer chose:", computer)

#for tie
if user == computer:
    print("tie!")

# rock and scissor 
#  or paper and rock or,
#  scissor and paper , 
# yahi 3 posibilities hai
elif user == 'rock':
    if computer == 'scissors':
        print("You win!")
    else:
        print("Computer wins!")

elif user == 'paper':
    if computer == 'rock':
        print("You win!")
    else:
        print("Computer wins!")
elif user == 'scissors':
    if computer == 'paper':
        print("You win!")
    else:
        print("Computer wins!")