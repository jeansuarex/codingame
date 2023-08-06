days = "Mo Tu We Th Fr Sa Su".split() * 2
a, b = input().split("-")
start = days.index(a)
finish = days.index(b, start+1)
days_open = days[start:finish+1]

n = int(input())
for i in range(n):
    day = input()
    if day in days_open:
        print("yes")
    else:
        print("no")