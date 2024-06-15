n=input()
ln=len(n)
ll=[int(i)**i for i in n]
print(sum(ll)) if sum(ll)==int(n) else print(-1)

