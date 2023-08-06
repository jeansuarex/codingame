name = input()

reverse_name = name[::-1]

palindromized = ""
for i, y in zip(name,reverse_name):
    palindromized += i
    palindromized += y

print(palindromized)
