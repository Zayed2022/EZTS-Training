A = [1, 2, 3, 4, 5,6]
k=3
m=-float('inf')
for i in range((len(A)//2)+1):
    l=A[i:i+k]
    print(l)
    ll=[(i+1)*l[i] for i in range(len(l))]
    s=sum(ll)
    m=max(s,m)
print(m)
