n = int(input())
data = [int(i) for i in input().split()]

if data:
    actual = data[0]
    l = [data[0]]
    for i in data[1:]:
        h = i - actual
        l.append(h)
        actual = i
    print(*l)
else:
    print("None")
