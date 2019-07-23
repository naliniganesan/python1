r11,r21=map(int,input().split())
for i in range(0,(r11*r21)+1):
   if(i**2==0):
      print("yes")
      break
else:
   print("no")
