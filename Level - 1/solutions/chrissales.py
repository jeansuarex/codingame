import math
s = int(input())
p = int(input())
maximum = float('-inf')
total = 0
for i in range(p):
    prices = int(input())
    if prices > maximum:
        maximum = prices
    total += prices
print(math.ceil(total - (maximum * (s / 100))))