# Dhyey Shah 20CS079
# Write a Python program to sum all the items in a dictionary.
# https://github.com/DhyeyShah2805/Assignment2.git
def Summation(dict):
    # counter of summation
    sum = 0
    # for loop for iterating values in dictionary
    for i in dict.values():
        sum = sum + i
    return sum


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300, 'd':500}
print("Sum :", Summation(dict))