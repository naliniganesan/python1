ns=input()
l2=list(map(int,input().split()))
for i in range(len(l2)-1):
   if(l2[i]>l2[i+1]):
      print(i)
