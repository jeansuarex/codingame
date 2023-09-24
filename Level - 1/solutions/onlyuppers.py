s = input()

b = [i for i in s if i.isupper()]

print(''.join(b)[::-1] or "...")