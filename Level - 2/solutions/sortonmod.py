n = int(input())
s = [int(i) for i in input().split()]
mod = sorted([i for i in s if i % n == 0])

index = 0
for i in range(len(s)):
    if s[i] % n == 0:
        s[i] = mod[index]
        index += 1

print(*s)
