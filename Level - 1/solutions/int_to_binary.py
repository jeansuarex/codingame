t = input()
c = [bin(i)[2:].zfill(4) for i in [int(h) for h in t.split(",")]]
for i in zip(*c):
    print(''.join(i))

