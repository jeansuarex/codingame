x = int(input())
y = int(input())
k = int(input())
for i in range(y):
    row = input()
    for _ in range(k):
        print(row.replace('0','  '*k).replace('1',' *'*k))