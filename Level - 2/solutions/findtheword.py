n = int(input())
completes = [input() for i in range(n)]
m = int(input())
incomplete = [input() for i in range(m)]


for h in incomplete:
    same_length = [i for i in completes if len(i)==len(h)]
    matches = 0
    word = ""
    #looking for the best match (sorry for the variable names)
    for i in same_length:
        m = 0
        for q,w in zip(h,i):
            if q == w:
                m +=1
            if m > matches:
                matches = m
                word = i
    print(word)