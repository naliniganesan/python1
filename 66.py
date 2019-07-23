nr=int(input())
if(nr>1):
   for i in range(2,nr):
      if(nr%i)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")
