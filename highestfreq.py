from collections import Counter
s="NIGGA"
c=Counter(s)
m=0
for i,j in c.items():
    if j>m:
        m=j
        k=i
print(k)