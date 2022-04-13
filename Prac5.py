str = input()
news = ""
for i in range(len(str)):
    if str[i].islower():
        news += str[i].upper()
        i = i + 1
    else:
        news += str[i].lower()
        i = i + 1
print(news)
