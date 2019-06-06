x,y=[int(x) for x in input().split()]
for a in range(x,y):
  sum=0
  temp=a
  while temp > 0:
    d = temp % 10
    sum=sum + d ** 3
    temp = temp // 10
  if(a==sum):
    print(a)
