from itertools import combinations
sa,vm = input().split()
vm = int(vm)
san1 = []
hj = combinations(sa,len(sa)-vm)
for d in hj:
    san1.append("".join(d))
print(min(san1))
