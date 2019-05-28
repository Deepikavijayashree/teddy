num=int(input())
for k in range(2,num):
    if (num%k==0):
      print("no")
      break
else:
    print("yes")
