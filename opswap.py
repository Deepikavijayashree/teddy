x,y = [int(x) for x in input().split()]
x = x ^ y
y = x ^ y
x = x ^ y
print(x,y)
