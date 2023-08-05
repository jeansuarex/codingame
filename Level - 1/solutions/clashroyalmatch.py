health = int(input())
level = int(input())
first = 200
totaldamage = (level - 1) * 20 + 200

result = health - totaldamage
if totaldamage >= health:
    print(f"hehehehaw {result}")
else:
    print(f"rawr {result}")
