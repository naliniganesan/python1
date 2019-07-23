ef soe(n1):
   for i in range(n1+1):
      q=2
while(q*q<=n1):
   if(prime(q)==1):
      for i in range(q*2,n1+1,q):
         prime(i)=0
      q+=1
   for q in range(2,n1):
      if(prime(q)):
         print(q)
