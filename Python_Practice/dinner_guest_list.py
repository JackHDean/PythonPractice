def invites():
    for name in dinner_guests:
        print("Hello, " + name + "!\nWould you like to come to dinner?\n")

#3.4

dinner_guests = ["Steve", "Carl", "Bill"]
invites()

#3.5

unavailable = dinner_guests[2]
print(unavailable + " can not make it to dinner!\n")
dinner_guests[2] = "Freddie"
invites()

#3.6

print("Good news! I have found a larger table! More room means more guests!\n")
dinner_guests.insert(0, "Dom")
dinner_guests.insert(1, "Lisa")
dinner_guests.append("Jason")
invites()

#3.7
for name in dinner_guests:
    while len(dinner_guests) > 2: 
        removed_guests = dinner_guests.pop()
        print("Apologies, " + removed_guests + ". The table won't come on time! There is no room for you.\n")


for name in dinner_guests:
    print("Hi, " + name + "! You are still invited, See you there!\n")

while len(dinner_guests) != 0:
    del dinner_guests[0]
print(dinner_guests)


