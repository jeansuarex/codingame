n = int(input())
w = [input() for _ in range(n)]

task = "to infinity and beyond"

c = []
while task:
    match = False
    for i in w:
        if task[0] in i.lower():
            c.append(i)
            w.remove(i)
            task = task[1:]
            match = True
            break
    if not match:
        print("Red alert!!!")
        break

if not task:
    for i in c:
        print(i)
