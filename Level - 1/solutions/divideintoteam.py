a = input().split(", ")
n = int(input())

for i in range(n):
    print(f"Team {i+1}: {', '.join(a[i::n])}")
