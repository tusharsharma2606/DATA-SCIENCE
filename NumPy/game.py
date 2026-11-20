import random

ch = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice (Rock, Paper, Scissor): ")

comp_ch = random.choice(ch)

print("Computer chose:", comp_ch)
if user_choice == comp_ch:
    print("It's a tie!")
    
    
print("You chose:", user_choice)
if user_choice == "Rock":
    if comp_ch == "Scissor":
        print("You win!")
    else:
        print("Computer wins!") 
        
print("You chose:", user_choice)
if user_choice == "Paper":
    if comp_ch == "Rock":
        print("You win!")
    else:
        print("Computer wins!")
        
pr                    