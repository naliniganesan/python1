n1=input()
s1=list(input())
lp1=['a','e','i','o','u','A','E','I','E','O','U']
dn1=[]
for i in s1:
   if i not in lp1:
      dn1.append(i)
print(''.join(map(str,dn1[::-1])))
