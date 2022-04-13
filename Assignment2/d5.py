# Dhyey Shah 20CS079
# Write a Python script to concatenate following dictionaries to create a new one
# https://github.com/DhyeyShah2805/Assignment2.git
dict1 = {'a': 100, 'b': 78}
dict2 = {'c': 23, 'd': 768}
dict3 = {'e': 900, 'f': 32}
dict4 = {}
for dict in (dict1,dict2,dict3):dict4.update(dict)
print("New Dictionary is",dict4)