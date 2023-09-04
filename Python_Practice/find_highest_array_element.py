nums = [12, 7645, 543, 4]

def find_highest(arrays):
    cheese = len(arrays) #4

    while cheese > 1:
        print("running one iteration")
        if arrays[0] > arrays[1]:
            print(f"{arrays[1]} is smaller than {arrays[0]} - Removing")
            arrays.pop(1)
        elif arrays[0] < arrays[1]:
            print(f"{arrays[0]} is smaller than {arrays[1]} - Removing")
            arrays.pop(0)
        cheese -= 1
    return arrays

print(find_highest(nums))