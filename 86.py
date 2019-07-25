sh1=list(input())
sh2=[]
for i in sh1:
   if(i not in sh2):
      sh2.append(i)
if(sh1=sh2):
   print("Yes")
else:
   print("No")
