import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    #Determine the winner based on the rules of Rock-Paper-Scissors.
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play():
    #Play a single round of Rock-Paper-Scissors.
    print("\nChoose rock, paper, or scissors ")
    user_choice = input("Enter Your Choice: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"\n        You chose         : {user_choice}")
    print(f"        The computer chose: {computer_choice}\n")

    winner = determine_winner(user_choice, computer_choice)
    
    if winner == 'tie':
        print("---------- It's a tie! ----------\n")
    elif winner == 'user':
        print("---------- Congratulations! You win! ----------\n")
    else:
        print("---------- Oh, the computer wins! ----------\n")
    
    return winner

print("--------------- Welcome to the Rock-Paper-Scissors Game! ---------------")
print("\n1.Rock beats Scissors.\n2.Scissors beats Paper.\n3.and Paper beats Rock.")
print("\nLet's Start the GAME!")
    
user_score = 0
computer_score = 0
    
while True:
    winner = play()
        
    if winner == 'user':
        user_score += 1
    elif winner == 'computer':
        computer_score += 1
    
    print(f"Current Score :   You     : {user_score}\n                  Computer: {computer_score}")
        
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != 'yes':
        break
    
print("\nFinal Score - You: {}, Computer: {}".format(user_score, computer_score))
if(user_score > computer_score): print("------ You Win the Game! ------")
elif(computer_score > user_score): print("--- Oops You Lose the Game ---")
else: print("Its a Tie!")
print("\nThanks for playing! ")
