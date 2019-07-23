d1=str(input())
s1=list(d1)
r1=len(d1)
p1=""
if r1%2==0:
   s1[int(r1/2)]=="*"
   s1[int(r1/2-1)]=="*"
else:
   s1[int(r1/2)]=="*"
p1=p1.join(s1)
print(p1)
