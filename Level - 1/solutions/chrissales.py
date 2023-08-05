s = int(input())
p = int(input())
t = []
for i in range(p):
    price = int(input())
    t.append(price)
sortedlist = sorted(t)
discount = int(sortedlist[-1] * (s * .01))
total = sum(sortedlist) - discount
print(total)