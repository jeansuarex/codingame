n = int(input())
k = list(map(int, input().split()))

final = [k]

while len(k) != 1:
    k = [k[i] + k[i+1] for i in range(len(k) - 1)]
    final.append(k)

for i, row in enumerate(final):
    print(" " * i + " ".join(str(num) for num in row))