n = int(input())
for i in range(n):
    word = input()
    vowels = []
    for vowel in "aAeEiIoOuU":
        if vowel in word:
            vowels.append(vowel)
    if not vowels:
        print("NONE")
    else:
        print(vowels[0])