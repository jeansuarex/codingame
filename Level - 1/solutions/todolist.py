t = int(input())
todolist = []
for i in range(t):
    item = input()
    todolist.append(item)

dones = []
n = int(input())
for i in range(n):
    done = input()
    dones.append(done)

todolist = sorted(todolist)

for i in todolist:
    if i not in dones:
        print(i)