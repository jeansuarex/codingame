
s = input().split()
first, second = None,None
difference = 0
for h in s:
    try:
        if first == None:
            first = int(h)
        elif second == None:
            second = int(h)
    except ValueError:
        if first:    
            if second == None and h == "_":
                difference += 1
steps = (second - first) //  (difference + 1)
firstlines =  len(s[:s.index(str(first))])
lastlines = len(s[s.index(str(second))+1:])
m = []
number = first - (firstlines * steps)
for i in range(len(s)):
    m.append(number)
    number = number + steps
print(*m)

#if you found a better solution than mine, congrats