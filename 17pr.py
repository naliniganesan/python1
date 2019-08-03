mn1,mn2=map(int,input().split())
for i in range(1,100000):
   if(i%mn1==0 and i%mn2==0):
      print(i)
      break
