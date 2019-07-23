n1,n2=map(str,input().split())
if(len(n1)!=len(n2)):
   print("no")
else:
   s1=[n1.count(i) for i in n1]
   s2=[n2.count(i) for i in n2]
if(s1==s2):
   print("yes")
else:
   print("no")
