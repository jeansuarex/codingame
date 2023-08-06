n = input()
t = input()
count = 0
word = ""
for char in t:
    if char == n:
        count += 1
    else:
        if count > 0:
            word += str(count)
            count = 0
        word += char
if count > 0:
    word += str(count)
print(word)
