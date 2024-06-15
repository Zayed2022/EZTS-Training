## 8^1 + 9^2 = 89.
n=input()
ln=len(n)
ll=[int(n[i])**(i+1) for i in range(ln)]
print(sum(ll)) if sum(ll)==int(n) else print(-1)

