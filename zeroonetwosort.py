a = [2, 1, 0, 1, 1, 2, 0, 0]
n = len(a)
c0,c1,c2 =0,0,0
for i in range(n):
    if a[i]==0:
        c0+=1
    if a[i]==1:
        c1+=1
    if a[i]==2:
        c2+=1
j=0
print(c0,c1,c2)
while c0>0:
    a[j]=0
    j+=1
    c0-=1
while c1>0:
    a[j]=1
    j+=1
    c1-=1
while c2>0:
    a[j]=2
    j+=1
    c2-=1
print(a)

