import random
print("\nWELCOME TO JACK'S ROCK, PAPER, SCISSORS GAME!!!\n")
while True:
    choices = ["rock","paper", "scissors"]
    user_choice = input("ROCK, PAPER, SCISSORS, SHOOT!!! ").lower()
    if user_choice not in choices:
        print("Sorry, please enter either rock, paper or scissors!")
        continue
    computer_choice = random.choice(choices)
    print(f"The computer has chosen {computer_choice}!")
    win = "YOU WIN!!!"
    if user_choice == choices[0] and computer_choice == choices[2]:
        print(win)
        
    elif user_choice == choices[1] and computer_choice == choices[0]:
        print(win)
        
    elif user_choice == choices[2] and computer_choice == choices[1]:
        print(win)
        
    elif user_choice == computer_choice:
        print("Its a tie!!!")
        
    else:
        print("YOU HAVE LOST!!!")
    while True:
        replay = input("Would you like to play again? (Yes or No) ").lower()
        if replay == "yes":
            break
        elif replay == "no":
            exit()
        else:
            print("Please enter \"Yes\" or \"No\"")

    

        

