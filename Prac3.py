from collections import Counter

K = int(input())
k = Counter(list(map(int, input().split())))
for i in k:
    if k[i] == 1:
        print(i)
        break
