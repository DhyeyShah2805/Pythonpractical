# Dhyey Shah 20CS079
# Write a Python program to remove an item from a set if it is present in the set.
# https://github.com/DhyeyShah2805/Assignment2.git

def Remove(sets):
    sets.discard(20)
    print(sets)


# Driver Code
sets = {10, 20, 26, 41, 54}
Remove(sets)