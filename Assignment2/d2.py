# Dhyey Shah 20CS079
#  Write a Python script to merge two Python dictionaries.
# https://github.com/DhyeyShah2805/Assignment2.git
def dictMerge(dict1, dict2):
    return dict2.update(dict1)


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This return None
print(dictMerge(dict1, dict2))

# changes made in dict2
print(dict2)