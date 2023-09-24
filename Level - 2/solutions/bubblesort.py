n = int(input())
p = list(map(int, input().split()))
passes = int(input())

for _ in range(passes):
    for h in range(len(p) - 1):
        if p[h] > p[h+1]:
            p[h], p[h+1] = p[h+1], p[h]

print(*p)
