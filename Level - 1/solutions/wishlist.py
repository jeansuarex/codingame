wishlist = input().split(', ')
n = int(input()) 
for i in range(n):
    item = input()
    if item in wishlist:
        print("YOINK")
    else:
        print("YEET")
