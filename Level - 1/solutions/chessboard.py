n = int(input())
a, b = (0, 1) if n % 2 == 0 else (1, 0)
for i in range(n):
    for h in range(n):
        print(a if (i + h) % 2 == 0 else b, end="")
    print()

#this is my solution, i just wanted to save some lines of code
