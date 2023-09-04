while True:

    alien = {"x_position" : 0, "speed" : input("What speed do you want to go? (Slow, mediium, fast)".lower())}

    if alien["speed"] == "slow":
        x_position = alien["x_position"] + 1
        break
    elif alien["speed"] == "medium":
        x_position = alien["x_position"] + 2
        break
    elif alien["speed"] == "fast":
        x_position = alien["x_position"] + 3 
        break
    else:
        print("Sorry, please choose slow, medium or fast: ")
        continue
print("Your new position is " + str(x_position)) 

