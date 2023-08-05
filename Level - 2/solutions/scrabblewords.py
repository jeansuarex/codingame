tiles = input()
for i in range(5):
    word = input()
    rest = tiles
    corrects = rest.count("?")
    for h in word:
        if h in rest:
            rest = rest.replace(h,"",1)
            corrects += 1
    if corrects >= len(word):
        print("Yes")
    else:
        print("No")