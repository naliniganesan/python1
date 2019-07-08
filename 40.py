n1=int(input())
a,b=0,1
print(b,end=" ")
for i in range(1,n1):
  fb=a+b
  print(fb,end=" ")
  a,b=b,fb
