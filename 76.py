s12=int(input())
if(s12>1):
   for i in range (2,s12):
      if(s12%i==0):
       print("yes")
       break
   else:
      print("no")
