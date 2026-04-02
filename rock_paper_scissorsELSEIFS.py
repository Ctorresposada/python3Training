import random
computer_options= ["rock","paper","scissors"]
computer_choice=random.choice(computer_options)
user_choice=input("Do you want rock,paper, or scissors? \n")
user_choice=user_choice.lower()
print("Converting to lower case "+ user_choice)
print("Computer choice was "+ computer_choice)
if computer_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice=="scissors":
        print("user WINS")
elif user_choice == "paper" and computer_choice=="rock":
        print("user WINS")
elif user_choice == "scissors" and computer_choice=="paper":
        print("user WINS")
else:
       print("You lose, COMPUTER WINS")