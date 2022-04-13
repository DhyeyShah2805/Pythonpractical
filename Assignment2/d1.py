# Dhyey Shah 20CS079
# Write a Python script to check whether a given key already exists in a dictionary.
# https://github.com/DhyeyShah2805/Assignment2.git

# Creating function (Maam because i am familiar with this approach)
def checkKey(dict, key):
    # checking condition
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")


dict = {'a': 10, 'b': 20, 'c': 30}

key = 'b'
checkKey(dict, key)

key = 'd'
checkKey(dict, key)