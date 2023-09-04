usernames = []

#5.8
for name in usernames:
    if name == "admin":
        print(f"Hello, {name.title()}")
    else:
        print(f"Hello {name}, welcome back!")

#5.9
if (len(usernames)) == 0:
    print("We need more users!")

#5.10

current_users = ["bob", "jim", "wendy", "stacey", "carl"]
new_users = ["bob", "steve", "kevin", "carl", "dom"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username, {new_user.title()} has been taken. Please enter a new username.")

#5.11

nums = list(range(1, 10))
for num in nums:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 2:
        print(f"{num}rd")
    else: 
        print(f"{num}th")