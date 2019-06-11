def large(x,n):
  max=x[0]
  for i in range(1,n):
    if x[i]>max:
      max=x[i]
  return max
x=[int(i) for i in input().split()]
n=len(x)
answer=large(x,n)
print(answer)
