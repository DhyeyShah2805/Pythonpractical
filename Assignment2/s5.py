# Dhyey Shah 20CS079
# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# https://github.com/DhyeyShah2805/Assignment2.git
from collections import Counter
s = 'aabbcccddddhyeyshah'
print("Original string: "+s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3))
