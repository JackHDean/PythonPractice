#1

#for num in range(1500, 2701):
    #if num % 7 == 0 and num % 5 == 0:
        #print(num)

#2

#for num in range(0,7):
    #if num != 3 and num != 6:
        #print(num)
        
#3

#for num in range(1,51):
    #if num % 3 == 0:
        #print("Fizz")
    #elif num % 5 == 0:
        #print("Buzz")
    #elif num % 3 == 0 and num % 5 == 0:
        #print("FizzBuzz")
    #else:
        #print(num)
        
#4
#evens = []
#for i in range(100, 401):
    #if i % 2 == 0:
        #evens.append(str((i)))
#sep = ", ".join(evens)
#print(sep)

#5

#num = int(input("Please enter a number here: "))
#factors = []
#for i in range(2, num+1):
    #if num % i == 0:
        #factors.append(i)

#if len(factors) == 2:
    #print(f"{num} is a prime number as is only has factors {factors}")
#else:
    #print(f"{num} is not a prime number as is has more than two factors which include {factors}")

#6

#def find_max(num1, num2, num3):
    #list = []
    #list.append(num1)
    #list.append(num2)
    #list.append(num3)
    #print("The max number is {}".format(max(list)))

#find_max(num1 = int(input("Give me the first number: ")), 
#num2 = int(input("Give me the second number: ")), 
#num3 = int(input("Give me the third number: ")))

#7
#import random
#correct = random.randrange(1,10)

#while True:
    #guess = int(input("Guess the number that I am thinking of between 1 and 9: "))
    #if guess == correct:
        #print(f"CORRECT!!! THE NUMBER WAS {correct}!")
        #break
    #else:
        #print("Incorrect. Try again.")
        #continue

#8 

#def string_rev(str):
    #print(str[::-1])

#string_rev(input("Enter a word for me to reverse: "))

#9

#def count_cases(str):
    #uppers=[]
    #lowers=[]
    #others=[]
    #for upper in str:
        #if upper.isupper():
            #uppers.append(upper)
    #print(f"\nYou have {len(uppers)} uppercase letters in your string!")

    #for lower in str:
        #if lower.islower():
            #lowers.append(lower)
    #print(f"You have {len(lowers)} uppercase letters in your string!")

    #for other in str:
        #if not other.isalpha():
            #others.append(other)
    #print(f"\nYou ALSO have {len(others)} different characters in your string!\n")


#count_cases(input("Please enter a word here: "))

#10

#menu = {1: "Beef", 2: "Chicken", 3: "Lamb", 4: "Pork"}
#for num, food in menu.items():
    #print(f"\nType {num} if you want to order {food}\n") # prints out menu

#while True:
    #user_choice = (input("\nCan I take Your order? "))
    #if not user_choice.isalpha() and int(user_choice) in range(1,5): # if user enters a number between 1-4
        #user_choice = int(user_choice)
        #break
    #else: 
        #print("Menu numbers only please!")
        #continue
#for num in menu.keys(): # iterate over keys in the menu dictionary
    #if num == user_choice: # see if the iterated key matches the user input
        #print(f"You have selected " + menu[num])
        #while True:

            #weight = input("Enter weight of meat (in kg): ")
            #if not weight.isalpha(): # checking that the weight is a number
                #weight = float(weight)
                #break
            #else: 
                #print("Please select a valid metrical value (in kg)")
                #continue
        #if user_choice == 1:
            #time = 50 * int(weight) + 20
            #print("The cooking time for a piece of " + menu[num] + f" that weighs {weight}kg is {time} minutes")

        #elif user_choice == 2:
            #time = 45 * int(weight) + 20
            #print("The cooking time for a piece of " + menu[num] + f" that weighs {weight} is {time} minutes")

        #elif user_choice == 3:
            #time = 60 * int(weight) + 30
            #print("The cooking time for a piece of " + menu[num] + f" that weighs {weight} is {time} minutes")
        #else:
            #time = 70 * int(weight) + 35
            #print("The cooking time for a piece of " + menu[num] + f" that weighs {weight} is {time} minutes")

#11 

#import random
#print("\nWELCOME TO JACK'S ROCK, PAPER, SCISSORS GAME!!!\n")
#while True:
    #choices = ["rock","paper", "scissors"]
    #user_choice = input("ROCK, PAPER, SCISSORS, SHOOT!!! ").lower()
    #if user_choice not in choices:
        #print("Sorry, please enter either rock, paper or scissors!")
        #continue
    #computer_choice = random.choice(choices)
    #print(f"The computer has chosen {computer_choice}!")
    #win = "YOU WIN!!!"
    #if user_choice == choices[0] and computer_choice == choices[2]:
        #print(win)
        
    #elif user_choice == choices[1] and computer_choice == choices[0]:
        #print(win)
        
    #elif user_choice == choices[2] and computer_choice == choices[1]:
        #print(win)
        
    #elif user_choice == computer_choice:
        #print("Its a tie!!!")
        
    #else:
        #print("YOU HAVE LOST!!!")
    #while True:
        #replay = input("Would you like to play again? (Yes or No) ").lower()
        #if replay == "yes":
            #break
        #elif replay == "no":
            #exit()
        #else:
            #print("Please enter \"Yes\" or \"No\"")

    
