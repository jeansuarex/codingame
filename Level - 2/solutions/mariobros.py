n = int(input())
high, low = 0,0
walls = [int(i) for i in input().split()]

current_wall = walls[0]

for i in walls[1:]:
    if current_wall > i or current_wall == i:
        low +=1
    elif current_wall < i :
        high +=1
    current_wall = i
print(high,low)