s = 0 
A = 0
for i in input().split():
    a = int(i)
    s+=a
    A = min(A,s)
    if s>0:
        s=0
print(A)
